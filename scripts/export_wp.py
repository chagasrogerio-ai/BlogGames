"""Converte content/posts/*.md em um arquivo WXR para importar no WordPress.

Uso: python scripts/export_wp.py
Depois: WordPress > Ferramentas > Importar > WordPress > enviar wordpress-import.xml
Requer: pip install markdown python-frontmatter
"""
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

import frontmatter
import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "wordpress-import.xml"

CATEGORIES = {"historia": "História", "analise": "Análise", "guia": "Guia"}


def cdata(text: str) -> str:
    return "<![CDATA[" + text.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def to_date(value) -> datetime:
    if isinstance(value, datetime):
        return value
    if hasattr(value, "year"):
        return datetime(value.year, value.month, value.day, 9, 0)
    return datetime.fromisoformat(str(value))


items = []
for f in sorted((ROOT / "content" / "posts").glob("*.md")):
    post = frontmatter.load(f)
    dt = to_date(post["date"]).strftime("%Y-%m-%d %H:%M:%S")
    html = markdown.markdown(post.content, extensions=["tables"])
    cat = post.get("category", "")
    cat_xml = (
        f'<category domain="category" nicename="{escape(cat)}">{cdata(CATEGORIES.get(cat, cat))}</category>'
        if cat
        else ""
    )
    tags_xml = "".join(
        f'<category domain="post_tag" nicename="{escape(str(t))}">{cdata(str(t))}</category>'
        for t in post.get("tags", [])
    )
    items.append(f"""
  <item>
    <title>{cdata(post["title"])}</title>
    <dc:creator>{cdata("admin")}</dc:creator>
    <content:encoded>{cdata(html)}</content:encoded>
    <excerpt:encoded>{cdata(post.get("excerpt", ""))}</excerpt:encoded>
    <wp:post_date>{cdata(dt)}</wp:post_date>
    <wp:post_name>{cdata(post["slug"])}</wp:post_name>
    <wp:status>{cdata("publish")}</wp:status>
    <wp:post_type>{cdata("post")}</wp:post_type>
    {cat_xml}{tags_xml}
  </item>""")

OUT.write_text(
    """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
  xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:wp="http://wordpress.org/export/1.2/">
<channel>
  <title>Retro Games BR</title>
  <wp:wxr_version>1.2</wp:wxr_version>"""
    + "".join(items)
    + "\n</channel>\n</rss>\n",
    encoding="utf-8",
)
print(f"{len(items)} posts exportados para {OUT}")
