export type Brand = "Tasty Crousty" | "Krousty Sabaïdi" | "Kebab";
export type Verdict = "Validé" | "Surcoté" | "Arnaque";

export type Restaurant = {
  id: string;
  name: string;
  brand: Brand;
  city: string;
  address: string;
  isPremium: boolean;
  verdict: Verdict;
  verdictText: string;
  ratings: {
    croustillant: number;
    poulet: number;
    sauce: number;
    prix_plaisir: number;
    tenue: number;
  };
  reviewCount: number;
  uberEatsUrl?: string;
  sauces: string[];
};

export type Opening = {
  id: string;
  city: string;
  brand: Brand;
  openingDate: string;
  confirmed: boolean;
  address?: string;
};

export type Combo = {
  id: string;
  label: string;
  sauces: string[];
  upvotes: number;
  downvotes: number;
};

export type FauxCrousty = {
  id: string;
  name: string;
  city: string;
  verdict: "Authentique" | "Passable" | "Arnaque";
  score: number;
  reviews: number;
};

export const SAUCES = [
  { id: "blanche", label: "Blanche", color: "#f5f5f0", emoji: "🤍" },
  { id: "pimentee", label: "Pimentée", color: "#ef4444", emoji: "🔥" },
  { id: "curry", label: "Curry", color: "#f59e0b", emoji: "🟡" },
  { id: "sucree-pimentee", label: "Sucrée-Pimentée", color: "#f97316", emoji: "🧡" },
  { id: "soja", label: "Soja", color: "#854d0e", emoji: "🤎" },
];

export const restaurants: Restaurant[] = [
  {
    id: "ks-bordeaux",
    name: "Krousty Sabaïdi Bordeaux",
    brand: "Krousty Sabaïdi",
    city: "Bordeaux",
    address: "14 Rue Sainte-Catherine, 33000",
    isPremium: true,
    verdict: "Validé",
    verdictText: "L'original depuis 2012. La sauce curry-soja n'existe nulle part ailleurs. Le panage tient encore 10 minutes après. Référence absolue.",
    ratings: { croustillant: 4.9, poulet: 4.8, sauce: 4.9, prix_plaisir: 4.8, tenue: 4.7 },
    reviewCount: 2187,
    sauces: ["Blanche", "Curry", "Soja", "Pimentée"],
  },
  {
    id: "ks-paris",
    name: "Krousty Sabaïdi Paris",
    brand: "Krousty Sabaïdi",
    city: "Paris",
    address: "45 Rue de la Roquette, 75011",
    isPremium: false,
    verdict: "Validé",
    verdictText: "Le niveau tient comparé à Bordeaux. La sauce soja fait la différence. Légèrement moins généreux en portion mais ça reste incontestable.",
    ratings: { croustillant: 4.6, poulet: 4.7, sauce: 4.8, prix_plaisir: 4.6, tenue: 4.5 },
    reviewCount: 1563,
    sauces: ["Blanche", "Curry", "Soja"],
  },
  {
    id: "tc-lyon",
    name: "Tasty Crousty Lyon",
    brand: "Tasty Crousty",
    city: "Lyon",
    address: "92 Boulevard des États-Unis, 69008",
    isPremium: true,
    verdict: "Validé",
    verdictText: "Le meilleur Tasty Crousty du réseau. Portion honnête, panage qui croque, service rapide.",
    ratings: { croustillant: 4.6, poulet: 4.5, sauce: 4.6, prix_plaisir: 4.7, tenue: 4.4 },
    reviewCount: 654,
    sauces: ["Blanche", "Pimentée", "Curry", "Sucrée-Pimentée"],
  },
  {
    id: "ks-toulouse",
    name: "Krousty Sabaïdi Toulouse",
    brand: "Krousty Sabaïdi",
    city: "Toulouse",
    address: "3 Rue de la Pomme, 31000",
    isPremium: false,
    verdict: "Validé",
    verdictText: "Solide. Le poulet est de qualité, le croustillant tient. Pas aussi marquant que Bordeaux mais très au-dessus de la concurrence locale.",
    ratings: { croustillant: 4.5, poulet: 4.6, sauce: 4.7, prix_plaisir: 4.7, tenue: 4.3 },
    reviewCount: 789,
    sauces: ["Blanche", "Pimentée", "Curry"],
  },
  {
    id: "tc-marseille",
    name: "Tasty Crousty Marseille",
    brand: "Tasty Crousty",
    city: "Marseille",
    address: "5 Boulevard Garibaldi, 13001",
    isPremium: false,
    verdict: "Validé",
    verdictText: "Bonne surprise. La pimentée arrache vraiment. Portion généreuse pour Marseille.",
    ratings: { croustillant: 4.4, poulet: 4.3, sauce: 4.5, prix_plaisir: 4.9, tenue: 4.1 },
    reviewCount: 432,
    sauces: ["Blanche", "Pimentée"],
  },
  {
    id: "tc-paris-11",
    name: "Tasty Crousty Paris 11e",
    brand: "Tasty Crousty",
    city: "Paris",
    address: "26 Rue du Faubourg du Temple, 75011",
    isPremium: true,
    verdict: "Surcoté",
    verdictText: "La hype TikTok a tout faussi. File d'attente de 40 min pour un crousty qui ramollit pendant que tu attends.",
    ratings: { croustillant: 3.8, poulet: 4.1, sauce: 4.3, prix_plaisir: 3.5, tenue: 3.2 },
    reviewCount: 1243,
    uberEatsUrl: "#",
    sauces: ["Blanche", "Pimentée", "Curry"],
  },
  {
    id: "tc-paris-18",
    name: "Tasty Crousty Paris 18e",
    brand: "Tasty Crousty",
    city: "Paris",
    address: "28 Avenue de Saint-Ouen, 75018",
    isPremium: false,
    verdict: "Surcoté",
    verdictText: "Inconsistant. Parfois excellent, souvent décevant. Le panage colle au riz à mi-chemin.",
    ratings: { croustillant: 3.5, poulet: 3.9, sauce: 4.0, prix_plaisir: 3.6, tenue: 3.0 },
    reviewCount: 876,
    sauces: ["Blanche", "Pimentée", "Sucrée-Pimentée"],
  },
  {
    id: "tc-nantes",
    name: "Tasty Crousty Nantes",
    brand: "Tasty Crousty",
    city: "Nantes",
    address: "12 Rue du Calvaire, 44000",
    isPremium: false,
    verdict: "Validé",
    verdictText: "Crousty honnête, pas de chichi. Le staff fait attention à la tenue du plat.",
    ratings: { croustillant: 4.3, poulet: 4.2, sauce: 4.1, prix_plaisir: 4.5, tenue: 4.2 },
    reviewCount: 298,
    sauces: ["Blanche", "Pimentée", "Sucrée-Pimentée"],
  },
  {
    id: "tc-grenoble",
    name: "Tasty Crousty Grenoble",
    brand: "Tasty Crousty",
    city: "Grenoble",
    address: "50 Avenue du 8 mai 1945, 38130",
    isPremium: false,
    verdict: "Surcoté",
    verdictText: "Correct mais pas à la hauteur de la réputation locale. Panage mou, poulet trop fin.",
    ratings: { croustillant: 3.4, poulet: 3.8, sauce: 4.0, prix_plaisir: 4.0, tenue: 3.5 },
    reviewCount: 321,
    sauces: ["Blanche", "Pimentée"],
  },
  {
    id: "tc-orleans",
    name: "Tasty Crousty Orléans",
    brand: "Tasty Crousty",
    city: "Orléans",
    address: "6 Place du Général de Gaulle, 45000",
    isPremium: false,
    verdict: "Arnaque",
    verdictText: "Le crousty arrive humide. Le poulet sent le réchauffé. À 9€ on s'attendait à mieux qu'une boîte molle.",
    ratings: { croustillant: 2.1, poulet: 2.8, sauce: 3.5, prix_plaisir: 2.5, tenue: 1.9 },
    reviewCount: 187,
    sauces: ["Blanche", "Pimentée"],
  },
];

export const openings: Opening[] = [
  { id: "o1", city: "Lille", brand: "Tasty Crousty", openingDate: "2026-05-10", confirmed: true, address: "Rue Nationale" },
  { id: "o2", city: "Strasbourg", brand: "Tasty Crousty", openingDate: "2026-05-24", confirmed: true },
  { id: "o3", city: "Rennes", brand: "Krousty Sabaïdi", openingDate: "2026-06-07", confirmed: false },
  { id: "o4", city: "Nice", brand: "Tasty Crousty", openingDate: "2026-06-14", confirmed: true },
  { id: "o5", city: "Montpellier", brand: "Tasty Crousty", openingDate: "2026-07-01", confirmed: false },
  { id: "o6", city: "Dijon", brand: "Krousty Sabaïdi", openingDate: "2026-07-15", confirmed: false },
];

export const combos: Combo[] = [
  { id: "c1", label: "Double Blanche", sauces: ["Blanche", "Blanche"], upvotes: 3421, downvotes: 412 },
  { id: "c2", label: "Le Classique", sauces: ["Blanche", "Pimentée"], upvotes: 2876, downvotes: 543 },
  { id: "c3", label: "Le Fou", sauces: ["Pimentée", "Pimentée"], upvotes: 1654, downvotes: 1203 },
  { id: "c4", label: "L'Asiatique", sauces: ["Curry", "Soja"], upvotes: 1432, downvotes: 287 },
  { id: "c5", label: "Le Doux", sauces: ["Blanche", "Sucrée-Pimentée"], upvotes: 987, downvotes: 156 },
];

export const fauxCroustys: FauxCrousty[] = [
  { id: "f1", name: "Snack Al Baraka", city: "Paris 19e", verdict: "Authentique", score: 4.2, reviews: 234 },
  { id: "f2", name: "Quick Kebab Express", city: "Lyon", verdict: "Passable", score: 2.8, reviews: 87 },
  { id: "f3", name: "Le Sultan", city: "Marseille", verdict: "Arnaque", score: 1.4, reviews: 156 },
  { id: "f4", name: "Chez Mehdi", city: "Bordeaux", verdict: "Authentique", score: 4.6, reviews: 312 },
  { id: "f5", name: "Fast Food du Coin", city: "Toulouse", verdict: "Arnaque", score: 1.1, reviews: 203 },
];

export const grandDebatVotes = { tastyCrousty: 47823, kroustySabaidi: 38941 };

export function getGlobalScore(r: Restaurant) {
  const { croustillant, poulet, sauce, prix_plaisir, tenue } = r.ratings;
  return ((croustillant + poulet + sauce + prix_plaisir + tenue) / 5).toFixed(1);
}

export function getRankedRestaurants() {
  return [...restaurants].sort((a, b) => parseFloat(getGlobalScore(b)) - parseFloat(getGlobalScore(a)));
}

export function getCities() {
  return [...new Set(restaurants.map((r) => r.city))].sort();
}

export function getRestaurantsByCity(city: string) {
  return restaurants.filter((r) => r.city.toLowerCase() === city.toLowerCase());
}

export function getRestaurantById(id: string) {
  return restaurants.find((r) => r.id === id);
}

export const VERDICT_CONFIG = {
  "Validé":  { emoji: "✅", color: "text-green-400",  bg: "bg-green-500/15 border-green-500/30" },
  "Surcoté": { emoji: "⚠️", color: "text-yellow-400", bg: "bg-yellow-500/15 border-yellow-500/30" },
  "Arnaque": { emoji: "🚨", color: "text-red-400",    bg: "bg-red-500/15 border-red-500/30" },
};
