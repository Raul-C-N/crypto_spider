import requests as rq
from bs4 import BeautifulSoup as soup
import time
from datetime import date
########## FAZER POR REQUESTS!################

today = date.today()
my_url = 'https://cryptonews.com/news/'
filename = "news_cyrptonews.com"+str(today)+".csv"

def Scrapper (my_url):
    """SCRAPPER BÁSICO
    insira a página no valor my_url sem o número índice final.
    exemplo: https://www.mercadolivre.com.br/ofertas?page=3 deve ser inserido como https://www.mercadolivre.com.br/ofertas?page= """
    # opening up connection, grabbing the page
    ##page = 1
    count = 0
    ##my_url += str(page)
    fonte_html = rq.get(my_url)
    texto_html = fonte_html.text
    ###Preparando arquivo CSV
    f = open(filename, "w")
    headers = "manchete, link, \n"
    f.write(headers)
    
    #html parsing
    pag_sopa = soup(texto_html, "html.parser")

    # grabs each container
    
    containers = pag_sopa.find_all("article",{"class":"mb-30"})

    for container in containers:
        count +=1 
        
        #manchete artigo
        try:
            manchete_container = container.h4.text
            manchete_artigo = str(manchete_container)
        except:
            manchete_artigo = None

        #link da notícia
        try:
            link_container = container.findAll('a')
            url_list_temp = [] #abrir lista de urls
            for url in link_container:
                url_list_temp.append(url.get('href')) #apensar a url quebrada do site na lista, a url que interessa é de índice [0]
            # retirar o link do site - eles não facilitam a extração no código fonte da página
            # print (url_list_temp[0], 4*'\n') #teste de obtenção das urls parciais
            #print ((str(my_url)[:-6]) + str(url_list_temp[0])) #url base + item [0] da lista de url dá a página a ser visitada
            url_final = (str(my_url)[:-6]) + str(url_list_temp[0])
        except:
            url_final = None
                
        #ESCREVENDO NO ARQUIVO CSV
        #f.write (str(manchete_artigo.replace(",",".")) + ',' (str(link_texto.replace(",","."))+ '\n')
        f.write (str(manchete_artigo.replace(",","."))+','+url_final+","+str(count)+'\n')
        print (count)
        print ("Manchete: "+manchete_artigo+"\n")
        print ("link: "+ url_final+'\n')
        print ("----------------------------------------------")

    f.close()

Scrapper(my_url)