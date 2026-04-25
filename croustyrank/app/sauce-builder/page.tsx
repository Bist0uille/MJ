"use client";
import { useState } from "react";
import { SAUCES, combos } from "@/lib/data";

type Sauce = { id: string; label: string; color: string; emoji: string };

export default function SauceBuilderPage() {
  const [selected, setSelected] = useState<Sauce[]>([]);
  const [saved, setSaved] = useState(false);

  function toggleSauce(sauce: Sauce) {
    setSelected((prev) => {
      const exists = prev.find((s) => s.id === sauce.id);
      if (exists) return prev.filter((s) => s.id !== sauce.id);
      if (prev.length >= 3) return prev;
      return [...prev, sauce];
    });
    setSaved(false);
  }

  function saveCombo() {
    setSaved(true);
  }

  const sortedCombos = [...combos].sort((a, b) => b.upvotes - a.upvotes);

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-10">
      <div className="text-center space-y-2">
        <h1 className="text-4xl font-black">🍶 Sauce Combo Builder</h1>
        <p className="text-neutral-400">Construis ton combo idéal et compare avec la communauté</p>
      </div>

      {/* Builder */}
      <section className="bg-[#141414] border border-[#2a2a2a] rounded-2xl p-6 space-y-5">
        <div>
          <h2 className="font-bold mb-1">Choisis tes sauces (max 3)</h2>
          <p className="text-xs text-neutral-500">Sélectionne les sauces que tu commandes</p>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
          {SAUCES.map((sauce) => {
            const isSelected = !!selected.find((s) => s.id === sauce.id);
            const isDisabled = !isSelected && selected.length >= 3;
            return (
              <button
                key={sauce.id}
                onClick={() => toggleSauce(sauce)}
                disabled={isDisabled}
                className={`flex items-center gap-3 p-3 rounded-xl border-2 font-semibold transition-all text-left ${
                  isSelected
                    ? "border-orange-500 bg-orange-500/10 text-white"
                    : isDisabled
                    ? "border-[#2a2a2a] bg-[#1a1a1a] text-neutral-600 cursor-not-allowed"
                    : "border-[#2a2a2a] hover:border-orange-500/50 text-neutral-300 hover:text-white"
                }`}
              >
                <span className="text-2xl">{sauce.emoji}</span>
                <span className="text-sm">{sauce.label}</span>
                {isSelected && <span className="ml-auto text-orange-400">✓</span>}
              </button>
            );
          })}
        </div>

        {/* Preview */}
        <div className="bg-[#1e1e1e] rounded-xl p-4 min-h-16 flex items-center gap-3">
          {selected.length === 0 ? (
            <p className="text-neutral-600 text-sm">Sélectionne tes sauces ci-dessus...</p>
          ) : (
            <div className="flex items-center gap-2 flex-wrap">
              {selected.map((s, i) => (
                <span key={s.id} className="flex items-center gap-1 bg-[#2a2a2a] text-white px-3 py-1.5 rounded-lg text-sm font-medium">
                  {s.emoji} {s.label}
                  {i < selected.length - 1 && <span className="text-neutral-500 ml-1">+</span>}
                </span>
              ))}
            </div>
          )}
        </div>

        <div className="flex gap-3">
          <button
            onClick={saveCombo}
            disabled={selected.length === 0 || saved}
            className={`flex-1 py-3 rounded-xl font-bold transition-all ${
              saved
                ? "bg-green-500/20 text-green-400 border border-green-500/30 cursor-default"
                : selected.length === 0
                ? "bg-[#2a2a2a] text-neutral-600 cursor-not-allowed"
                : "bg-orange-500 hover:bg-orange-400 text-white hover:scale-[1.01]"
            }`}
          >
            {saved ? "✓ Combo sauvegardé !" : "Sauvegarder mon combo"}
          </button>
          <button
            onClick={() => { setSelected([]); setSaved(false); }}
            className="px-4 py-3 rounded-xl border border-[#2a2a2a] text-neutral-500 hover:text-white hover:border-[#3a3a3a] transition-colors font-medium"
          >
            Reset
          </button>
        </div>

        {saved && (
          <div className="text-center space-y-2 pt-2">
            <p className="text-sm text-neutral-400">Partage ton combo !</p>
            <button className="bg-[#1d9bf0]/20 hover:bg-[#1d9bf0]/30 text-[#1d9bf0] border border-[#1d9bf0]/30 font-semibold px-4 py-2 rounded-lg text-sm transition-colors">
              "Mon combo parfait → croustyrank.fr/sauce-builder" 🔥
            </button>
          </div>
        )}
      </section>

      {/* Classement communautaire */}
      <section>
        <h2 className="text-2xl font-black mb-4">🏆 Top combos de la communauté</h2>
        <div className="space-y-3">
          {sortedCombos.map((combo, i) => {
            const score = combo.upvotes - combo.downvotes;
            const total = combo.upvotes + combo.downvotes;
            const ratio = Math.round((combo.upvotes / total) * 100);
            return (
              <div
                key={combo.id}
                className="bg-[#141414] border border-[#2a2a2a] rounded-xl p-4 flex items-center gap-4"
              >
                <span className={`text-xl font-black w-8 text-center ${i === 0 ? "text-yellow-400" : i === 1 ? "text-neutral-300" : i === 2 ? "text-amber-600" : "text-neutral-600"}`}>
                  {i + 1}
                </span>
                <div className="flex-1">
                  <div className="font-bold">{combo.label}</div>
                  <div className="flex gap-1 mt-1">
                    {combo.sauces.map((s, j) => {
                      const sauce = SAUCES.find((sauce) => sauce.label === s) ?? SAUCES[0];
                      return (
                        <span key={j} className="text-xs bg-[#2a2a2a] text-neutral-400 px-2 py-0.5 rounded">
                          {sauce?.emoji} {s}
                        </span>
                      );
                    })}
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-orange-400 font-black">+{score.toLocaleString("fr-FR")}</div>
                  <div className="text-xs text-neutral-600">{ratio}% approuvent</div>
                </div>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}
