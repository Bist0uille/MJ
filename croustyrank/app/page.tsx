import Link from "next/link";
import { getRankedRestaurants, grandDebatVotes, getCities, getGlobalScore, VERDICT_CONFIG } from "@/lib/data";

function BrandBadge({ brand }: { brand: string }) {
  const styles: Record<string, string> = {
    "Tasty Crousty": "bg-orange-500/20 text-orange-400 border border-orange-500/30",
    "Krousty Sabaïdi": "bg-green-500/20 text-green-400 border border-green-500/30",
    "Kebab": "bg-neutral-500/20 text-neutral-400 border border-neutral-500/30",
  };
  return (
    <span className={`px-2 py-0.5 rounded text-xs font-semibold ${styles[brand] ?? styles["Kebab"]}`}>
      {brand}
    </span>
  );
}

export default function HomePage() {
  const ranked = getRankedRestaurants().slice(0, 10);
  const cities = getCities();
  const total = grandDebatVotes.tastyCrousty + grandDebatVotes.kroustySabaidi;
  const tcPct = Math.round((grandDebatVotes.tastyCrousty / total) * 100);
  const ksPct = 100 - tcPct;

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 space-y-12">
      {/* Hero */}
      <section className="text-center space-y-4 py-8">
        <div className="inline-block bg-orange-500/10 border border-orange-500/20 text-orange-400 text-xs font-bold px-3 py-1 rounded-full mb-2">
          +323% sur UberEats en 12 mois 🚀
        </div>
        <h1 className="text-5xl md:text-7xl font-black tracking-tight">
          Le meilleur crousty<br />
          <span className="text-orange-500">c&apos;est lequel ?</span>
        </h1>
        <p className="text-neutral-400 text-lg max-w-xl mx-auto">
          Le classement communautaire du riz pané qui a rendu fous les ados français.
          On note vraiment : croustillant, poulet, sauce, tenue.
        </p>
        <div className="flex flex-wrap gap-3 justify-center pt-2">
          <Link href="/le-grand-debat" className="bg-orange-500 hover:bg-orange-400 text-white font-bold px-6 py-3 rounded-xl transition-colors">
            🥊 Le Grand Débat →
          </Link>
          <Link href="/sauce-builder" className="bg-white/5 hover:bg-white/10 border border-white/10 text-white font-bold px-6 py-3 rounded-xl transition-colors">
            🍶 Construire son combo
          </Link>
        </div>
      </section>

      {/* Grand Débat teaser */}
      <section className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-6">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="text-lg font-bold">🥊 Le Grand Débat</h2>
            <p className="text-sm text-neutral-500">{total.toLocaleString("fr-FR")} votes — temps réel</p>
          </div>
          <Link href="/le-grand-debat" className="text-sm text-orange-400 hover:text-orange-300 font-semibold">
            Voter →
          </Link>
        </div>
        <div className="space-y-3">
          <div className="flex items-center gap-3">
            <span className="text-sm font-bold text-orange-400 w-32 truncate">Tasty Crousty</span>
            <div className="flex-1 bg-[#2a2a2a] rounded-full h-4 overflow-hidden">
              <div className="h-4 bg-orange-500 rounded-full" style={{ width: `${tcPct}%` }} />
            </div>
            <span className="text-sm font-black text-orange-400 w-10 text-right">{tcPct}%</span>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-sm font-bold text-green-400 w-32 truncate">Krousty Sabaïdi</span>
            <div className="flex-1 bg-[#2a2a2a] rounded-full h-4 overflow-hidden">
              <div className="h-4 bg-green-500 rounded-full" style={{ width: `${ksPct}%` }} />
            </div>
            <span className="text-sm font-black text-green-400 w-10 text-right">{ksPct}%</span>
          </div>
        </div>
      </section>

      {/* Classement national */}
      <section>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-black">🏆 Top 10 national</h2>
          <span className="text-xs text-neutral-500">5 critères : croustillant · poulet · sauce · prix · tenue</span>
        </div>
        <div className="space-y-3">
          {ranked.map((r, i) => {
            const vc = VERDICT_CONFIG[r.verdict];
            return (
              <Link
                key={r.id}
                href={`/restaurants/${r.id}`}
                className="flex items-center gap-4 bg-[#141414] hover:bg-[#1e1e1e] border border-[#2a2a2a] rounded-xl p-4 transition-colors group"
              >
                <span className={`text-2xl font-black w-8 text-center shrink-0 ${i === 0 ? "text-yellow-400" : i === 1 ? "text-neutral-300" : i === 2 ? "text-amber-600" : "text-neutral-600"}`}>
                  {i + 1}
                </span>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 flex-wrap">
                    <span className="font-bold group-hover:text-orange-400 transition-colors">{r.name}</span>
                    <span className={`text-xs px-1.5 py-0.5 rounded border font-bold ${vc.bg} ${vc.color}`}>
                      {vc.emoji} {r.verdict}
                    </span>
                  </div>
                  <div className="flex items-center gap-2 mt-1 flex-wrap">
                    <BrandBadge brand={r.brand} />
                    <span className="text-xs text-neutral-500">{r.city}</span>
                    <span className="text-xs text-neutral-600">· {r.reviewCount} avis</span>
                  </div>
                </div>
                <span className="text-sm font-black text-orange-400 shrink-0">★ {getGlobalScore(r)}</span>
              </Link>
            );
          })}
        </div>
      </section>

      {/* Villes */}
      <section>
        <h2 className="text-2xl font-black mb-4">📍 Par ville</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
          {cities.map((city) => (
            <Link
              key={city}
              href={`/villes/${city.toLowerCase()}`}
              className="bg-[#141414] hover:bg-[#1e1e1e] border border-[#2a2a2a] rounded-xl p-4 text-center font-bold hover:border-orange-500/50 transition-all group"
            >
              <div className="text-2xl mb-1">🏙️</div>
              <div className="group-hover:text-orange-400 transition-colors">{city}</div>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
