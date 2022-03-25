from bs4 import BeautifulSoup as bs
import re

# url = 'https://www.deeplearningbook.com.br/uma-breve-historia-das-redes-neurais-artificiais/'
#
# conteudo = requests.get(url).content
with open('teste2.html', 'r') as arquivo_html:
    conteudo = arquivo_html.read()

registro_conteudo = []
soup = bs(conteudo, 'lxml')
titulo_capitulo = soup.find(class_='entry-title')  # raspa o título do conteúdo da página
registro_conteudo.append(titulo_capitulo.text)
conteudo_capitulo = soup.find(class_='entry-content')  # raspa o conteúdo textual e imagens contidas no texto da página

padrao_p = re.compile('^<p.style="text\-align:.justify;">.')
padrao_ref = re.compile('^<p>.')
padrao_img = re.compile('^<p><img.')
padrao_img_alt = re.compile('^<p><figure\ class="centered\-image"><img.')
padrao_vazio = re.compile('^<p>.</p>$')

for parte in conteudo_capitulo:
    if bool(re.match(padrao_p, str(parte))):
        registro_conteudo.append(parte.text)
    elif bool(re.match(padrao_img, str(parte))) or bool(re.match(padrao_img_alt, str(parte))):
        imagem = parte.find('img')
        imagem_dados = (imagem['alt'], imagem['src'])
        registro_conteudo.append(imagem_dados)
    elif bool(re.match(padrao_ref, str(parte))):
        registro_conteudo.append(parte.text)
    elif bool(re.match(padrao_vazio, str(parte))):
        continue

for x in registro_conteudo:
    print(x)


# proximo_conteudo = soup.find(class_='navigation post-navigation')
#
# proximo_link = proximo_conteudo.find(name='div', class_='nav-next')
#
# if proximo_link is not None:
#     print(proximo_link.a['href'])
# else:
#     pass


