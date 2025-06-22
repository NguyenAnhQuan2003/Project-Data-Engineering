import json
from bs4 import BeautifulSoup
from tqdm import tqdm

INPUT_FILE = "project2.json"
OUTPUT_FILE = "data.json"

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in tqdm(data, desc="Cleaning descriptions"):
    desc = item.get("description", "")
    if desc:
        try:
            soup = BeautifulSoup(desc, 'html.parser')
            clean_text = soup.get_text(separator="\n", strip=True)
            clean_text = clean_text.replace('\n', ' ')
            item["description"] = clean_text
        except Exception as e:
            print(f" Error parsing description for ID {item.get('id')}: {e}")
            item["description"] = desc  # giữ nguyên nếu lỗi

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)