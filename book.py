from bs4 import BeautifulSoup as bs
from lxml.html.clean import Cleaner

sanitizar_url = Cleaner()

# url = 'https://www.deeplearningbook.com.br/uma-breve-historia-das-redes-neurais-artificiais/'
#
# conteudo = requests.get(url).content
with open('teste.html', 'r') as arquivo_html:
    conteudo = arquivo_html.read()

registro_conteudo = []
registro_imagens = []
soup = bs(conteudo, 'lxml')
titulo_capitulo = soup.find(class_='entry-title')  # raspa o título do conteúdo da página
registro_conteudo.append(titulo_capitulo.text)
conteudo_capitulo = soup.find(class_='entry-content')  # raspa o conteúdo textual e imagens contidas no texto da página
imagens = conteudo_capitulo.find_all('img')
for imagem in imagens:
    dados_imagem = imagem['alt'], imagem['src']
    registro_imagens.append(dados_imagem)

for parte in conteudo_capitulo:
    if parte.name == 'p':
        registro_conteudo.append(parte.text)
    else:
        continue

for x in registro_conteudo:
    contador = 0
    teste = 'Fig' in x
    if teste:
        registro_conteudo[registro_conteudo.index(x)] = registro_imagens[contador]
        contador += 1
    else:
        continue

# for c in registro_conteudo:
#     print(registro_conteudo.index(c), c)
# proximo_conteudo = soup.find(class_='navigation post-navigation')
#
# proximo_link = proximo_conteudo.find(name='div', class_='nav-next')
#
# if proximo_link is not None:
#     print(proximo_link.a['href'])
# else:
#     pass
