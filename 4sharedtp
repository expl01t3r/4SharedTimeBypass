import requests
import re




print('''
   __ __ _____ __                        __   _______                   ______  __                     
  / // // ___// /_  ____ _________  ____/ /  /_  __(_)___ ___  ___     / __ ) \/ /___  ____ ___________
 / // /_\__ \/ __ \/ __ `/ ___/ _ \/ __  /    / / / / __ `__ \/ _ \   / __  |\  / __ \/ __ `/ ___/ ___/
/__  __/__/ / / / / /_/ / /  /  __/ /_/ /    / / / / / / / / /  __/  / /_/ / / / /_/ / /_/ (__  |__  ) 
  /_/ /____/_/ /_/\__,_/_/   \___/\__,_/    /_/ /_/_/ /_/ /_/\___/  /_____/ /_/ .___/\__,_/____/____/  
                                                                             /_/                       

''')

def menu():
    op = int(input('''
1 - Resolver outro link
2 - Sair
Escolha: '''))
    if op == 1:
        link()
    elif op == 2:
        exit()
    else:
        print('OpÃ§Ã£o invalida!')
        menu()

def link():
    url=input('url: ')
    url= re.sub('.com/.*?/','.com/get/', url)
    sessao = requests.get(url)
    sessao = requests.get(url, cookies=sessao.cookies)
    reg = re.search('(<input type="hidden" id="baseDownloadLink" value=")(.*?)("/>)', sessao.content.decode('UTF-8'))
    print('\nLink resolvido: {link}\n' .format(link =reg.group(2)))
    menu()

link()
