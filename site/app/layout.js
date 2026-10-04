import "./globals.css";

export const metadata = {
  title: "Retro Games BR",
  description: "História e análise de games retrô e indie, em português.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body>
        <header>
          <a href="/">Retro Games BR</a>
        </header>
        <main>{children}</main>
        <footer>
          Alguns links podem ser de afiliados: sem custo extra para você, o blog pode receber comissão.
        </footer>
      </body>
    </html>
  );
}
