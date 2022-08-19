from pystyle import *
import requests, random, string
import threading, os, time
from random import choice

erreur=0
lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
fail=0

os.system('cls')

class spotify:

    def __init__(self, profile, proxy = None):
        self.session = requests.Session()
        self.profile = profile
        self.proxy = proxy
    
    def register_account(self):
        headers = {
            "Accept": "*/*",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.spotify.com/"
        }
        email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
        password = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
        proxies = None
        if self.proxy != None:
            proxies = {"https": f"http://{self.proxy}"}
        data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/fr/&displayname=github.com/ZeusFuckYou/Venomix_&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
        try:
            create = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers = headers, data = data, proxies = proxies)
            if "login_token" in create.text:
                login_token = create.json()['login_token']
                return login_token
            else:
                return None
        except:
            return False

    def get_csrf_token(self):
        try:
            r = self.session.get("https://www.spotify.com/fr/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
            return r.text.split('csrfToken":"')[1].split('"')[0]
        except:
            return None
        
    def get_token(self, login_token):
        headers = {
            "Accept": "*/*",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": self.get_csrf_token(),
            "Host": "www.spotify.com"
        }
        self.session.post("https://www.spotify.com/api/signup/authenticate", headers = headers, data = "splot=" + login_token)
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "WebPlayer",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/"
        }
        try:
            r = self.session.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers
            )
            return r.json()["accessToken"]
        except:
            return None

    def follow(self):
        if "/user/" in self.profile:
            self.profile = self.profile.split("/user/")[1]
        if "?" in self.profile:
            self.profile = self.profile.split("?")[0]
        login_token = self.register_account()
        if login_token == None:
            return None, erreur
        elif login_token == False:
        
            return None, erreur
        auth_token = self.get_token(login_token)
        if auth_token == None:
            return None, "while getting auth token"
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "app-platform": "WebPlayer",
            "Referer": "https://open.spotify.com/",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "authorization": "Bearer {}".format(auth_token),
        }
        try:
            self.session.put(
                f"https://api.spotify.com/v1/playlists/{self.profile}/followers",
                headers = headers
            )
            return True, None
        except:
            return False, "while following"








ascii = r'''
 _    _ _______ __   _  _____  _______ _____ _     _
  \  /  |______ | \  | |     | |  |  |   |    \___/ 
   \/   |______ |  \_| |_____| |  |  | __|__ _/   \_
                                                            '''



banner = r"""
        _.---**""**-.       
._   .-'           /|`.     
 \`.'             / |  `.   
  V              (  ;    \  
  L       _.-  -. `'      \ 
 / `-. _.'       \         ;
:            __   ;    _   |
:`-.___.+-*"': `  ;  .' `. |
|`-/     `--*'   /  /  /`.\|
: :              \    :`.| ;
| |   .           ;/ .' ' / 
: :  / `             :__.'  
 \`._.-'       /     |      
  : )         :      ;      
  :----.._    |     /       
 : .-.    `.       /        
  \     `._       /         
  /`-            /          
 :             .'           
  \ )       .-'             
   `-----*"'           """


banner = Add.Add(ascii, banner, center=True)


blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))

white = Col.white

def init():
    System.Clear()
    System.Title('Venomix')
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner))) 
    print()
    print(f" {Col.Symbol('-_-', purple, Col.dark_gray)} {purple}Venomix{Col.dark_gray}  The {purple}best tools{Col.dark_gray} to upgrade your {purple}Spotify Playlist{Col.reset} ")
    print()
    print(f" {Col.Symbol('<3', purple, Col.dark_gray)} {Col.dark_gray}Go to {purple}github.com/ZeusFuckYou/Venomix{Col.dark_gray} to download this tool{purple} !{Col.reset} ")
    print('\n')
    



init() 
spotify_profile = str(input(f"\n {Col.Symbol('?', purple, Col.dark_gray)} {white}Enter the{purple} playlist id {white}-> {purple}"))
print('')
threads = int(input(f" {Col.Symbol('?', purple, Col.dark_gray)} {white}Enter the{purple} threads {purple}({white} max 10000 {purple}){white} -> {Col.reset}"))
print('')
print(f' [{purple}1{white}] {purple}Proxies\n {white}[{purple}2{white}] {purple}Proxyless{Col.reset}')
print("")
option = int(input(f" {Col.Symbol('?', purple, Col.light_gray)} {white}Choice {purple}->{Col.reset} "))

def load_proxies():
  if not os.path.exists("proxies.txt"):
      print(f"\n {Col.Symbol('!', purple, Col.dark_gray)} {white}File {purple}proxies.txt {white}not found{Col.reset}")
      time.sleep(3)
      exit()
  with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print(f"\n {Col.Symbol('!', purple, Col.dark_gray)} {white}No {purple}proxies {white}loaded in {purple}proxies.txt{Col.reset}")
            time.sleep(3)
            exit()

if option == 1:
    load_proxies()
    os.system('cls')
    init()
    print(f" {Col.Symbol('+', purple, Col.light_gray)} {purple}Loading...")

if option == 2:
  print(f"\n {Col.Symbol('!', purple, Col.light_gray)} {white}This option is not {purple}available{white} for the moment")
  time.sleep(5)
  exit()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        System.Title(f"Venomix / Like : {counter}")
        print(f"\n {white}Liked {purple}{counter}{white} -> ( {purple}{spotify_profile} {white})")
    else:
        System.Title(f"Venomix / Like : {counter}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter:
            proxy_counter = 0