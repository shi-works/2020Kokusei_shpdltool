# -*- coding: utf-8 -*-
import csv
import requests

# 都道府県コードのリストを作成する
KenCodelist = []

# csvファイルの読み込み
with open('./KenCode.csv') as f:
    header = next(csv.reader(f))
    for row in csv.reader(f):
        s = row[0]
        KenCodelist.append(s)

# 都道府県コードのリストでループ
for KenCode in KenCodelist:
    # URL指定
    # 小地域
    url = "https://www.e-stat.go.jp/gis/statmap-search/data?dlserveyId=A002005212020&code=" + \
        KenCode + "&coordSys=1&format=shape&downloadType=5&datum=2011"
    # データをurlから取得する
    r = requests.get(url, stream=True)
    # zipファイルとして保存する
    saveFile = "D:/GIS/e-stat/境界データ/小地域/国勢調査/2020年/基本単位区_世界測地系緯度経度・Shapefile_JGD2011/" + \
        "A002005212020DDSWC" + KenCode + "-JGD2011.zip"
    with open(saveFile, 'wb') as f:
        f.write(r.content)
        print(KenCode)

print(u'処理終了')
