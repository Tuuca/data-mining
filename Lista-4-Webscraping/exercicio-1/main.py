import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000"

resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html, 'html.parser')

cursos = soup.find_all('ul', class_='curso')

for curso in cursos:
    nome = curso.find('li', class_='nome').text
    area = curso.find('li', class_='area').text
    carga = curso.find('li', class_='carga').text
    conteudos = curso.find_all('li', class_='descricao')

    print(f'Nome: {nome}')
    print(f'Área: {area}')
    print(f'Carga Horária: {carga}')
    for conteudo in conteudos:
        print(f'Conteúdo: {conteudo.text}')
    print('\n---\n')