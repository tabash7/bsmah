"""Retint the shared layout to the Bsmah palette and add its own art direction."""

from pathlib import Path

path = Path(__file__).resolve().parents[1] / "styles.css"
css = path.read_text(encoding="utf-8")
palette = {
    "#071a34": "#142d35",
    "#0d294c": "#1b4047",
    "#142640": "#21363d",
    "#627087": "#5b7072",
    "#d9a647": "#65b9a9",
    "#efc979": "#a5e1d5",
    "#f7f4ee": "#f4efe6",
    "#dce1e7": "#d5e0db",
    "#123865": "#2f6a70",
    "#0b2444": "#1b454c",
    "#173b65": "#2c6669",
    "#14365c": "#285d63",
    "#12345b": "#214a50",
    "#06152a": "#10272e",
    "#a87827": "#317f76",
    "#94691c": "#317f76",
    "#8b611a": "#276e66",
    "#996e20": "#276e66",
    "#92671e": "#276e66",
    "#b2873a": "#398f83",
    "#b6812b": "#398f83",
    "#d7ad5a": "#a5e1d5",
    "#f2c977": "#a5e1d5",
    "#f3c76a": "#a5e1d5",
    "#f5ca70": "#a5e1d5",
    "#e6b450": "#74c7b8",
    "#e8bb60": "#74c7b8",
    "#eebf5d": "#74c7b8",
    "#bd8a33": "#317f76",
    "#d9ab54": "#74c7b8",
    "#efc467": "#a5e1d5",
    "#e8edf2": "#e6efea",
    "#e9eef3": "#e6efea",
    "#f7f6f2": "#f3f4ef",
    "#f7f4ee": "#f4efe6",
}
for old, new in palette.items():
    css = css.replace(old, new)
css += """

/* Bsmah art direction: calm geometry, generous space, and a fingerprint mark. */
.brand img,.footer-brand img{border-radius:12px;background:#142d35;border:0}
.hero{background:radial-gradient(circle at 18% 38%,#376b6b 0,#1b454c 39%,#142d35 78%)}
.hero:before{border-color:rgba(165,225,213,.19)}
.hero-pattern{background:repeating-radial-gradient(circle at 71% 52%,transparent 0 46px,rgba(165,225,213,.045) 47px 48px)}
.hero-visual-frame{border:1px solid rgba(165,225,213,.5);border-radius:24px;transform:none;padding:23px;background:rgba(255,255,255,.035)}
.hero-visual-frame img{transform:none;border-radius:18px;background:#142d35}
.button-gold{background:#a5e1d5;color:#142d35;border-radius:6px}
.button-gold:hover{background:#f4efe6}
.button-outline,.nav-contact{border-radius:6px}
.blog-card{border-top:0;border-right:4px solid #65b9a9;border-radius:4px}
.article-next{border-color:#65b9a9}
.article-featured{border-radius:8px;overflow:hidden}
.banner-frame{border-radius:10px;background:#214a50;overflow:hidden}
.contact{background:#e6efea}
.blog-landing-hero,.article-hero{background:radial-gradient(circle at 12% 35%,#2c6669,#142d35 68%)}
"""
path.write_text(css, encoding="utf-8")
print("Applied Bsmah palette")
