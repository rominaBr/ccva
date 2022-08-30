from django.shortcuts import render
import requests



def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_dolar(params={}):
    response = generate_request('https://www.dolarsi.com/api/api.php?type=valoresprincipales', params)
    if response:
       casa = response     
       return casa

    return ''