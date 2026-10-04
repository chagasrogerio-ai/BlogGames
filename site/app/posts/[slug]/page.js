import { notFound } from "next/navigation";
import { getAllPosts, getPost } from "../../../lib/posts";

export function generateStaticParams() {
  return getAllPosts().map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }) {
  const { slug } = await params;
  const post = getPost(slug);
  return post ? { title: post.title, description: post.excerpt } : {};
}

export default async function PostPage({ params }) {
  const { slug } = await params;
  const post = getPost(slug);
  if (!post) notFound();
  return (
    <article>
      <h1>{post.title}</h1>
      <div className="meta">{post.date} · {post.category}</div>
      <div dangerouslySetInnerHTML={{ __html: post.html }} />
    </article>
  );
}
