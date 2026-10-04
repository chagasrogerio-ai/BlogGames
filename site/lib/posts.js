import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { marked } from "marked";

const dir = path.join(process.cwd(), "..", "content", "posts");

const toDay = (d) => (d instanceof Date ? d.toISOString() : String(d)).slice(0, 10);

export function getAllPosts() {
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".md"))
    .map((f) => {
      const { data } = matter(fs.readFileSync(path.join(dir, f), "utf8"));
      return { ...data, date: toDay(data.date) };
    })
    .filter((p) => p.date <= new Date().toISOString().slice(0, 10))
    .sort((a, b) => (a.date < b.date ? 1 : -1));
}

export function getPost(slug) {
  const file = path.join(dir, `${slug}.md`);
  if (!fs.existsSync(file)) return null;
  const { data, content } = matter(fs.readFileSync(file, "utf8"));
  return { ...data, date: toDay(data.date), html: marked.parse(content) };
}
