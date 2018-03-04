#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import json
import argparse

from bs4 import BeautifulSoup
import requests

TARGET_URL = 'https://ja.wikipedia.org/wiki/%E3%82%A6%E3%82%A7%E3%83%96%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0'

def main(argv=sys.argv[1:]):
    argvs = sys.argv
    if len(argvs) <= 1:
        print('Usage: python scraping_711.py "KEYWORD"')
        return
    elif len(argvs) > 2:
        print('KEYWORD is only one')
        return
    #print(argvs)
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument('output', type=argparse.FileType('w', encoding='utf-8'))
    # parser.add_argument('-f', '--format', default='json', choices=['json', 'csv'])
    # args = parser.parse_args(argv)
    #
    # fmt = args.format
    # output = args.output

    # ここから動く
    payload = {
        'keyword': argvs[1],
        'searchKeywordFlg': '1'
        }
    res_search = requests.get(TARGET_URL, params=payload)
    soup_search = BeautifulSoup(res_search.text, 'html.parser')
    result_list = soup_search.select('.productImg a')
    if len(result_list) == 0:
        print('検索結果が見つかりませんでした')
        return
    else:
        result_url = result_list[0].get('href')

    # 食品情報のテーブル要素を取得
    res = requests.get('http:{}'.format(result_url))
    soup = BeautifulSoup(res.text, 'html.parser')
    table_elm_list = soup.select('.oneColumnWrap table')

    table_contents_dict = {}
    # テーブル要素を辞書に格納
    if len(table_elm_list) == 1:
        table_contents = table_elm_list[0]
        th_list = table_contents.find_all('th')
        td_list = table_contents.find_all('td')
        for i in range(0, 5):
            table_contents_dict[th_list[i].text] = td_list[i].text

    # 結果出力
    if len(table_contents_dict) == 5:
        for key, value in table_contents_dict.items():
            print('{} : {}'.format(key, value))
    else:
        print('error: len(table_contents_dict) = {}'.format(len(table_contents_dict)))
    #ここまで動く

    # if fmt == 'json':
    #     data = json.dumps(titles, ensure_ascii=False, indent=2, sort_keys=True)
    #     output.write(data)
    # elif fmt == 'csv':
    #     writer = csv.writer(output)
    #     writer.writerows(titles)


if __name__ == '__main__':
    sys.exit(main())