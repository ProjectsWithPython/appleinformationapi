from bs4 import BeautifulSoup
import requests
import json
import re

url = requests.get("https://apple.fandom.com/wiki/IPhone")
url_two = requests.get('https://apple.fandom.com/wiki/List_of_Apple_products')
scarper = BeautifulSoup(url.text, 'html.parser')
scarper_two = BeautifulSoup(url_two.text, 'html.parser')


def name_scrape():
    data = scarper.select('.toctext')
    em = []
    for i in data:
        em.append(i.get_text())
    def filter_list(word):
        if word.startswith('i'):
            return True
        else:
            return False
    data = filter(filter_list, em)
    data = list(data)
    return data



def image_scape():
    images = scarper.select('.image')
    em = []
    for i in images:
        small =  i.select('img')
        for i in small:
            em.append(i.get_attribute_list('src')[0])
    
    def fil(word):
        if word.startswith('h'):
            return True
        else:
            return False
    data = filter(fil, em)
    data = list(data)
    return data


def scrape_products():
    em = []
    products = scarper_two.select('li')
    for i in products:
        string = i.get_text()
        replaced_string = re.sub(r"[\n]", '', string)
        more_better_replaced = re.sub(r"[\t]", '', replaced_string)
        em.append(more_better_replaced)
    def fil(word):
        if not word:
            return False
        else:
            return True
    data = filter(fil, em)
    data = list(data)
    return data
        


def main():
    return [{"images" : image_scape()}, {"models": name_scrape()}, {"products": scrape_products()}]