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
def scraper(request):
    all_balances = []
    all_names = []

    def filtering(donor, step, recipient) :
        count = 0
        for info in range(0, int(len(donor))) :
            if count == 0 :
                count = count + step
                recipient.append(donor[count])
            else :
                count = count + 6
                if count > len(donor) :
                    break
                else :
                    recipient.append(donor[count])

    def parser(link) :
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, "lxml")
        row_accounts_1 = soup.find_all("td")
        accounts_1 = []
        for item in row_accounts_1 :
            accounts_1.append(item.text)
        account_balance = []
        accounts_names = []
        filtering(accounts_1, 2, accounts_names)
        filtering(accounts_1, 3, account_balance)
        for acc in account_balance :
            all_balances.append(acc)
        for acc in accounts_names :
            all_names.append(acc)

    parser(f"https://etherscan.io/accounts")
    parser(f"https://etherscan.io/accounts/2")
    parser(f"https://etherscan.io/accounts/3")
    parser(f"https://etherscan.io/accounts/4")

    for n in range(0, len(all_balances)) :
        modified_1 = all_balances[n].replace(" Ether", "")
        modified_2 = float(modified_1.replace(",", ""))
        all_balances[n] = modified_2

    return render(request, 'chartapp/index.html', {"balance": all_balances, "data": all_names })