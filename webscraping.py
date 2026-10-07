import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


hoje = datetime.now().strftime(r'%Y-%m-%d %H-%M')
html = requests.get('https://www.stuttgart.com.br/bebidas/cervejas.html?product_list_limit=36')
soup = BeautifulSoup(html.text, 'html.parser')

produtos = []
for produto in soup.select('#layer-product-list .product-item-details'):
     titulo = produto.select_one('.product-item-link').text.strip()
     familia = produto.select_one('.german_name').text.strip()
     codigo = produto.select_one('.sku').text.strip()
     preco = produto.select_one('.price-box').text.strip()

     produtos.append({
          'titulo':titulo,
          'familia':familia,
          'codigo':codigo,
          'preco': preco
     })

df = pd.DataFrame(produtos)
df.to_csv(f'{hoje} - cervejas.csv')

#for preco in soup.select('.sku , .german_name, .price'):
    #print(preco.text.strip())


