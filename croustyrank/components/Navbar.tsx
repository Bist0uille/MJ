"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Classement" },
  { href: "/le-grand-debat", label: "🥊 Grand Débat" },
  { href: "/sauce-builder", label: "🍶 Combos" },
  { href: "/ouvertures", label: "📍 Ouvertures" },
  { href: "/faux-crousty", label: "🚨 Faux Crousty" },
];

export default function Navbar() {
  const path = usePathname();
  return (
    <nav className="sticky top-0 z-50 border-b border-[#2a2a2a] bg-[#0a0a0a]/95 backdrop-blur">
      <div className="max-w-6xl mx-auto px-4 flex items-center gap-6 h-14">
        <Link href="/" className="font-black text-xl tracking-tight">
          <span className="text-orange-500">CROUSTY</span>
          <span className="text-white">RANK</span>
        </Link>
        <div className="flex items-center gap-1 overflow-x-auto scrollbar-hide flex-1">
          {links.map((l) => (
            <Link
              key={l.href}
              href={l.href}
              className={`px-3 py-1.5 rounded-lg text-sm font-medium whitespace-nowrap transition-colors ${
                path === l.href
                  ? "bg-orange-500 text-white"
                  : "text-neutral-400 hover:text-white hover:bg-white/5"
              }`}
            >
              {l.label}
            </Link>
          ))}
        </div>
      </div>
    </nav>
  );
}
