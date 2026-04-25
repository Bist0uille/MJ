"use client";
import { useState } from "react";
import { fauxCroustys } from "@/lib/data";

type Verdict = "Authentique" | "Passable" | "Arnaque" | "all";

const VERDICT_STYLES = {
  Authentique: "bg-green-500/20 text-green-400 border border-green-500/30",
  Passable: "bg-yellow-500/20 text-yellow-400 border border-yellow-500/30",
  Arnaque: "bg-red-500/20 text-red-400 border border-red-500/30",
};

const VERDICT_EMOJI = {
  Authentique: "✅",
  Passable: "⚠️",
  Arnaque: "🚨",
};

export default function FauxCroustyPage() {
  const [filter, setFilter] = useState<Verdict>("all");
  const [reporting, setReporting] = useState(false);
  const [reported, setReported] = useState(false);

  const filtered = filter === "all"
    ? fauxCroustys
    : fauxCroustys.filter((f) => f.verdict === filter);

  const sorted = [...filtered].sort((a, b) => b.score - a.score);

  const counts = {
    Authentique: fauxCroustys.filter((f) => f.verdict === "Authentique").length,
    Passable: fauxCroustys.filter((f) => f.verdict === "Passable").length,
    Arnaque: fauxCroustys.filter((f) => f.verdict === "Arnaque").length,
  };

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-8">
      <div className="text-center space-y-2">
        <h1 className="text-4xl font-black">🚨 Faux Crousty Detector</h1>
        <p className="text-neutral-400 max-w-xl mx-auto">
          Les kebabs ont tous ajouté un &quot;crousty&quot; au menu. Lequel est vraiment digne ?
          La communauté a testé pour toi.
        </p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-3 gap-3">
        {(["Authentique", "Passable", "Arnaque"] as const).map((v) => (
          <div key={v} className={`rounded-2xl p-4 text-center border ${VERDICT_STYLES[v]}`}>
            <div className="text-3xl mb-1">{VERDICT_EMOJI[v]}</div>
            <div className="text-2xl font-black">{counts[v]}</div>
            <div className="text-xs opacity-80">{v}</div>
          </div>
        ))}
      </div>

      {/* Filtres */}
      <div className="flex gap-2 flex-wrap">
        {(["all", "Authentique", "Passable", "Arnaque"] as const).map((v) => (
          <button
            key={v}
            onClick={() => setFilter(v)}
            className={`px-4 py-2 rounded-xl text-sm font-semibold border transition-all ${
              filter === v
                ? "bg-orange-500 text-white border-orange-500"
                : "bg-[#141414] text-neutral-400 border-[#2a2a2a] hover:border-orange-500/50 hover:text-white"
            }`}
          >
            {v === "all" ? "Tous" : `${VERDICT_EMOJI[v]} ${v}`}
          </button>
        ))}
      </div>

      {/* Liste */}
      <div className="space-y-3">
        {sorted.map((faux) => (
          <div
            key={faux.id}
            className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-4 flex items-center gap-4"
          >
            <div className="text-3xl">{VERDICT_EMOJI[faux.verdict]}</div>
            <div className="flex-1 min-w-0">
              <div className="font-bold">{faux.name}</div>
              <div className="text-sm text-neutral-500">{faux.city} · {faux.reviews} avis</div>
            </div>
            <div className="text-right shrink-0">
              <span className={`px-2 py-0.5 rounded text-xs font-bold border ${VERDICT_STYLES[faux.verdict]}`}>
                {faux.verdict}
              </span>
              <div className="text-sm font-black text-orange-400 mt-1">★ {faux.score.toFixed(1)}</div>
            </div>
          </div>
        ))}
      </div>

      {/* Signaler un faux crousty */}
      {!reporting && !reported && (
        <div className="bg-[#141414] border border-dashed border-[#3a3a3a] rounded-2xl p-5 text-center space-y-3">
          <p className="font-bold">Tu as testé un crousty de kebab douteux ?</p>
          <p className="text-sm text-neutral-500">Aide la communauté à éviter les arnaques</p>
          <button
            onClick={() => setReporting(true)}
            className="bg-red-500/20 hover:bg-red-500/30 border border-red-500/30 text-red-400 font-bold px-5 py-2.5 rounded-xl transition-colors"
          >
            🚨 Signaler un Faux Crousty
          </button>
        </div>
      )}

      {reporting && !reported && (
        <div className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5 space-y-4">
          <h2 className="font-bold">Signaler un établissement</h2>
          <div className="space-y-3">
            <input
              type="text"
              placeholder="Nom du restaurant"
              className="w-full bg-[#1e1e1e] border border-[#2a2a2a] rounded-xl px-3 py-2 text-sm outline-none focus:border-orange-500/50 transition-colors"
            />
            <input
              type="text"
              placeholder="Ville"
              className="w-full bg-[#1e1e1e] border border-[#2a2a2a] rounded-xl px-3 py-2 text-sm outline-none focus:border-orange-500/50 transition-colors"
            />
            <div className="flex gap-2">
              {(["Authentique", "Passable", "Arnaque"] as const).map((v) => (
                <button key={v} className={`flex-1 py-2 rounded-xl text-xs font-bold border ${VERDICT_STYLES[v]} hover:opacity-80 transition-opacity`}>
                  {VERDICT_EMOJI[v]} {v}
                </button>
              ))}
            </div>
            <textarea
              placeholder="Décris ton expérience..."
              rows={3}
              className="w-full bg-[#1e1e1e] border border-[#2a2a2a] rounded-xl px-3 py-2 text-sm outline-none focus:border-orange-500/50 transition-colors resize-none"
            />
          </div>
          <div className="flex gap-2">
            <button
              onClick={() => { setReported(true); setReporting(false); }}
              className="flex-1 bg-orange-500 hover:bg-orange-400 text-white font-bold py-2.5 rounded-xl transition-colors"
            >
              Envoyer le signalement
            </button>
            <button
              onClick={() => setReporting(false)}
              className="px-4 py-2.5 border border-[#2a2a2a] text-neutral-500 hover:text-white rounded-xl transition-colors"
            >
              Annuler
            </button>
          </div>
        </div>
      )}

      {reported && (
        <div className="bg-green-500/10 border border-green-500/20 rounded-2xl p-5 text-center space-y-2">
          <div className="text-3xl">✅</div>
          <p className="font-bold text-green-400">Signalement reçu !</p>
          <p className="text-sm text-neutral-500">Il sera vérifié par la communauté avant publication.</p>
        </div>
      )}
    </div>
  );
}
