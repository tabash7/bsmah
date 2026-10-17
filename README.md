# بصمة لحلول التقنية

Arabic, right-to-left static website for `https://bsmah.com/`. Contact: `info@bsmah.com`.

## Contents

- `index.html`: company homepage, services, EMPID, blog entry points, contact.
- `content/posts.json`: 16 Bsmah articles with independent titles, summaries, and practical guidance.
- `tools/build_blog.py`: creates all blog pages and `sitemap.xml` from the article source.
- `assets/bsmah-mark.svg`, `assets/bsmah-og.webp`: Bsmah brand mark and social preview.
- `assets/blog/`: compressed 480 px and 1200 px WebP editorial photography.
- `assets/empid/`: screenshots from the Arabic EMPID Al Ofoq demonstration tenant using test data.
- `BRAND.md`: visual and editorial identity.
- `SEO.md`: search setup and cross-site editorial linking approach.

## Build and preview

From `D:\bsmah`, run `python tools/build_blog.py`, then `python -m http.server 4174`. Open `http://127.0.0.1:4174/`.

Publish at the root of `https://bsmah.com/`. The pages use root-relative asset paths and canonical URLs at that domain. The email actions open the visitor's mail app; the site has no contact form.

The shared editorial photographs are unbranded illustrative assets. The new logo, homepage copy, article copy, and social preview are specific to Bsmah. The original AlRetaj badge and banner are not referenced by any published Bsmah page.

The unused copied AlRetaj badge and banner remain in `assets/`; remove them during a later cleanup if permitted. They are not requested by pages and do not affect page download size.
