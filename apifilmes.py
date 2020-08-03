import requests
from collections import Counter

def resquest_api(filme, page):
   return requests.get('https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}'.format(filme, page)).json()

def getListYear(pJson, vNumReg):
    vCount = 0
    listTemp = []

    for i in range(0, vNumReg):
        listTemp.append(pJson[vCount]["Year"])
        vCount += 1

    listTemp += listTemp

    return listTemp

def group_list(lst):
    return list(zip(Counter(lst).keys(), Counter(lst).values()))

search_input = input("Digite o nome para pesquisa: ")

content_json = resquest_api(search_input, 1)

vPaginaAtual = int(content_json['page'])
vTotalPages = int(content_json['total_pages'])
listCountMovies = []

for i in range(0, vTotalPages):
    listYear = getListYear(content_json["data"], len(content_json["data"]))

    if (vTotalPages > 1 and vPaginaAtual < vTotalPages):
        listCountMovies += listYear
        vPaginaAtual += 1
        content_json = resquest_api(search_input, vPaginaAtual)
    else:
        listCountMovies += listYear
        print(sorted(group_list(listCountMovies)))


