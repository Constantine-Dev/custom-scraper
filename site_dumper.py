import re, os, io, sys, json, requests, datetime
from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup

API = {
    'user': 'https://www.mpweekly.com/culture/wp-json/wp/v2/usres/',
    'pages': 'https://www.mpweekly.com/culture/wp-json/wp/v2/posts/',
    # 'taxonomy': 'https://www.inmediahk.net/taxonomy/term/5030?page=',
    # 'sports': 'https://www.inmediahk.net/sports?page=',
    # 'socialnews_pj': 'https://www.inmediahk.net/taxonomy/term/530876?page=',
    'node': 'https://www.inmediahk.net/node/',  # 1080670
    # 'articles-by-date': 'https://www.inmediahk.net/articles-by-date/all/' # '12/27/2021'
}

APILIST = list(API)

payload = {}
headers = {
    'Accept': 'application/json',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
	'Connection': 'keep-alive'
}

download_dir = 'resultes'
com_dir = 'mpweekly'

for ops_num in range(0, int(len(API))):
    print(str(ops_num) + '. ' + APILIST[int(ops_num)])
options_num = input('Select the options by No. 0-00: ')
selected_API = APILIST[int(options_num)]

def file_set():
    for num in range(0, int(len(APILIST))):
        API_NAME = APILIST[int(num)]
        
        for API_NAME in APILIST:
            listDir = os.listdir('.')
            if download_dir in listDir:
                list2 = os.listdir(download_dir + '/')
                if com_dir in list2:
                    folder_check = os.listdir(download_dir + '/' + com_dir + '/')
                    if str(API_NAME) in folder_check:
                        pass
                    else:
                        path = os.path.join(download_dir + '/' + com_dir + '/', str(API_NAME))
                        os.mkdir(path)
                else:
                    office_path = os.path.join(download_dir + '/', com_dir + '/')
                    os.mkdir(office_path)
                    path = os.path.join(download_dir + '/' + com_dir + '/', str(API_NAME))
                    os.mkdir(path)
            else:
                os.mkdir(download_dir)
                office_path = os.path.join(download_dir + '/', com_dir + '/')
                os.mkdir(office_path)
                path = os.path.join(download_dir + '/' + com_dir + '/', str(API_NAME))
                os.mkdir(path)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def main():
    for APIS in API:
        timer = datetime.now()
        DateTime = timer.strftime('_%Y-%m-%d_%H-%M-%S_')
        SavDir = download_dir + '/'+ com_dir +'/' + APIS + '/'
            
        if APIS == str(selected_API):
            if APIS == 'articles-by-date':
                day_delta = timedelta(days=1)
                start_date = date(2004, 10, 11)
                end_date = date.today()

                for single_date in range((end_date - start_date).days):
                    date_count = start_date + single_date*day_delta
                    FileName = APIS + str(DateTime) + str(date_count.strftime('_%m-%d-%Y'))
                    responser = requests.get(API[str(APIS)] + str(date_count.strftime("%m/%d/%Y")), headers=headers, data=payload)
                    if responser.status_code == 200:
                        # wf = open(SavDir + FileName + '.html', 'w', encoding='utf-8')
                        # wf.writelines(responser.text)
                        # wf.close()
                        responser.close()
                        print(str(SavDir) + str(FileName) + '.html <= Saved! stCODE: [' + str(responser.status_code) + '] IDs: ' + str(date_count.strftime("%m/%d/%Y")))
                    else:
                        responser.close()
                        print('Target ' + APIS + ' ID not Load!=> ' + str(date_count.strftime("%m/%d/%Y")) + ' stCODE: [' + str(responser.status_code) + ']')
                        pass
            else:
                start_page = input('Start Page of <' + APIS + '> Num +1[int only]: ')
                end_page = input('End Page of <' + APIS + '> Num +1[int only]: ')
                for obj_num in range(int(start_page), int(end_page)):
                    FileName = APIS + str(DateTime) + str(obj_num)
                    responser = requests.get(API[str(APIS)] + str(obj_num), headers=headers, data=payload)
                    if responser.status_code == 200:
                        wf = open(SavDir + FileName + '.json', 'w', encoding='utf-8')
                        wf.writelines(responser.text)
                        wf.close()
                        responser.close()
                        print(str(SavDir) + str(FileName) + '.json <= Saved! stCODE: [' + str(responser.status_code) + '] IDs: ' + str(obj_num))
                    else:
                        responser.close()
                        print('Target ' + APIS + ' ID not Load!=> ' + str(obj_num) + ' stCODE: [' + str(responser.status_code) + ']')
                        pass

        else:
            pass

if __name__ == '__main__':
    file_set()
    main()
