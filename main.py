import requests
from bs4 import BeautifulSoup


url = 'https://programathor.com.br/jobs-node-js?expertise=J%C3%BAnior'


def getData():
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    jobsList = soup.findAll('div', class_="cell-list-content")

    for job in jobsList:
        title = job.find(
            'h3', class_="text-24 line-height-30").text

        infosList = job.find('div', class_="cell-list-content-icon")

        infos = infosList.findAll('span')

        print('Titulo da vaga:    ', title)
        print('Empresa:           ', infos[0].text)
        print('Local de trabalho: ', infos[1].text)
        print('Porte da empresa:  ', infos[2].text)
        print('Porte da empresa:  ', infos[3].text)
        print('Nivel:             ', infos[4].text)
        print('PJ/ CLT:           ', infos[5].text)
        print('\n -------------------------------------- \n')


getData()
