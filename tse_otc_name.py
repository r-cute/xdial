import json
import urllib.request
import gzip

save_path = './docs/manual/tw_stock.js'

# 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL'
tpex_url = 'otc.json'#'https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyQuotes?response=json'
tse_url = 'tse.json'#'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&type=ALLBUT0999'

def fetch_json(url):
    if(url.startswith('http')):
        with urllib.request.urlopen(url) as response:
            return json.load(response)
    else:
        with open(url, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

ret = {"tse": {x[0]:x[1] for x in fetch_json(tse_url)["tables"][8]["data"]},
        "otc": {x[0]:x[1] for x in fetch_json(tpex_url)["tables"][0]["data"]}}

# with gzip.open(save_path, 'wt', encoding='utf-8') as gz_file:
#     json.dump(ret, gz_file, separators=(',', ':'))

with open(save_path, 'w', encoding='utf-8') as json_file:
    json.dump(ret, json_file, separators=(',', ':'), ensure_ascii=False)
