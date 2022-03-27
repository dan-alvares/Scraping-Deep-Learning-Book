from bs4 import BeautifulSoup as bs
import re
import requests
import time

url = 'https://www.deeplearningbook.com.br/deep-learning-a-tempestade-perfeita/'


def criar_arquivo(titulo, link):
    with open(f'{titulo}.txt', 'w') as arquivo:
        arquivo.write(f'Conteúdo criado por Data Science Academy\n'
                      f'Link para acessar o conteúdo original: {link}\n')
        arquivo.write('/' * 30 + '\n')
        arquivo.write(f'{titulo}\n')
        arquivo.write('/' * 30 + '\n')


def inserir_txt(titulo, linha_txt):
    with open(f'{titulo}.txt', 'a') as arquivo_txt:
        arquivo_txt.write(linha_txt)


def scrape(link):
    conteudo = requests.get(link).content
    # registro_conteudo = []

    soup = bs(conteudo, 'lxml')
    titulo_capitulo = soup.find(class_='entry-title').text  # raspa o título do conteúdo da página
    criar_arquivo(titulo_capitulo, link)  # cria arquivo txt com o título do capítulo
    conteudo_capitulo = soup.find(
        class_='entry-content')  # raspa o conteúdo textual e imagens contidas no texto da página

    # Cria padrão para adequar formatação das linhas raspadas
    padrao_p = re.compile('^<p style="text-align: justify;"> ')
    padrao_ref = re.compile('^<p> ')
    padrao_img = re.compile('^<p><img ')
    padrao_img_alt = re.compile('^<p><figure class="centered-image"><img ')
    padrao_vazio = re.compile('^<p> </p>$')

    for parte in conteudo_capitulo:
        if bool(re.match(padrao_p, str(parte))):
            inserir_txt(titulo_capitulo, parte.text + '\n')
        elif bool(re.match(padrao_img, str(parte))) or bool(re.match(padrao_img_alt, str(parte))):
            imagem = parte.find('img')
            imagem_dados = (imagem['alt'], imagem['src'])
            inserir_txt(titulo_capitulo, str(imagem_dados) + '\n')
        elif bool(re.match(padrao_ref, str(parte))):
            inserir_txt(titulo_capitulo, parte.text + '\n')
        elif bool(re.match(padrao_vazio, str(parte))):
            continue

    time.sleep(10)
    proximo_conteudo = soup.find(class_='navigation post-navigation')

    proximo_link = proximo_conteudo.find(name='div', class_='nav-next')

    if proximo_link is not None:
        nova_url = proximo_link.a['href']
        print(f"Acessando próxima página >> {nova_url}")
        scrape(nova_url)
    else:
        pass


scrape(url)
