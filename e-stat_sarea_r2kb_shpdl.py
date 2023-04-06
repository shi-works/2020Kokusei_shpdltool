# -*- coding: utf-8 -*-
import csv
import requests

# 市区町村コードのリストを作成する
CityCodelist = []

# csvファイルの読み込み
with open('./CityCode.csv') as f:
    header = next(csv.reader(f))
    for row in csv.reader(f):
        s = row[0]
        CityCodelist.append(s)

# 都道府県コードのリストでループ
for CityCode in CityCodelist:
    # URL指定
    # 小地域
    url = "https://www.e-stat.go.jp/gis/statmap-search/data?dlserveyId=B002005212020&code=" + \
        CityCode + "&coordSys=1&format=shape&downloadType=5&datum=2011"

    # データをurlから取得する
    r = requests.get(url, stream=True)
    # zipファイルとして保存する
    saveFile = "D:/GIS/e-stat/境界データ/小地域/国勢調査/2020年/test/" + \
        "B002005212020DDSWC" + CityCode + "-JGD2011.zip"
    with open(saveFile, 'wb') as f:
        f.write(r.content)
        print(CityCode)

print(u'処理終了')
