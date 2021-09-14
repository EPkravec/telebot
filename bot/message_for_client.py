from parsing import data_link_client, browser, link_parse_client, total_contackt_client

link_client_parse = link_parse_client(browser,
                                      'https://www.youtube.com/results?search_query=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D1%8B&sp=CAE%253D')
i = -1
link_client_parse = set(link_client_parse)
link_client_parse = list(link_client_parse)
for l in link_client_parse[0:5]:
    i += 1
    data_link_client(browser, i, url=l)


total_contackt_client()

import glob
import json

result = []
for f in glob.glob(r'C:\Users\1\PycharmProjects\pythonProject\bot\bot\data_client\data_client.json'):
    with open(f, "r", encoding='utf-8') as infile:
        result.append(json.load(infile))


k = -1
for i in result:
    for h in i:
        k += 1
        print(i[k]['links_autor'])