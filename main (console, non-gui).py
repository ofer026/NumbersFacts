from bs4 import BeautifulSoup
import requests

type = input("enter the type of info you want to get (date, math, year (leave blank for trivia)): ")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.57756"}


URL = "http://numbersapi.com/"

if type.lower() == "date":
    while True:
        day = input("enter the day in the date (or type random): ")
        if day.lower() == "random":
            break
        try:
            int(day)
        except ValueError:
            pass
        else:
            if int(day) >= 32:
                pass
            elif int(day) <= 0:
                pass
            else:
                break
    while True:
        month = input("enter the month in the date (if you typed \"random\" in day, type 1): ")
        try:
            int(month)
        except ValueError:
            pass
        else:
            if int(month) >= 12:
                pass
            elif int(month) <= 0:
                pass
            else:
                break
    if day.lower() == "random":
        URL += day + "/date"
    else:
        URL += month + "/" + day + "/date"
elif type.lower() == "year":
    while True:
        year = input("enter the year that you want to get info about (or type random): ")
        if year.lower() == "random":
            break
        try:
            int(year)
        except ValueError:
            pass
        else:
            break
    if year.lower() == "random":
        URL += "random/year"
    else:
        URL += year + "/year"
elif type.lower() == "math":
    while True:
        num = input("enter the number that you want to get info about (or type random): ")
        if num.lower() == "random":
            break
        try:
            int(num)
        except ValueError:
            pass
        else:
            break
    URL += num + "/math"
elif type.lower() == "":
    while True:
        num = input("enter the number that you want to get info about (or type random): ")
        if num.lower() == "random":
            break
        try:
            int(num)
        except ValueError:
            pass
        else:
            break
    URL += num
else:
    raise Exception("What you typed is neither date nor math nor year nor blank")

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
input()

#print(URL)