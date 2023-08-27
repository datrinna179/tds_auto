import os, uuid, json, requests, time
from datetime import datetime
try:
    import requests
    from selenium import webdriver
    from pynput import keyboard#thêm thư viện
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from onest_captcha import OneStCaptchaClient
except: 
    os.system("pip install selenium")
    os.system("pip install 1stcaptcha")
    os.system("pip install requests")
    os.system("pip install pynput")
from selenium import webdriver
from pynput import keyboard#thêm thư viện
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from onest_captcha import OneStCaptchaClient
import threading
import requests

class show_info: #show tên luồng
    Name = ''
    IsStop = False
    def __init__(self, Name,):
        self.Name = Name
        self.IsStop = False
#mới add vô, phần này để nhập luồng
sleepTime = 3
tools = []
i = 1
index = 0
TDS_token = []
password = []
#class để nhập luồng
class nhap_luong:
    nhap_so_luong = int(input("Nhập số luồng: "))
    while i <= nhap_so_luong:
        tools.append(show_info(f"Luồng {i}"))
        i += 1
    listen = keyboard.Listener 
    # đọc file
file_object = open('information.txt','r+')
with open('information.txt') as rf:
    try:
        mylist = rf.read().splitlines()
        if 'information.txt' != '':
            while index < len(mylist):
                a = mylist[index]
                TDS_list = a.split("|", 2)
                TDS_token.append(TDS_list[0])
                password.append(TDS_list[1])
                index += 1
        else:
            print("vui lòng kiểm tra lại file backup TDS !")
            exit()
    except:
        file_object.close()
print(TDS_token)
print(password)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
options.add_argument("--window-size=500,800")
options.add_argument("--mute-audio")

APIKEY = "88302c3ea2b84472869247edccacfd29"
client = OneStCaptchaClient(apikey=APIKEY)

site_key = "6LeGw7IZAAAAAECJDwOUXcriH8HNN7_rkJRZYF8a"
url = "https://traodoisub.com/view/cauhinh/"

today = datetime.today()
ngay = today.day
thang = today.day
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

type_job = "like"
type_nhan = "LIKE"

headers = {
    'authority': 'traodoisub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'user-agent': 'traodoisub tiktok tool',
}

class Pro5_Config:
    def __init__(self, cookies,fb_dtsg,jazoet,id_page) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        self.fb_dtsg = fb_dtsg
        self.jazoet = jazoet
        self.user_id = id_page
        
    def Like(self, id, reaction):
        if '_' in id:
            uid = id.split('_')[1]
        else:
            uid = id
            
        try:
            url = requests.get(f'https://www.facebook.com/{uid}', headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reaction+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }
            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return True
        except:
            return False 
        
    def Follow(self, uid):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+uid+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '5032256523527306',
        }
        try:
            follow = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return follow
        except:
            return False
        
    def Page(self,uid):
        data = {
            'av':self.user_id,
            '__user':self.user_id,
            '__a':'1','__dyn':'7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyU8EW0CEboG4E762S1DwUx60gu0BU2_CxS320om78bbwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W2i4U72m7-8wywfCm2Sq2-azo2NwwwOg2cwMwhF8-4UdUcojxK2B0oobo8o','__csr':'g8JNc9n2tWr5W4til-I_On8J9rshlR8nZFiELH_Hnij4JfOJLOGiLoxLBlGRuZaGF4CZddQ4L_JfCiDKWVryuiqqFAcy8x6CBtqJkF8ZVExauAbgOtLAG5FUGFptxqfxi4Hzaz8CQ2SaxC9xCi48Wqqq11g8EaoS9g9U4m224oG68sGucx68wyg6G22mfxa4Xxq7EKbwi82LwNxu48c814EC2K3O5U-2WEhCxO1EwioeUiwiE6e3HwTw18C02k-0exw0deO0jV05Swe20bTw5_w1zF03I202po6e07Co0K6Zlw0jjo0E-0qW08ug8UhBw21e0fLw5Ww9K0Z86u','__req':'o','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006793331','__s':'v80lqo:poayhk:qxdcmk','__hsi':'7185553908092803679','__comet_req':'15','fb_dtsg':self.fb_dtsg,'jazoest':self.jazoet,'lsd':'V64c7kKr5hAtzX2IIDgKp8','__aaid':'775223720487728','__spin_r':'1006793331','__spin_b':'trunk','__spin_t':'1673017141','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometPageLikeCommitMutation','variables':'{"input":{"attribution_id_v2":"CometSinglePageHomeRoot.react,comet.page,via_cold_start,1673017144344,576155,250100865708545,","is_tracking_encrypted":true,"page_id":"'+uid+'","source":"unknown","tracking":[],"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"isAdminView":false}','server_timestamps':'true','doc_id':'5491200487600992',}
        try:
            page = requests.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data)
            if 'FOLLOW' in page.text:
                return True
            else:
                return page.text
        except:
            return False
    
def Config_Page(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    idpef = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}','doc_id': '5300338636681652'}).json()
    a = idpef['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
    sl = 0
    for b in a:
        sl +=1
        uid = b['profile']['id']
        name = b['profile']['name']
        delegate_page_id = b['profile']['delegate_page_id']
        # print (f" PAGE : {sl} | ID : {uid} | Name : {name} ")
    return a
def Get_Data(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoet = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    return json.dumps({'fb_dtsg':fb_dtsg,'jazoet':jazoet})

class TDS_Cofig:
    def __init__(self, token):
        self.TDS_token = token

    def Login_TDS(self):
        try:
            r = requests.get(f'https://traodoisub.com/api/?fields=profile&access_token={self.TDS_token}', headers=headers, timeout=5).json()
            if 'success' in r:
                print(f" Đăng nhập thành công!")
                time.sleep(1)
                os.system("cls")
                print('-'*60)
                print(f" Username: {r['data']['user']} | Xu hiện tại: {r['data']['xu']} Xu")
                return r
            else:
                print(" Token TDS không hợp lệ, hãy kiểm tra lại!\n")
                return 'error_token'
        except:
            return 'error'

    def Load_Job(self, type):
        try:
            load_job = requests.get(f"https://traodoisub.com/api/?fields={type}&access_token={self.TDS_token}", headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
            return load_job
        except:
            return False
        
    def Config(self, id, name):
        urlch = requests.get(f"https://traodoisub.com/api/?fields=run&id={id}&access_token={self.TDS_token}").json()
        try: 
            msg = urlch["data"]["msg"]
            print(f" Cấu Hình | ID : {id} | Name : {name} ")
        except:
            if 'error' in urlch:
                print(f" ID: {id} Chưa được cấu hình ")
                return False
            
    def Add_Clone(self, username, password, uid):
        print (f"Tiến hành cấu hình ID: {uid}")
        try:
            driver = webdriver.Chrome(options=options)
            driver.get('https://traodoisub.com/')
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="top"]/div/div[1]/nav/button').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="navbarVerticalCollapse"]/div/ul/li[3]/a').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="cauhinh"]/li[1]/a').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="idfb"]').send_keys(uid)

            print("Đang giải captcha")
            result = client.recaptcha_v2_task_proxyless(site_url=url, site_key=site_key, invisible=False)
            if result["code"] == 0:  # success:
                token = result["token"]
                captcha = driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
                driver.execute_script("arguments[0].setAttribute('style', '')",captcha)
                driver.execute_script(f"arguments[0].innerHTML='{token}'",captcha)

                driver.find_element(By.XPATH, '//*[@id="idfb"]').send_keys(Keys.ENTER)
            else:  # wrong
                print(result["messeage"])
            driver.quit()
            return True
        except:
            return False
            
    def Nhan_Xu(self, type, id):
        try:
            nhan_xu = requests.get(f"https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.TDS_token}", headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}).json()
            try:
                data = nhan_xu['data']
                xu = data['xu']
                msg = data['msg']
                return msg, xu
            except:
                return nhan_xu
        except:
            return False
            
class Run_tool:
    def Done_Job(job, id, type, msg, xu):
        uid = id.split('_')[1] if '_' in id else id
        time = datetime.now().strftime("%H:%M:%S")
        print(f'[{job}] | [{time}] | [{type}] | [{uid}] | [{msg}] | [{xu}]')

    def Error_Job(id, type):
        uid = id.split('_')[1] if '_' in id else id
        print(f'Đang Lỗi Gì Đó, Vui Lòng Chờ Đợi', end = '\r'); time.sleep(2); print('                                                   ', end = '\r')
                
    def Anti_Block(delaybl):
        for i in range(delaybl, -1, -1):
            print(f' Đang hoạt động chống block sẽ chạy lại sau {i} giây  ',end = '\r');time.sleep(1); print('                                                        ', end = '\r')
            
    def Rest(delay):
        for i in range(delay, -1, -1):
            time.sleep(1)     

def Main(TDS_token, password):
    os.system('cls')
    print("Thành công:") #thêm print
    job = 0
    bug = 0
    tds = TDS_Cofig(TDS_token) #bug
    info_account = tds.Login_TDS()
    with open("cookie.txt", "r+") as f:
        cookie = f.readline()
        if cookie.endswith("\n"):
            cookie = cookie[:-1]
        data = f.read()
        f.seek(0)
        f.write(data)
        f.truncate()
    
    print('-'*60)
    
    if cookie == "":
        print (" Cookie đã hết, vui lòng backup!")
        print('-'*60)
        exit()
        
        
    #### vào việc
    Page = Config_Page(cookie)
    # a = int(input(' \033[1;32mBạn Muốn Chạy Page Thứ Mấy : \033[1;33m'))
    # chon = a-1
    chon = 0
    delay = 5
    nvblock = 20
    delaybl = 200

    id_page = Page[chon]['profile']['id']
    name = Page[chon]['profile']['name']
    cookie_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
    data = Get_Data(cookie)
    fb_dtsg = json.loads(data)['fb_dtsg']
    jazoet = json.loads(data)['jazoet']
    pro5 = Pro5_Config(cookies=cookie_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
    tt = 0

    os.system('cls')
    username = info_account['data']['user']
    xu = info_account['data']['xu']
    print (f" Tài Khoản: {username} \n Xu Hiện Tại : {xu} ")

    print('-'*60)
    
    check = tds.Config(id_page, name)
    if check == False:
        os.system("cls")
        time.sleep(2)
        add = tds.Add_Clone(username, password, id_page)
        if add == True:
            print(" Đã add clone xong, tiến hành cấu hình clone")
            time.sleep(2)
            os.system("cls")
            check = tds.Config(id_page, name)
            
    print('-'*60)
    
    while True:
        list_job = tds.Load_Job(type_job)
        if list_job == False:
            print(' Không Get Được Nhiệm Vụ Like              ', end = '\r'); time.sleep(2); print('                                                        ', end = '\r')
        elif 'error' in list_job.text:
            if list_job.json()['error'] == ' Thao tác quá nhanh vui lòng chậm lại':
                print(f' Đang Get Nhiệm Vụ Like              ', end = '\r'); time.sleep(2); print('                                                       ', end = '\r')
            else:
                print(list_job.json()['error'] , end ='\r')
        else:
            list_job = list_job.json()
            if len(list_job) == 0:
                print(' Hết Nhiệm Vụ Like                             ', end = '\r');time.sleep(2); print('                                                        ', end = '\r')
            else:
                print(f' Tìm Thấy {len(list_job)} Nhiệm Vụ Like                       ', end = '\r')
                for x in list_job:
                    id = x['id']
                    like_id = "1635855486666999"
                    like = pro5.Like(id, like_id)
                    if like == False:
                        Run_tool.Error_Job(id, type_nhan)
                        bug += 1
                    else:
                        nhan = tds.Nhan_Xu(type_nhan, id)
                        try:
                            xu = nhan[1]
                            msg = nhan[0] 
                            job += 1
                            Run_tool.Done_Job(job, id, type_nhan, msg, xu)
                            bug = 0
                            if job % nvblock == 0:
                                Run_tool.Anti_Block(delaybl)
                            else:
                                Run_tool.Rest(delay)
                        except:
                            Run_tool.Error_Job(id, type_nhan)
                            bug += 1
                    
                    if bug >= 5:
                        if name == 0:
                            print(f' Cookie Tài Khoản {name} Đã Bị Out !!!                ')
                            print(" Vui lòng chờ 2s để add vào cookie mới")
                            time.sleep(2)
                            Main()
                        else:
                            print(f' Tài Khoản {name} Đã Bị Block Like !!!					')
                            print(" Vui lòng chờ 2s để add vào cookie mới")
                            time.sleep(2)
                            Main()
        # list_job = tds.Load_Job(type_job)
        # if list_job == False:
        #     print('Không Get Được Nhiệm Vụ Like Page                 ', end = '\r');time.sleep(2); print('                                                        ', end = '\r')
        #     list_job = []
        # elif 'error' in list_job.text:
        #     if list_job.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
        #         print(f'Đang Get Nhiệm Vụ Like Page                         ', end = '\r'); time.sleep(2); print('                                                       ', end = '\r')
        #     else:
        #         print(list_job.json()['error'] , end ='\r')
        #     list_job = []
        # else:
        #     list_job = list_job.json()
        #     if len(list_job) == 0:
        #         print('Hết Nhiệm Vụ Like Page                                 ', end = '\r');time.sleep(2); print('                                                        ', end = '\r')
        #     else:
        #         print(f'\033[1;32mTìm Thấy {len(list_job)} Nhiệm Vụ Like Page           ', end = '\r')
        #         for x in list_job:
        #             id = x['id']
        #             like_page = pro5.Page(id)
        #             if like_page == False:
        #                 Run_tool.Error_Job(id, type_nhan)
        #                 bug += 1
        #             else:
        #                 nhan = tds.Nhan_Xu(type_nhan, id)
        #                 try:
        #                     xu = nhan[1]
        #                     msg = nhan[0] 
        #                     job += 1
        #                     Run_tool.Done_Job(job, id, type_nhan, msg, xu)
        #                     bug = 0
        #                     if job % nvblock == 0:
        #                         Run_tool.Anti_Block(delaybl)
        #                     else:
        #                         Run_tool.Rest(delay)
        #                 except:
        #                     Run_tool.Error_Job(id, type_nhan)
        #                     bug += 1
        #             if bug >= 5:
        #                 if name == 0:
        #                     print(f'  Cookie Tài Khoản {name} Đã Bị Out !!!                ')
        #                     print("Vui lòng chờ 2s để add vào cookie mới")
        #                     time.sleep(2)
        #                     Main()
        #                 else:
        #                     print(f' Tài Khoản {name} Đã Bị Block Like Page !!!					')
        #                     print("Vui lòng chờ 2s để add vào cookie mới")
        #                     time.sleep(2)
        #                     Main()
class multithreading:
    def execute_python_file(profile):
        #dừng luồng
        if(profile.IsStop):
            print("{} Stop\n" .format(profile.Name))
            return
        #dừng tool sau khi nhấn phím 
        totalRunningThread = any(x.IsStop == False for x in tools)
        print("Total: {}\n".format(totalRunningThread))
        if(totalRunningThread == False):
            listen.stop()
    #nhấn phím để dừng luồng
    def on_press(key): # key: phim nhấn
        vk = key.vk if hasattr(key, 'vk') else key.value.vk 
        print('vk = ',vk)
        if(vk == None):
            return
        index = vk - 48
        if(index >=0 and index < len(tools) and tools[index].IsStop == False):
            print("Dừng luồng: {}".format(tools[index].Name))
            tools[index].IsStop = True 
    number_of_index = 0
    #chạy luồng
    if __name__ == "__main__":
        try:
            for item in tools:
                p = threading.Thread(target=Main, args=(TDS_token[number_of_index], password[number_of_index], ))
                p.start()
                time.sleep(sleepTime)
                number_of_index += 1
        except:
            print("Chạy không thành công, kiểm tra lại file backup !")
            exit()
        with keyboard.Listener(on_press=on_press) as listener:
            listen = listener
            listener.join()                          