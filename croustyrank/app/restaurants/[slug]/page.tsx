import Link from "next/link";
import { getRestaurantById, restaurants, getGlobalScore, VERDICT_CONFIG } from "@/lib/data";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import RestaurantClient from "./RestaurantClient";

export async function generateStaticParams() {
  return restaurants.map((r) => ({ slug: r.id }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const r = getRestaurantById(slug);
  if (!r) return { title: "Restaurant introuvable" };
  return {
    title: `${r.name} — ${r.verdict} · CroustyRank`,
    description: `${r.verdictText} Note : ${getGlobalScore(r)}/5 · ${r.reviewCount} avis.`,
  };
}

export default async function RestaurantPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const r = getRestaurantById(slug);
  if (!r) notFound();

  const brandColor = r.brand === "Tasty Crousty" ? "#f97316" : r.brand === "Krousty Sabaïdi" ? "#22c55e" : "#737373";
  const vc = VERDICT_CONFIG[r.verdict];

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-8">
      <div>
        <Link href={`/villes/${r.city.toLowerCase()}`} className="text-sm text-neutral-500 hover:text-orange-400 transition-colors">
          ← {r.city}
        </Link>
        <div className="flex items-start justify-between gap-4 mt-2">
          <div>
            <h1 className="text-3xl font-black">{r.name}</h1>
            <p className="text-neutral-500 text-sm mt-1">{r.address}</p>
            <div className="flex items-center gap-2 mt-2 flex-wrap">
              <span
                className="px-2 py-0.5 rounded text-xs font-bold border"
                style={{ color: brandColor, borderColor: `${brandColor}40`, backgroundColor: `${brandColor}15` }}
              >
                {r.brand}
              </span>
              <span className={`text-xs px-2 py-0.5 rounded border font-bold ${vc.bg} ${vc.color}`}>
                {vc.emoji} {r.verdict}
              </span>
            </div>
          </div>
          <div className="text-right shrink-0">
            <div className="text-4xl font-black text-orange-400">★ {getGlobalScore(r)}</div>
            <div className="text-sm text-neutral-500">{r.reviewCount} avis</div>
          </div>
        </div>
      </div>

      {/* Sauces dispo */}
      <section className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5">
        <h2 className="font-bold mb-3">🍶 Sauces disponibles</h2>
        <div className="flex gap-2 flex-wrap">
          {r.sauces.map((s) => (
            <span key={s} className="bg-[#2a2a2a] text-neutral-300 px-3 py-1.5 rounded-lg text-sm font-medium">{s}</span>
          ))}
        </div>
      </section>

      <RestaurantClient restaurant={r} />

      {r.uberEatsUrl && (
        <div className="bg-orange-500/10 border border-orange-500/20 rounded-2xl p-5 flex items-center justify-between gap-4">
          <div>
            <h3 className="font-bold text-orange-400">Commander maintenant</h3>
            <p className="text-sm text-neutral-500">Livraison via UberEats</p>
          </div>
          <a href={r.uberEatsUrl} className="bg-orange-500 hover:bg-orange-400 text-white font-bold px-5 py-2.5 rounded-xl transition-colors">
            Commander →
          </a>
        </div>
      )}
    </div>
  );
}
