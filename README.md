# Retro Games BR

Um conteúdo (`content/posts/*.md`), dois sites.

```
content/posts/   fonte única dos artigos (Markdown + frontmatter)
site/            Next.js -> Vercel (grátis)
supabase/        schema de newsletter e cliques de afiliados
scripts/         export_wp.py -> gera wordpress-import.xml para a Hostinger
```

## Rodar o site localmente
```
cd site
npm install
npm run dev      # http://localhost:3000
```

## Publicar na Vercel
1. `git init`, commit e push para um repositório no GitHub.
2. Vercel > Add New Project > importar o repositório.
3. Root Directory: `site`. Ative "Include source files outside of the Root Directory" (o site lê `../content`).

## Enviar para o WordPress (Hostinger)
```
pip install markdown python-frontmatter
python scripts/export_wp.py
```
No WordPress: Ferramentas > Importar > WordPress > envie `wordpress-import.xml`.

## Novo artigo
Crie `content/posts/meu-slug.md` com `title`, `slug`, `date`, `category`, `excerpt`, `tags`.
Posts com data futura ficam ocultos até o próximo deploy após a data.
