"use client";
import { useState } from "react";
import { grandDebatVotes } from "@/lib/data";
import Link from "next/link";

const ARGS_TC = [
  "Conçu par un expert du marketing digital — le produit parfait pour TikTok",
  "40+ restaurants en France en moins de 2 ans",
  "Interface épurée, service rapide, format dark kitchen disponible",
  "La nouvelle génération l'a adopté massivement",
  "+323% sur UberEats en 12 mois",
];

const ARGS_KS = [
  "L'ORIGINAL depuis 2012 à Bordeaux — Tasty Crousty a copié la recette",
  "La sauce curry-soja est introuvable chez les concurrents",
  "Portions encore plus généreuses selon les avis",
  "34 restaurants gérés par des passionnés, pas par une agence d'influence",
  "Note communautaire moyenne supérieure sur notre classement",
];

export default function GrandDebatPage() {
  const [votes, setVotes] = useState(grandDebatVotes);
  const [voted, setVoted] = useState<null | "tc" | "ks">(null);

  const total = votes.tastyCrousty + votes.kroustySabaidi;
  const tcPct = Math.round((votes.tastyCrousty / total) * 100);
  const ksPct = 100 - tcPct;

  function vote(team: "tc" | "ks") {
    if (voted) return;
    setVoted(team);
    setVotes((v) => ({
      tastyCrousty: team === "tc" ? v.tastyCrousty + 1 : v.tastyCrousty,
      kroustySabaidi: team === "ks" ? v.kroustySabaidi + 1 : v.kroustySabaidi,
    }));
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-10">
      <div className="text-center space-y-3">
        <div className="inline-block bg-red-500/10 border border-red-500/20 text-red-400 text-xs font-bold px-3 py-1 rounded-full">
          🔴 LIVE — {total.toLocaleString("fr-FR")} votes
        </div>
        <h1 className="text-4xl md:text-6xl font-black">
          🥊 Le Grand Débat
        </h1>
        <p className="text-neutral-400 text-lg">
          L&apos;original vs le viral. Qui fait vraiment le meilleur crousty ?
        </p>
      </div>

      {/* Barre de résultats */}
      <div className="relative h-12 flex rounded-xl overflow-hidden border border-[#2a2a2a]">
        <div
          className="bg-orange-500 flex items-center justify-start pl-4 font-black text-white text-lg transition-all duration-500"
          style={{ width: `${tcPct}%` }}
        >
          {tcPct > 20 && `${tcPct}%`}
        </div>
        <div
          className="bg-green-500 flex items-center justify-end pr-4 font-black text-white text-lg transition-all duration-500 flex-1"
        >
          {ksPct > 20 && `${ksPct}%`}
        </div>
      </div>

      {/* Les deux camps */}
      <div className="grid md:grid-cols-2 gap-6">
        {/* Tasty Crousty */}
        <div className={`bg-[#141414] border-2 rounded-2xl p-6 space-y-4 transition-all ${voted === "tc" ? "border-orange-500 shadow-lg shadow-orange-500/20" : "border-[#2a2a2a]"}`}>
          <div className="text-center">
            <div className="text-5xl mb-2">🔥</div>
            <h2 className="text-2xl font-black text-orange-500">Tasty Crousty</h2>
            <p className="text-neutral-500 text-sm">Le viral · 40+ restos</p>
            <div className="text-4xl font-black text-orange-400 mt-2">{tcPct}%</div>
            <p className="text-xs text-neutral-600">{votes.tastyCrousty.toLocaleString("fr-FR")} votes</p>
          </div>
          <ul className="space-y-2">
            {ARGS_TC.map((a, i) => (
              <li key={i} className="flex gap-2 text-sm text-neutral-300">
                <span className="text-orange-500 mt-0.5 shrink-0">✓</span>
                {a}
              </li>
            ))}
          </ul>
          <button
            onClick={() => vote("tc")}
            disabled={!!voted}
            className={`w-full py-3 rounded-xl font-black text-lg transition-all ${
              voted === "tc"
                ? "bg-orange-500 text-white cursor-default"
                : voted
                ? "bg-[#2a2a2a] text-neutral-600 cursor-not-allowed"
                : "bg-orange-500 hover:bg-orange-400 text-white hover:scale-[1.02]"
            }`}
          >
            {voted === "tc" ? "✓ Voté !" : "Voter Tasty Crousty"}
          </button>
        </div>

        {/* Krousty Sabaïdi */}
        <div className={`bg-[#141414] border-2 rounded-2xl p-6 space-y-4 transition-all ${voted === "ks" ? "border-green-500 shadow-lg shadow-green-500/20" : "border-[#2a2a2a]"}`}>
          <div className="text-center">
            <div className="text-5xl mb-2">🌿</div>
            <h2 className="text-2xl font-black text-green-400">Krousty Sabaïdi</h2>
            <p className="text-neutral-500 text-sm">L&apos;original · depuis 2012</p>
            <div className="text-4xl font-black text-green-400 mt-2">{ksPct}%</div>
            <p className="text-xs text-neutral-600">{votes.kroustySabaidi.toLocaleString("fr-FR")} votes</p>
          </div>
          <ul className="space-y-2">
            {ARGS_KS.map((a, i) => (
              <li key={i} className="flex gap-2 text-sm text-neutral-300">
                <span className="text-green-500 mt-0.5 shrink-0">✓</span>
                {a}
              </li>
            ))}
          </ul>
          <button
            onClick={() => vote("ks")}
            disabled={!!voted}
            className={`w-full py-3 rounded-xl font-black text-lg transition-all ${
              voted === "ks"
                ? "bg-green-500 text-white cursor-default"
                : voted
                ? "bg-[#2a2a2a] text-neutral-600 cursor-not-allowed"
                : "bg-green-500 hover:bg-green-400 text-white hover:scale-[1.02]"
            }`}
          >
            {voted === "ks" ? "✓ Voté !" : "Voter Krousty Sabaïdi"}
          </button>
        </div>
      </div>

      {voted && (
        <div className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5 text-center space-y-3">
          <p className="font-bold text-lg">Vote enregistré ! 🎉</p>
          <p className="text-neutral-400 text-sm">Partage le débat pour faire gagner ton camp</p>
          <div className="flex gap-3 justify-center">
            <button className="bg-[#1d9bf0]/20 hover:bg-[#1d9bf0]/30 text-[#1d9bf0] border border-[#1d9bf0]/30 font-semibold px-4 py-2 rounded-lg text-sm transition-colors">
              Partager sur X →
            </button>
            <Link href="/" className="bg-white/5 hover:bg-white/10 border border-white/10 text-white font-semibold px-4 py-2 rounded-lg text-sm transition-colors">
              Voir le classement
            </Link>
          </div>
        </div>
      )}
    </div>
  );
}
