import json
import requests
import pandas as pd
import time
from tqdm import tqdm
from config import HEADERS, BASE_URL, BATCH_SIZE, MAX_WORKERS
from concurrent.futures import ThreadPoolExecutor, as_completed
import math
import os

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['name'] = json.get('name')
    d['url_key'] = json.get('url_key')
    d['price'] = json.get('price')
    d['description'] = json.get('description')
    d['thumbnail_url'] = json.get('thumbnail_url')
    return d

def fetch(pid):
    try:
        response = requests.get(BASE_URL.format(pid), headers=HEADERS, timeout=5)
        if response.status_code == 200:
            print('Crawl data {} success!!!'.format(pid))
            return ('success', parser_product(response.json()))
        else:
            print(f"Failed: {pid}, status code = {response.status_code}")
            return ('fail', {"id": pid, "status_code": response.status_code})
    except requests.exceptions.RequestException as e:
        print(f"Error for {pid}: {e}")
        return ('fail', {"id": pid, "error": str(e)})

df_id = pd.read_csv('product_id_tiki.csv')
p_ids = df_id['id'].tolist()

print(p_ids)
result = []
errors = []

start_time = time.time()

#chat gpt
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(fetch, pid): pid for pid in p_ids}
    for future in tqdm(as_completed(futures), total=len(futures), desc="Crawling"):
        status, data = future.result()
        if status == 'success':
            result.append(data)
        else:
            errors.append(data)

# for pid in tqdm(p_ids, total=len(p_ids)):
#     try:
#         response = requests.get(BASE_URL.format(pid), headers=HEADERS)
#         if response.status_code == 200:
#             print('Crawl data {} success!!!'.format(pid))
#             result.append(parser_product(response.json()))
#         else:
#             print(f"Failed: {pid}, status code = {response.status_code}")
#             errors.append({
#                 "id": pid,
#                 "status_code": response.status_code
#             })
#     except requests.exceptions.RequestException as e:
#         print(f"Error for {pid}: {e}")
#         errors.append({
#             "id": pid,
#             "error": str(e)
#         })
#     time.sleep(0.1)

df_products = pd.DataFrame(result)
df_products.to_json('project2.json', orient='records', force_ascii=False, indent=2)

with open('project2_errors.json', 'w', encoding='utf-8') as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)

#chat gpt
def write_chunks(data, prefix, outdir):
    os.makedirs(outdir, exist_ok=True)
    total_chunks = math.ceil(len(data) / BATCH_SIZE)
    for i in range(total_chunks):
        chunk = data[i * BATCH_SIZE : (i + 1) * BATCH_SIZE]
        filename = f"{outdir}/{prefix}_part_{i+1:03}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(chunk, f, ensure_ascii=False, indent=2)
        print(f" Saved {filename} ({len(chunk)} records)")

write_chunks(result, "project2", "output_parts")
write_chunks(errors, "project2_errors", "output_errors")
total = len(p_ids)
success = len(result)
fail = len(errors)
success_rate = round(success / total * 100, 2)
fail_rate = round(fail / total * 100, 2)

stats_df = pd.DataFrame([{
    "total_ids": total,
    "success": success,
    "fail": fail,
    "success_rate(%)": success_rate,
    "fail_rate(%)": fail_rate
}])
stats_df.to_csv('thong_ke.csv', index=False)
#Test git thui
# test nhé
#---