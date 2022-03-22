from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
from datetime import date

today = date.today()
my_url = 'https://www.mercadolivre.com.br/ofertas?page='
filename = "ofertas_dia_ML_acum"+str(today)+".csv"
f = open(filename, "w")

def Scrapper (my_url):
    """SCRAPPER BÁSICO
    insira a página no valor my_url sem o número índice final.
    exemplo: https://www.mercadolivre.com.br/ofertas?page=3 deve ser inserido como https://www.mercadolivre.com.br/ofertas?page= """
    # opening up connection, grabbing the page
    ##page = 1
    count = 0
    ##my_url += str(page)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    
    #html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs each container
    containers = page_soup.findAll("div",{"class":"promotion-item__container"})

    for container in containers:
        count +=1 

        #product title
        try:
            title = container.img["alt"]
        except:
            title = "None"

        #preço antigo
        try:
            preco_antigo_container = container.findAll("span",{"class":"promotion-item__oldprice"})
            preco_antigo = preco_antigo_container[0].text
        except:
            preco_antigo = "None"

        #preço novo
        try:
            preco_novo_container = container.findAll("span",{"class":"promotion-item__price"})
            preco_novo = preco_novo_container[0].text
        except:
            preco_novo = "None"
        #frete
        try:
            frete_container = container.findAll("span",{"class":"promotion-item__shipping"})
            frete = frete_container[0].text
        except:
            frete = "None"
        
        #ESCREVENDO NO ARQUIVO CSV
        f.write (title.replace(",", "|") + ',' + str(preco_antigo.replace(",",".")) + ',' + str(preco_novo) + ',' + str(frete)+ ',' + str(count) + '\n')

        print (count)
        print ("Produto: "+title+"\n")
        print ("Preço antigo: "+preco_antigo+"\n")
        print ("Preço novo: "+preco_novo+"\n")
        print ("Frete: "+frete+"\n")
        print ("----------------------------------------------")


""" Scrapper(my_url) """


def trade_spider(my_url, max_pages):
    page =1
    my_url_original = my_url
    while page <= max_pages:        
        Scrapper(my_url)
        print ("PÁGINA")
        print (page)
        page += 1
        my_url = my_url_original + str(page) 
        print (my_url)
        
def Craw_csv (max_pages):

    #preparando arquivo CSV para gravação
    filename = "ofertas_dia_ML_acum.csv"
    f = open(filename, "w")
    headers = "produto, preco_antigo, preço_promoção, frete, id, \n"
    f.write(headers)

    trade_spider (my_url, max_pages)

    f.close()

Craw_csv(10)
print ("Craw está em módulo. Importe e use Craw_csv(max_pages) para prosseguir.")

""" Python programming tutorial 26 how to build a web crawler """