# -*- coding: utf-8 -*-
"""NASAKamensky.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YKpQFwmljF0SS7XiOj6poKLvFqo_Lnr7
"""

!pip install requests

import requests

API_KEY = 'MbNWQfHAsg9gatULkp04nACdeqPBrJqihYNQSEWo'

def Photo(URL):
    api_key = "MbNWQfHAsg9gatULkp04nACdeqPBrJqihYNQSEWo"
    date = '2022-08-11'
    query_params = {"api_key": api_key, "earth_date": date}
    response = requests.get(URL,params=query_params).json()
    ans = (response)
    return ans['photos'][:3]

Photo("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?")

