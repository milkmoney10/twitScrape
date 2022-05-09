from django.shortcuts import render
import requests


def home(request):
    apikey = ""
    secretkey = ""
    bearertoken = ''

    headers = {
        'Authorization': f"Bearer {bearertoken}",
    }
    params = (
        ('max_results', '15'),
        ('user.fields', 'description')
    )

    ids = [['Sisyphus', '1366930865574584323'],
           ['larry0x', '1134151355776585729'],
           ['Cryptoyieldinfo', '1241561583450390528'],
           ['noahseidman', '38810696'],
           ['fomosaruus', "929827324563947521"],
           ["billybogbaghold", "971741153530757120"],
           ["korpi87", "2375428142"],
           ['sourcex', '1365181321073451009'],
           ['guleid', '1384598458263277569'],
           ['cryptoexpert101', '951353538851950594'],
           ['degencryptoinfo', '1313895595292139523'],
           ['TheShual', '1334586569076903937'],
           ['sandra leow', '1341662614313525248'],
           ['DCF GOD', '1350996311777161219'],
           ['Alpha Only', '1452540915168337923']]

    context = {'profiles': []}
    for i in ids:
        emptyDict = {}
        response = requests.get(
            f"https://api.twitter.com/2/users/{i[1]}/following", headers=headers, params=params)
        print(response)
        getUserName = requests.get(
            f"https://api.twitter.com/2/users/{i[1]}", headers=headers)
        emptyDict[f"{getUserName.json()['data']['username']}"] = response.json()[
            'data']
        context['profiles'].append(emptyDict)

    return render(request, 'home.html', context)
