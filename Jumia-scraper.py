from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd

webpage = requests.get("https://www.jumia.ma").content
SparsedPage = BeautifulSoup(webpage, 'lxml')
Features = SparsedPage.find('div', attrs={'class': 'flyout'})
feature = Features.find_all('a', attrs={'class': 'itm'})

url = 'https://www.jumia.ma'

data = []

for link in feature:
    links = link.get('href')
    url_links = urljoin(url, links)
    sub_webpage = requests.get(url_links).content
    Sparsed_SubPage = BeautifulSoup(sub_webpage, 'lxml')
    Brand = Sparsed_SubPage.find_all('h3', attrs={'class': 'name'})
    Price = Sparsed_SubPage.find_all('div', attrs={'class': 'prc'})
    Reduction = Sparsed_SubPage.find_all('div', attrs={'class': 'bdg _dsct _sm'})
    Evaluation = Sparsed_SubPage.find_all('div', attrs={'class': 'stars _s'})


        
    if Brand and Price and Reduction and Evaluation:
        for brand, price, reduction, evaluation in zip(Brand, Price, Reduction, Evaluation):
            brand = brand.text.strip()
            price = price.text.strip()
            reduction = reduction.text.strip()
            evaluation = evaluation.text.strip()
            data.append({"product": brand, "price": price, "reduction": reduction, "evaluation": evaluation})


df = pd.DataFrame(data)
df.to_csv(r"C:\Users\computer\Desktop\Software & Data science projects\Websraping project\Jumia-scraper.csv", index=False)



