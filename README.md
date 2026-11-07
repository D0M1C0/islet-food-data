# islet-food-data

Food packs for the Islet app (a personal diabetes app). Islet downloads `packs/manifest.json` about once a week on
Wi-Fi and fetches any pack whose version went up. Each pack is checked against its SHA-256 before it replaces the copy
on the phone, so a broken download changes nothing. Islet works offline with the packs it already has.

| Pack | What it holds | Source |
| --- | --- | --- |
| `common_uk.tsv` | Everyday UK foods with typical small / average / large portions (grams). Carbs come from CoFID codes in the app. | Portion weights are estimates; CoFID (McCance and Widdowson's, Open Government Licence) for nutrients |
| `fastfood_<country>.tsv` | Chain items: weight per item (if given), carbs and sugars per item | Each chain's own published nutrition information (date in the `checked` column) |
| `off_<country>.tsv` (planned) | Packaged products sold in one country, for offline barcode and search | Open Food Facts (ODbL) |

To publish a change: edit or add packs in `packs/`, then run
`python tools/make_food_manifest.py packs https://raw.githubusercontent.com/D0M1C0/islet-food-data/main/packs`
and commit. A pack's version goes up automatically when its content changes.

The figures are a help for carb counting, not a guarantee: chains change recipes, and portion weights vary.
Check anything you eat often against the pack or the chain's current figures.
