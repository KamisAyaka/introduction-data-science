import requests
import csv
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55"
}
url = 'https://hoopshype.com/salaries/2018-2019/'

page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)

tr_list = tree.xpath('//*[@id="content-container"]/div/div[3]/div[2]/table/tbody/tr')
name_list = []
number_list = []

for tr in tr_list:
    name = tr.xpath('./td[2]/a/text()')[0]
    name = str(name).replace('\n', '').replace('\t', '')
    name_list.append(name)
    number = tr.xpath('./td[3]/text()')[0]
    number = str(number).replace('\n', '').replace('\t', '').replace('$', '')
    number_list.append(number)

csv_file_path = '2018.csv'

with open(csv_file_path, 'w', newline='', encoding= 'utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(name_list)
    csv_writer.writerow(number_list)
    csv_file.close()

