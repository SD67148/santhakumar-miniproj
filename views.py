from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import requests as r
# Create your views here.

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    if(val1=="amazon" and val2=="realme"):
        URL = "https://www.flipkart.com/search?q=real+me+smart+watch&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
        page = r.get(URL)
        soup = bs(page.content, "html.parser")
        price = soup.find("div", {"class": "_30jeq3 _16Jk6d"}).text
        res=price
    elif (val1 == "flipkart" and val2 == "realme"):
        URL = "https://www.amazon.in/realme-TFT-LCD-Touchscreen-Monitoring-Resistance/dp/B08MB8YL5X/ref=sr_1_4?keywords=real%2Bme%2Bsmart%2Bwatch&qid=1650977604&sr=8-4&th=1"
        page = r.get(URL)
        soup = bs(page.content, "html.parser")
        price = soup.find("div", {"class": "_30j777878  6d"}).text
        res = price

    return render(request, 'home.html', {'res': price})
prc=input()
def home(request):
    return render(request, "mee.html", {'gname': prc})