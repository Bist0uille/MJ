import { openings } from "@/lib/data";

function daysUntil(dateStr: string) {
  const target = new Date(dateStr);
  const now = new Date("2026-04-25");
  const diff = Math.ceil((target.getTime() - now.getTime()) / (1000 * 60 * 60 * 24));
  return diff;
}

function formatDate(dateStr: string) {
  return new Date(dateStr).toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric" });
}

export default function OuverturesPage() {
  const sorted = [...openings].sort(
    (a, b) => new Date(a.openingDate).getTime() - new Date(b.openingDate).getTime()
  );

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-8">
      <div className="text-center space-y-2">
        <div className="inline-block bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-bold px-3 py-1 rounded-full">
          {openings.length} ouvertures annoncées
        </div>
        <h1 className="text-4xl font-black">📍 Opening Tracker</h1>
        <p className="text-neutral-400">
          Sois le premier à savoir. Les vidéos d&apos;ouverture font 2M+ vues sur TikTok.
        </p>
      </div>

      {/* CTA alerte */}
      <div className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5 flex flex-col sm:flex-row gap-3 items-center">
        <div className="flex-1">
          <h2 className="font-bold">Reçois les alertes d&apos;ouverture</h2>
          <p className="text-sm text-neutral-500">Sois notifié avant l&apos;annonce officielle sur TikTok</p>
        </div>
        <div className="flex gap-2 w-full sm:w-auto">
          <input
            type="email"
            placeholder="ton@email.fr"
            className="bg-[#1e1e1e] border border-[#2a2a2a] rounded-xl px-3 py-2 text-sm flex-1 sm:w-48 outline-none focus:border-orange-500/50 transition-colors"
          />
          <button className="bg-orange-500 hover:bg-orange-400 text-white font-bold px-4 py-2 rounded-xl text-sm transition-colors whitespace-nowrap">
            M&apos;alerter
          </button>
        </div>
      </div>

      {/* Timeline */}
      <div className="space-y-4">
        {sorted.map((opening) => {
          const days = daysUntil(opening.openingDate);
          const brandColor = opening.brand === "Tasty Crousty" ? "orange" : "green";
          const brandTextColor = brandColor === "orange" ? "text-orange-400" : "text-green-400";
          const brandBgColor = brandColor === "orange" ? "bg-orange-500/20 border-orange-500/30" : "bg-green-500/20 border-green-500/30";

          return (
            <div
              key={opening.id}
              className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5 flex gap-4 items-start"
            >
              <div className={`shrink-0 w-16 h-16 rounded-xl ${brandBgColor} border flex flex-col items-center justify-center`}>
                <span className={`text-xl font-black ${brandTextColor}`}>{days}</span>
                <span className="text-xs text-neutral-500">jours</span>
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 flex-wrap">
                  <h2 className="font-black text-lg">{opening.city}</h2>
                  <span
                    className={`px-2 py-0.5 rounded text-xs font-bold border ${
                      opening.brand === "Tasty Crousty"
                        ? "bg-orange-500/20 text-orange-400 border-orange-500/30"
                        : "bg-green-500/20 text-green-400 border-green-500/30"
                    }`}
                  >
                    {opening.brand}
                  </span>
                  {opening.confirmed ? (
                    <span className="text-xs bg-green-500/10 text-green-400 border border-green-500/20 px-2 py-0.5 rounded">✓ Confirmé</span>
                  ) : (
                    <span className="text-xs bg-yellow-500/10 text-yellow-400 border border-yellow-500/20 px-2 py-0.5 rounded">⚠ Rumeur</span>
                  )}
                </div>
                <p className="text-sm text-neutral-500 mt-0.5">{formatDate(opening.openingDate)}</p>
                {opening.address && (
                  <p className="text-xs text-neutral-600 mt-1">{opening.address}</p>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Signaler */}
      <div className="bg-[#141414] border border-dashed border-[#3a3a3a] rounded-2xl p-5 text-center space-y-3">
        <p className="font-bold">Tu as une info sur une prochaine ouverture ?</p>
        <p className="text-sm text-neutral-500">Aide la communauté à anticiper</p>
        <button className="bg-white/5 hover:bg-white/10 border border-white/10 text-white font-bold px-5 py-2.5 rounded-xl transition-colors">
          Signaler une ouverture
        </button>
      </div>
    </div>
  );
}
