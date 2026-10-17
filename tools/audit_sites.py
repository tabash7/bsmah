"""Audit generated pages on both local sites before publication."""

import json
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup

BSMAH = Path(__file__).resolve().parents[1]
ALRETAJ = Path("D:/alretaj")


def audit(root: Path, domain: str) -> tuple[int, int]:
    pages = [root / "index.html", *sorted((root / "blog").rglob("index.html"))]
    problems: list[str] = []
    externals = 0
    for page in pages:
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        rel = page.relative_to(root)
        route = "/" if rel == Path("index.html") else "/" + str(rel.parent).replace("\\", "/") + "/"
        canonical = soup.find("link", rel="canonical")
        if canonical is None or canonical.get("href") != f"https://{domain}{route}":
            problems.append(f"{rel}: incorrect canonical")
        if len(soup.find_all("h1")) != 1:
            problems.append(f"{rel}: expected one h1")
        if not soup.title or not soup.find("meta", attrs={"name": "description"}):
            problems.append(f"{rel}: title or description missing")
        for tag in soup.find_all(["a", "img", "script", "link"]):
            attr = "href" if tag.name in {"a", "link"} else "src"
            url = tag.get(attr, "")
            if url.startswith("https://alretaj.com/") and domain == "bsmah.com":
                externals += 1
            elif url.startswith("https://bsmah.com/") and domain == "alretaj.com":
                externals += 1
            if not url.startswith("/") or url.startswith("//"):
                continue
            parsed = urlparse(url)
            relative = unquote(parsed.path).lstrip("/")
            target = root / relative
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                problems.append(f"{rel}: missing {url}")
    if problems:
        raise AssertionError("\n".join(problems))
    return len(pages), externals


def compare_posts() -> tuple[int, float]:
    a = {p["slug"]: p for p in json.loads((ALRETAJ / "content/posts.json").read_text(encoding="utf-8"))}
    b = {p["slug"]: p for p in json.loads((BSMAH / "content/posts.json").read_text(encoding="utf-8"))}
    assert a.keys() == b.keys() and len(a) == 16
    ratios = []
    for slug in a:
        assert a[slug]["title"] != b[slug]["title"], slug
        def body(post: dict) -> str:
            return " ".join(post["intro"] + [x for s in post["sections"] for x in s["paragraphs"]] + [post["takeaway"]])
        ratios.append(SequenceMatcher(None, body(a[slug]), body(b[slug])).ratio())
    return len(ratios), max(ratios)


if __name__ == "__main__":
    bsmah_pages, bsmah_links = audit(BSMAH, "bsmah.com")
    alretaj_pages, alretaj_links = audit(ALRETAJ, "alretaj.com")
    articles, highest_similarity = compare_posts()
    assert bsmah_links == 3 and alretaj_links == 3
    print(f"Bsmah: {bsmah_pages} pages, {bsmah_links} contextual AlRetaj links")
    print(f"AlRetaj: {alretaj_pages} pages, {alretaj_links} contextual Bsmah links")
    print(f"Articles: {articles}; highest body similarity: {highest_similarity:.2%}")
