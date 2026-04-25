import type { Metadata } from "next";
import "./globals.css";
import Navbar from "@/components/Navbar";

export const metadata: Metadata = {
  title: "CroustyRank — Le classement communautaire du crousty",
  description: "Compare les restaurants Tasty Crousty et Krousty Sabaïdi, vote pour le Grand Débat et trouve le meilleur crousty dans ta ville.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr" className="h-full">
      <body className="min-h-full flex flex-col bg-[#0a0a0a] text-[#f5f5f0]">
        <Navbar />
        <main className="flex-1">{children}</main>
        <footer className="border-t border-[#2a2a2a] py-6 text-center text-sm text-neutral-500 mt-12">
          CroustyRank — La référence communautaire du crousty 🍚🍗
        </footer>
      </body>
    </html>
  );
}
