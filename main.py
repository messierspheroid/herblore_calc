import pandas as pd
import requests

url = "https://runescape.wiki/w/Potions"
header = {
    "Request Line": "GET / HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

r = requests.get(url, headers=header)

dfs = pd.read_html(r.text)

regular_potions = dfs[2]
regular_potions_name = regular_potions["Potion"]
regular_potions_level = regular_potions["Level"]
regular_potions_xp = regular_potions["XP"]
regular_potions_effect = regular_potions["Effect"]
regular_potions_primary = regular_potions["Primary"]
regular_potions_secondary = regular_potions["Secondary"]

barbarian_potions = dfs[3]
combination_potions = dfs[4]
dungeoneering_weak_potions = dfs[6]
dungeoneering_medium_potions = dfs[7]
dungeoneering_strong_potions = dfs[8]

print()


