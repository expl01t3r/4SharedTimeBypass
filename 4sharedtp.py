import requests
import re
import os







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
1 - Resolver 1 link
2 - Resolver links de um arquivo
3 - Sair
Escolha: '''))
    if op == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(link(input('Link a Ser quebrado: ')))
    elif op == 2:
        arquivo = open(input('Caminho do arquivo com os links\n Ex.: C:\Arquivo.txt : '))
        for x in arquivo:
            link(x)
        menu()
    elif op == 3:
        exit()
    else:
        print('Opção invalida!')
        menu()


def link(url):
    url= re.sub('.com/.*?/','.com/get/', url)
    sessao = requests.get(url)
    sessao = requests.get(url, cookies=sessao.cookies)
    reg = re.search('(<input type="hidden" id="baseDownloadLink" value=")(.*?)("/>)', sessao.content.decode('UTF-8'))
    print('\nLink resolvido: {link}\n' .format(link =reg.group(2)))



menu()
