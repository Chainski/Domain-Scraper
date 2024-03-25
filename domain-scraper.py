#Author: chainski
#Github: https://github.com/chainski

import os
import requests,json
import os.path
from colorama import Fore
os.system('mode con: cols=160 lines=40')


banner = '''
                             ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
                             ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                             ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
                             ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
                             ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
                             ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
'''

info = '''
                                                                   ╔════════════════════════════════╗
                                                                   ║       DOMAIN SCRAPER V1.0      ║                                              
                                                                   ║       coded by chainski        ║
                                                                   ║ For Educational Purposes Only  ║                                     
                                                                   ║   https://github.com/chainski  ║              
                                                                   ╚════════════════════════════════╝
'''

    

print(Fore.CYAN+banner)
print(Fore.LIGHTGREEN_EX+info)

def main():

    choice ='0'
    while choice =='0':
        print(Fore.RESET+"                                                                        API URL:hackertarget.com")
        choice = input (Fore.LIGHTGREEN_EX+"\n\n [+] Press 1 To Start: ")
        if choice == "1":
            Hackertarget()
        else:
            print("I don't understand your choice.")


def Hackertarget():
    os.system("cls")
    print("""
╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗╔╦╗╔═╗╦═╗╔═╗╔═╗╔╦╗
╠═╣╠═╣║  ╠╩╗║╣ ╠╦╝ ║ ╠═╣╠╦╝║ ╦║╣  ║ 
╩ ╩╩ ╩╚═╝╩ ╩╚═╝╩╚═ ╩ ╩ ╩╩╚═╚═╝╚═╝ ╩
    """)
    session = requests.session()
    inip = input('Enter URL or IP: ')
    print("\n=========== Output ===============")
    api = "http://api.hackertarget.com/reverseiplookup/?q="
    apipun = api + inip
    output = session.get(apipun).text
    print(output)
    file = input("Save output to txt? [Y/n]").lower()
    if file == 'y':
        fila = input("\nFilename: ")
        filename = fila + ".txt"
        file1 = open(filename, "w")
        file1.write(str(output))
    else:
        print("\nThank for using my tool !")


main()
