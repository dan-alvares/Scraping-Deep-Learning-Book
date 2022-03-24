from bs4 import BeautifulSoup as bs
from lxml.html.clean import Cleaner

sanitizar_url = Cleaner()

# url = 'https://www.deeplearningbook.com.br/uma-breve-historia-das-redes-neurais-artificiais/'
#
# conteudo = requests.get(url).content
with open('teste.html', 'r') as arquivo_html:
    conteudo = arquivo_html.read()

registro_conteudo = []
soup = bs(conteudo, 'lxml')
titulo_capitulo = soup.find(class_='entry-title')  # raspa o título do conteúdo da página
registro_conteudo.append(titulo_capitulo.text)
conteudo_capitulo = soup.find(class_='entry-content')  # raspa o conteúdo textual e imagens contidas no texto da página


for parte in conteudo_capitulo:
    if parte.name == 'p':
        # and parte.attrs['style'][0] == 'text-align: justify;':
        if parte.find_next == 'img':
            registro_conteudo.append(parte['src'])
        else:
            registro_conteudo.append(parte.text)
    else:
        pass

# for i in registro_conteudo:
#     print(i)

for i in registro_conteudo:
    print(i)

# proximo_conteudo = soup.find(class_='navigation post-navigation')
#
# proximo_link = proximo_conteudo.find(name='div', class_='nav-next')
#
# if proximo_link is not None:
#     print(proximo_link.a['href'])
# else:
#     pass
