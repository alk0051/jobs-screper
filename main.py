import requests
from bs4 import BeautifulSoup


url = 'https://programathor.com.br/jobs-node-js?expertise=J%C3%BAnior'


def getData():
    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    jobsList = soup.find('div', class_="cell-list-content")

    title = jobsList.find('h3', class_="text-24 line-height-30")

    company = jobsList.findNext('div', class_="cell-list-content-icon")

    print(title)
    print(company)


getData()
