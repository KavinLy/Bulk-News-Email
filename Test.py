import smtplib
import pandas as pd
from urllib.request import urlopen
import json 

def whatCategory(category):
    if category == 'technology':
        url = urlopen('http://newsapi.org/v2/top-headlines?country=gb&category=technology&apiKey=80ed1377f8a942c1838e28b64d593b63')
        sendmail(url, category)
    elif category == 'entertainment':
        url = urlopen('http://newsapi.org/v2/top-headlines?country=gb&category=entertainment&apiKey=80ed1377f8a942c1838e28b64d593b63')
        sendmail(url, category)
    elif category == 'business':
        url = urlopen('http://newsapi.org/v2/top-headlines?country=gb&category=business&apiKey=80ed1377f8a942c1838e28b64d593b63')
        sendmail(url, category)
    elif category == 'general':
        url = urlopen('http://newsapi.org/v2/top-headlines?country=gb&category=general&apiKey=80ed1377f8a942c1838e28b64d593b63')
        sendmail(url, category)
    else:
        print('Not a valid category!')

def sendmail(url, category):
    data = json.loads(url.read())
    json_str=json.dumps(data)
    resp=json.loads(json_str) 
    exEmail = pd.read_excel('Email.xlsx')
    emails = exEmail['Emails'].values
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('lyk4coventry@gmail.com', 'Random-01')
    content = resp["articles"][0]['content']
    lenContent = content[0:150]
    bodyMsg = resp["articles"][0]['description'] + '\n\n' + lenContent + '...' + '\n\n To read more click the link below: \n' + resp["articles"][0]['url']
    body = bodyMsg
    title = resp["articles"][0]['title']
    subject = title
    message = 'Subject: {}\n\n{}'.format(subject,body)

    for email in emails:
        server.sendmail('lyk4coventry@gmail.com', email, message)
    server.quit()
    print('Email has been sent!')

whichCategory = input('Which email category to send? ')
lowerCat = whichCategory.lower()
whatCategory(lowerCat)
