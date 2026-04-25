"use client";
import { Restaurant, VERDICT_CONFIG } from "@/lib/data";
import { RadarChart, Radar, PolarGrid, PolarAngleAxis, ResponsiveContainer } from "recharts";
import { useState } from "react";

const CATEGORIES = [
  { key: "croustillant", label: "Croustillant" },
  { key: "poulet",       label: "Poulet" },
  { key: "sauce",        label: "Sauce" },
  { key: "prix_plaisir", label: "Prix/Plaisir" },
  { key: "tenue",        label: "Tenue" },
];

const MOCK_REVIEWS = [
  { text: "Le panage tient encore après 10 min, c'est rare. Sauce curry de folie.", stars: 5, date: "il y a 2j" },
  { text: "Portion généreuse mais le poulet était un peu sec ce soir-là.", stars: 3, date: "il y a 5j" },
  { text: "9€ justifiés. La tenue est impeccable, rien ne dégouline.", stars: 5, date: "il y a 1sem" },
  { text: "La pimentée arrache vraiment. Addictif mais attention à la tenue.", stars: 4, date: "il y a 2sem" },
];

export default function RestaurantClient({ restaurant: r }: { restaurant: Restaurant }) {
  const [userRating, setUserRating] = useState<number | null>(null);
  const vc = VERDICT_CONFIG[r.verdict];

  const data = CATEGORIES.map((c) => ({
    subject: c.label,
    value: r.ratings[c.key as keyof typeof r.ratings],
    fullMark: 5,
  }));

  return (
    <div className="space-y-6">
      {/* Verdict */}
      <section className={`border rounded-2xl p-5 ${vc.bg}`}>
        <div className="flex items-start gap-3">
          <span className="text-3xl">{vc.emoji}</span>
          <div>
            <div className={`font-black text-lg ${vc.color}`}>
              {r.verdict}
            </div>
            <p className="text-sm text-neutral-300 mt-1 leading-relaxed">{r.verdictText}</p>
          </div>
        </div>
      </section>

      {/* Radar chart */}
      <section className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5">
        <h2 className="font-bold mb-4">📊 Profil détaillé</h2>
        <div className="h-56">
          <ResponsiveContainer width="100%" height="100%">
            <RadarChart data={data}>
              <PolarGrid stroke="#2a2a2a" />
              <PolarAngleAxis dataKey="subject" tick={{ fill: "#737373", fontSize: 12 }} />
              <Radar
                name={r.name}
                dataKey="value"
                stroke="#f97316"
                fill="#f97316"
                fillOpacity={0.25}
                strokeWidth={2}
              />
            </RadarChart>
          </ResponsiveContainer>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 mt-2">
          {CATEGORIES.map((c) => {
            const val = r.ratings[c.key as keyof typeof r.ratings];
            return (
              <div key={c.key} className="flex items-center justify-between bg-[#1e1e1e] rounded-lg px-3 py-2">
                <span className="text-xs text-neutral-500">{c.label}</span>
                <span className={`text-sm font-bold ${val >= 4.5 ? "text-green-400" : val >= 3.5 ? "text-orange-400" : "text-red-400"}`}>
                  {val.toFixed(1)}
                </span>
              </div>
            );
          })}
        </div>
      </section>

      {/* Note rapide */}
      <section className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5">
        <h2 className="font-bold mb-3">⭐ Donne ton avis</h2>
        <div className="flex gap-2">
          {[1, 2, 3, 4, 5].map((star) => (
            <button
              key={star}
              onClick={() => setUserRating(star)}
              className={`text-3xl transition-transform hover:scale-110 ${
                userRating !== null && star <= userRating ? "text-orange-400" : "text-neutral-700"
              }`}
            >
              ★
            </button>
          ))}
        </div>
        {userRating && (
          <p className="text-sm text-green-400 mt-2 font-medium">Merci ! Ton vote a été pris en compte. 🙏</p>
        )}
      </section>

      {/* Avis */}
      <section className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-5">
        <h2 className="font-bold mb-4">💬 Avis de la communauté</h2>
        <div className="space-y-4">
          {MOCK_REVIEWS.map((rev, i) => (
            <div key={i} className="border-b border-[#2a2a2a] last:border-0 pb-4 last:pb-0">
              <div className="flex items-center gap-2 mb-1">
                <span className="text-orange-400 text-sm">{"★".repeat(rev.stars)}{"☆".repeat(5 - rev.stars)}</span>
                <span className="text-xs text-neutral-600">{rev.date}</span>
              </div>
              <p className="text-sm text-neutral-300">{rev.text}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
