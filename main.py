import requests, random, string, bs4, os
import rich
from rich import print
from rich.console import Console
import time


console = Console()

os.system("cls")
console.print(f"""\n\n

                 '
            *          .
                   *       '
              *                *                               
               Steam Checker.
          @t2zC.          10/07/22 
       '*
           *
                *
                       *
               *
                     *

                                                      
\n""", style="purple")


#Config
len = 5
webhook = input("           Webhook: ")

#Check webhook
r = requests.get(webhook)
r.status_code
if r.status_code == 401:
    console.print("           Invalid Webhook", style="red")
    time.sleep(2.4)
    exit()



#ID check
while True:
    id = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=len))
    request = requests.get(f'https://steamcommunity.com/id/{id}')
    lxml = bs4.BeautifulSoup(request.content, 'lxml')
    title = lxml.find('title')
    list = title.text.split()
    if list[-1] == "Error":
        print(f'{id} is Available')
        requests.post(webhook, data={"content" : "\🌠 New ID Found `"f'{id}'"` \n remember **it can be banned** or **blacklisted.** ;3\n`--------------------------------`"})
    else:
        print(f'{id} is Taken')

#Original made by @Femboysito in github.
