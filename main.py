import requests
from bs4 import BeautifulSoup


url = 'https://programathor.com.br/jobs-node-js?expertise=J%C3%BAnior'


def getData():
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    jobsList = soup.findAll('div', class_="cell-list-content")

    i = 0

    for job in jobsList:
        title = job.find(
            'h3', class_="text-24 line-height-30").text

        infosList = job.find('div', class_="cell-list-content-icon")

        infos = infosList.findAll('span')

        with open(f'data/{i}.txt', 'w') as f:
            print('Titulo da vaga:    ', title)
            print('Empresa:           ', infos[0].text)
            print('Local de trabalho: ', infos[1].text)
            print('Porte da empresa:  ', infos[2].text)
            print('Expect. salarial:  ', infos[3].text)
            print('Nivel:             ', infos[4].text)
            print('PJ/ CLT:           ', infos[5].text)
            print('\n -------------------------------------- \n')

            f.write(f"Titulo da vaga: {title} \n")
            f.write(f"Empresa: {infos[0].text} \n")
            f.write(f"Local de trabalho: {infos[1].text} \n")
            f.write(f"Porte da empresa: {infos[2].text} \n")
            f.write(f"Porte da empresa: {infos[3].text} \n")
            f.write(f"Nivel: {infos[4].text} \n")
            f.write(f'PJ/ CLT: {infos[5].text}')

            i = i + 1


getData()
