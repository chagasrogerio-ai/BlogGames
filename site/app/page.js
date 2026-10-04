import { getAllPosts } from "../lib/posts";

export default function Home() {
  const posts = getAllPosts();
  return (
    <>
      <h1>História e análise de games retrô</h1>
      <p className="meta">Clássicos, indies e a cultura por trás dos jogos, em português.</p>
      {posts.map((p) => (
        <div className="card" key={p.slug}>
          <h2><a href={`/posts/${p.slug}`}>{p.title}</a></h2>
          <div className="meta">{p.date} · {p.category}</div>
          <p>{p.excerpt}</p>
        </div>
      ))}
    </>
  );
}
