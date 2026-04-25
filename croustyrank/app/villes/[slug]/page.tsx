import Link from "next/link";
import { getRestaurantsByCity, getCities, getGlobalScore, VERDICT_CONFIG } from "@/lib/data";
import { notFound } from "next/navigation";
import type { Metadata } from "next";

export async function generateStaticParams() {
  return getCities().map((city) => ({ slug: city.toLowerCase() }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const city = slug.charAt(0).toUpperCase() + slug.slice(1);
  return {
    title: `Meilleur crousty à ${city} — CroustyRank`,
    description: `Classement des restaurants crousty à ${city} : Tasty Crousty, Krousty Sabaïdi. Noté sur croustillant, poulet, sauce, tenue et prix.`,
  };
}

function RatingBar({ label, value }: { label: string; value: number }) {
  return (
    <div className="flex items-center gap-2 text-sm">
      <span className="text-neutral-500 w-24 text-right shrink-0 text-xs">{label}</span>
      <div className="flex-1 bg-[#2a2a2a] rounded-full h-1.5">
        <div
          className={`h-1.5 rounded-full ${value >= 4.5 ? "bg-green-500" : value >= 3.5 ? "bg-orange-500" : "bg-red-500"}`}
          style={{ width: `${(value / 5) * 100}%` }}
        />
      </div>
      <span className={`text-xs font-bold w-8 ${value >= 4.5 ? "text-green-400" : value >= 3.5 ? "text-orange-400" : "text-red-400"}`}>
        {value.toFixed(1)}
      </span>
    </div>
  );
}

export default async function VillePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const city = slug.charAt(0).toUpperCase() + slug.slice(1);
  const restaurants = getRestaurantsByCity(city);

  if (restaurants.length === 0) notFound();

  const sorted = [...restaurants].sort(
    (a, b) => parseFloat(getGlobalScore(b)) - parseFloat(getGlobalScore(a))
  );

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-8">
      <div>
        <Link href="/" className="text-sm text-neutral-500 hover:text-orange-400 transition-colors">← Retour</Link>
        <h1 className="text-4xl font-black mt-2">
          Crousty à <span className="text-orange-500">{city}</span>
        </h1>
        <p className="text-neutral-400 mt-1 text-sm">
          {restaurants.length} restaurant{restaurants.length > 1 ? "s" : ""} · noté sur 5 critères par la communauté
        </p>
      </div>

      <div className="space-y-4">
        {sorted.map((r, i) => {
          const vc = VERDICT_CONFIG[r.verdict];
          return (
            <Link
              key={r.id}
              href={`/restaurants/${r.id}`}
              className="block bg-[#141414] hover:bg-[#1e1e1e] border border-[#2a2a2a] rounded-2xl p-5 transition-colors group"
            >
              <div className="flex items-start justify-between gap-4 mb-3">
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className={`text-xl font-black ${i === 0 ? "text-yellow-400" : "text-neutral-600"}`}>#{i + 1}</span>
                    <span className="font-bold text-lg group-hover:text-orange-400 transition-colors">{r.name}</span>
                  </div>
                  <p className="text-xs text-neutral-500 mt-0.5">{r.address}</p>
                  <div className="flex items-center gap-2 mt-2 flex-wrap">
                    <span className={`text-xs px-2 py-0.5 rounded border font-bold ${vc.bg} ${vc.color}`}>
                      {vc.emoji} {r.verdict}
                    </span>
                    <div className="flex gap-1">
                      {r.sauces.map((s) => (
                        <span key={s} className="text-xs bg-[#2a2a2a] text-neutral-500 px-1.5 py-0.5 rounded">{s}</span>
                      ))}
                    </div>
                  </div>
                </div>
                <div className="text-right shrink-0">
                  <div className="text-3xl font-black text-orange-400">★ {getGlobalScore(r)}</div>
                  <div className="text-xs text-neutral-600">{r.reviewCount} avis</div>
                </div>
              </div>

              {/* Verdict text */}
              <p className="text-xs text-neutral-400 italic mb-3 border-l-2 border-[#2a2a2a] pl-3">
                &quot;{r.verdictText}&quot;
              </p>

              <div className="space-y-1.5">
                <RatingBar label="Croustillant" value={r.ratings.croustillant} />
                <RatingBar label="Poulet" value={r.ratings.poulet} />
                <RatingBar label="Sauce" value={r.ratings.sauce} />
                <RatingBar label="Prix/Plaisir" value={r.ratings.prix_plaisir} />
                <RatingBar label="Tenue" value={r.ratings.tenue} />
              </div>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
