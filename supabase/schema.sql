-- Rode no SQL Editor do Supabase.

create table if not exists newsletter (
  id bigint generated always as identity primary key,
  email text not null unique,
  created_at timestamptz default now()
);

create table if not exists affiliate_clicks (
  id bigint generated always as identity primary key,
  post_slug text not null,
  program text,
  url text,
  created_at timestamptz default now()
);

alter table newsletter enable row level security;
alter table affiliate_clicks enable row level security;

-- Visitantes (chave anon) só podem inserir; ninguém lê pelo navegador.
create policy "anon insere newsletter" on newsletter for insert to anon with check (true);
create policy "anon insere cliques" on affiliate_clicks for insert to anon with check (true);
