# islet-food-data

Food packs for the Islet app (a personal diabetes app). Islet downloads `packs/manifest.json` about once a week on
Wi-Fi and fetches any pack whose version went up. Each pack is checked against its SHA-256 before it replaces the copy
on the phone, so a broken download changes nothing. Islet works offline with the packs it already has.

| Pack | What it holds | Source |
| --- | --- | --- |
| `common_uk.tsv` | Everyday UK foods with typical small / average / large portions (grams). Carbs come from CoFID codes in the app. | Portion weights are estimates; CoFID (McCance and Widdowson's, Open Government Licence) for nutrients |
| `fastfood_<country>.tsv` | Chain items: weight per item (if given), carbs and sugars per item. UK: Greggs (guide, Oct 2026), McDonald's (mcdonalds.com/gb, Nov 2026), KFC (kfc.co.uk, Nov 2026) | Each chain's own published nutrition information (date in the `checked` column) |
| `fastfood_pizzahut_uk.tsv` | Pizza Hut Delivery: whole pizzas and one serving (half, third, quarter), sides, chicken, dips, desserts; carbs per item (no weights given) | Pizza Hut nutrition and allergen booklet, valid from July 2026 (read 8 Nov 2026) |
| `fastfood_pret_uk.tsv` | Pret: food and drinks, per serving with the average weight | pret.co.uk menu pages (8 Nov 2026); the app also reads them monthly |
| `fastfood_starbucks_uk.tsv` | Starbucks: food per item, drinks per size (Short, Tall, Grande, Venti) with standard milk | starbucks.co.uk product pages (8 Nov 2026) |
| `fastfood_costa_uk.tsv` | Costa: drinks per cup (in store and take-out) and food per portion with its weight | costa.co.uk menu pages (8 Nov 2026) |
| `off_<country>.tsv` (planned) | Packaged products sold in one country, for offline barcode and search | Open Food Facts (ODbL) |

To publish a change: edit or add packs in `packs/`, then run
`python tools/make_food_manifest.py packs https://raw.githubusercontent.com/D0M1C0/islet-food-data/main/packs`
and commit. A pack's version goes up automatically when its content changes.

The figures are a help for carb counting, not a guarantee: chains change recipes, and portion weights vary.
Check anything you eat often against the pack or the chain's current figures.
