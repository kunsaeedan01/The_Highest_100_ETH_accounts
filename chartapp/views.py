from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import lxml
from bs4 import BeautifulSoup
chrome_driver_path = "C:/Users/Lenovo LEGION/Desktop/chromedriver.exe"
# Create your views here.


def index(request):

    data = "Current Data"
    return render(request, 'chartapp/index.html', {"data": data})
