import requests
import json
from flask import Flask, jsonify


app = Flask(__name__)
from collections import Counter

@app.route('/')

@app.route('/seach')
def seach():
    return str(json_str)


def resquest_api(filme, page):
    return requests.get(
        'https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}'.format(filme, page)).json()


def getListYear(pJson, vNumReg):
    vCount = 0
    listTemp = []
    i = 0
    for i in range(0, vNumReg):
        listTemp.append(pJson[vCount]["Year"])

        vCount += 1

    return listTemp


def group_list(lst):
    return list(zip(Counter(lst).keys(), Counter(lst).values()))


search_input = input("Digite o nome para pesquisa: ")

content_json = resquest_api(search_input, 1)

vPaginaAtual = int(content_json['page'])
vTotalPages = int(content_json['total_pages'])
vTotalReg = str(content_json['total'])
listCountMovies = []

for i in range(0, vTotalPages):
    listYear = getListYear(content_json["data"], len(content_json["data"]))
    json_str = []

    if (vTotalPages > 1 and vPaginaAtual < vTotalPages):
        listCountMovies += listYear
        vPaginaAtual += 1
        content_json = resquest_api(search_input, vPaginaAtual)

    else:
        vCount = 0
        listCountMovies += listYear
        listCountMovies = list(group_list(listCountMovies))

        if vCount == 0:
            json_str.append("{ moviesByYear: [")
            json_str.append("")

        for x in range(0, len(listCountMovies)):
            json_str[1] += str(listCountMovies[vCount])
            vCount += 1

        json_str = [w.replace('(', '{Year:') for w in json_str]
        json_str = [w.replace(', ', ', movies:') for w in json_str]
        json_str = [w.replace(')', '},') for w in json_str]
        json_str = [w.replace(')', '},') for w in json_str]
        json_str.append("total: " + vTotalReg)
        json_str.append("}")

        json_Str = json.dumps(json_str)

        # json_Str = json.dumps(listCountMovies)
        # print(sorted(group_list(listCountMovies)))
        print(json_Str)
        if __name__ == '__main__':
            app.run()