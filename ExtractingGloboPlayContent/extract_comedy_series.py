from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs


file = codecs.open("C:\\Users\\thier\\ExtractingGloboPlayContent\\comedy_series.html", "r", "utf-8")
soup = BeautifulSoup(file.read(), 'html.parser')

results = soup.find_all('span', attrs={'class': 'playkit-thumb__thumb-link-wrapper'})
for series in results:
    holder = series.find('a')
    title = holder.get('title')
    url_reference = "https://globoplay.globo.com" + holder.get('href')
    print(title)
    print('\n')
    print("url: " + url_reference)
    
    # Get details from Series
    url = url_reference + "detalhes/"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get Datasheet
    dataSheet = soup.find('div', attrs={'class': 'title-details-offer'})
    #print(dataSheet)

    sinopse = dataSheet.find('p', attrs={'class': 'title-details-offer__synopsis-description'})
    sinopse = sinopse.get_text()
    print("Sinopse: " + sinopse)

    basic_info = dataSheet.find('div', attrs={'class': 'title-details-offer__basic-info'})
    basic_info = basic_info.find_all('div', attrs={'class': 'title-details-offer-item'})
    roteiro = ""
    elenco = ""
    #print(basic_info)
    if (len(basic_info) > 1):
        roteiro = basic_info[1].get_text()
        roteiro = roteiro.split(': ')
        roteiro = roteiro[1]
    if (len(basic_info) > 2):    
        elenco = basic_info[2].get_text()
        elenco = elenco.split(': ')
        elenco = elenco[1]
    print("Roteiro: " + roteiro + '\n' + "Elenco: " + elenco)

    additional_info = dataSheet.find('div', attrs={'class': 'title-details-offer__additional-info'})
    additional_info = additional_info.find_all('div', attrs={'class': 'title-details-offer-item'})
    #print(additional_info)
    genero = ""
    ano = ""
    pais = ""
    
    if (len(additional_info) > 0):    
        genero = additional_info[0].get_text()
        genero = genero.split(': ')
        genero = genero[1]
    if (len(additional_info) > 1):
        ano = additional_info[1].get_text()
        ano = ano.split(': ')
        ano = ano[1]
    if (len(additional_info) > 2):
        pais = additional_info[2].get_text()
        pais = pais.split(': ')
        pais = pais[1]

    print("Gênero: " + genero + '\n' + "Ano de Lançamento: " + ano + '\n' + "País de Origem: " + pais)
    print('-----------------------------------------------------')
    print('\n')
    








