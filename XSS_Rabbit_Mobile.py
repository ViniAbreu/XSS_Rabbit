import requests
import re
import os

class colors:
    vermelho = '\033[3;31m'
    verde = '\033[1;32m'
    azul = '\033[1;34m'
    ciano = '\033[1;36m'
    magenta = '\033[1;35m'
    amarelo = '\033[1;33m'
    preto = '\033[1;30m'
    branco = '\033[1;37m'
    original = '\033[0;0m'
    reverso = '\033[2m'
    default = '\033[0m'


def banner():
    try:
        os.system('clear')
    except:
        os.system('cls')
        pass
    print('''+--------------------------------------+
|               XSS Rabbit             |
+--------------------------------------+
|           Coder: Sr.Biggs            |
|          Telegram: @SrBiggs          |
|           Version: 1.0               |
|           Date: 20/11/2017           |
|           GitHub: /SrBiggs           |
+--------------------------------------+''')

def XSS():
    with open("Crawled.txt","r") as file:
        for site in file:
            site = site.replace("\n","")
            try:
                with open("XSS Payloads.txt","r") as payloads:
                    for payload in payloads:
                        payload = payload.replace("\n","")
                        try:
                            req = requests.get(site+payload)
                            html = req.text

                            if payload in html:
                                print(colors.amarelo + "\n=====================================")
                                print(colors.azul + "[*] Vulnerable to XSS [*]")
                                print(colors.verde + "[+] Url : " + colors.ciano + site)
                                print(colors.verde + "[+] Script : " + colors.ciano + payload)
                                print(colors.amarelo + "=====================================")

                                with open("Vulnerable to XSS.txt","a") as vulns:
                                    vulns.write(str(site+"\n"))
                                    vulns.close()

                                break
                            else:
                                break

                        except:
                            print(colors.vermelho + "[!] Error : Erro ao fazer a requisição" + colors.default)
            except Exception as erro:
                print(colors.vermelho + "[!] Error : " + colors.default + str(erro))

    print(colors.verde + "[*] Scan XSS finished sites vulneráveis salvos em 'Vulneraveis to XSS.txt'")

def bing(pages):
    count = 1

    with open('Dorks.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            dork = lines[i].strip()

            while count < pages:

                try:
                    req = requests.get('http://www.bing.com/search?q=' + dork + '&first=' + str(count))
                    html = req.text

                except Exception as erro:
                    print(colors.vermelho + "[!] Error : " + colors.default + str(erro))

                try:
                    regex = re.findall('<h2><a href="(.+?)"', html)

                    for x in regex:
                        print(colors.verde + "\n[+] Found : " + colors.default + x)

                        with open("Crawled.txt", "a") as b:
                            b.write(str(x + "\n"))
                            b.close()

                except Exception as erro:
                    print(colors.vermelho + "[!] Error : " + colors.default + str(erro))

                count += 10

        print(colors.amarelo + "\n\n[+] Starting XSS Scanner [+]" + colors.default)

        XSS()

def main():
    print(colors.amarelo)
    banner()
    page = int(input(colors.ciano + "[?] Informe numero de paginas\n>" + colors.default))*10
    bing(page)
    print(colors.default)

if __name__ == '__main__':
    main()