import re, os, io, sys, json, sqlite3
from bs4 import BeautifulSoup, BeautifulStoneSoup

API = {
    'user': 'https://www.inmediahk.net/user/',
    'socialmovement': 'https://www.inmediahk.net/socialmovement?page=',
    'taxonomy': 'https://www.inmediahk.net/taxonomy/term/5030?page=',
    'community': 'https://www.inmediahk.net/community?page=',
    'world': 'https://www.inmediahk.net/world?page=',
    'conservation': 'https://www.inmediahk.net/conservation?page=',
    'media': 'https://www.inmediahk.net/media?page=',
    'lifestyle': 'https://www.inmediahk.net/lifestyle?page=',
    'animalrights': 'https://www.inmediahk.net/animalrights?page=',
    'culture': 'https://www.inmediahk.net/culture?page=',
    'sports': 'https://www.inmediahk.net/sports?page=',
    'socialnews_pj': 'https://www.inmediahk.net/taxonomy/term/530876?page=',
    'communitypost': 'https://www.inmediahk.net/communitypost?page=',
    'node': 'https://www.inmediahk.net/node/',  # 1080670
    'articles-by-date': 'https://www.inmediahk.net/articles-by-date/all/'  # '12/27/2021'

}

APILIST = list(API)

DataDir = 'resultes/'
office = 'inmediahk'
file = 'articles-by-date_2022-01-10_14-02-11__12-01-2004.html'

# for num in range(0, int(len(API))):
#     debug_res = str(num) + '. ' + APILIST[int(num)]
#     print(debug_res)
# options = input('Select options 0-9: ')
# ans = APILIST[int(options)]
# print('selected options: ' + ans)

set_dwn_lst = open(office + '_debug.json', 'w+', encoding="utf-8")
dum_da = {}  # "dumps": {}
json.dump(dum_da, set_dwn_lst, indent=4)
set_dwn_lst.close()


def write_json(new_data, filename=office + '_debug.json'):
    file = open(filename, 'r+')
    file_data = list(json.loads(str(file.read())))
    file_data.append(new_data)
    file.seek(0)
    json.dump(file_data, file, indent=4)
    file.close()

def pre_ops():
    pass

def main():
    rf = open(file, 'r')
    data = rf.read()
    rf.close()
    
    soup = BeautifulSoup(data, 'html.parser')
    
    #GET TARGET DIV
    target_div = soup.find('div', class_='a3-content')
    
    article_info = target_div.find_all(class_="article-info")
    soup_2 = BeautifulSoup(str(article_info), 'html.parser')
    
    for obj in soup_2:
        for num in range(0, int(len(obj))):
                    
            find_date = soup_2.find_all(class_='date')
            find_author = soup_2.find_all(class_='author')
            find_title = soup_2.find_all(class_='title')
            soup_3 = BeautifulSoup(str(find_title), 'html.parser')
            find_post_url = soup_3.find_all('a', href=True)
                                            
            date = find_date[num].text.strip()
            author = find_author[num].text.strip()
            title = find_title[num].text.strip()
            post_url = find_post_url[num]['href']
            video_url = None
                    
            jsonlys_data = {
                "date": date,
                "author": author,
                "title": title,
                "post_url": post_url
            }
            
            dump_jsonlys = json.dumps(jsonlys_data, indent=4)
                    
            json_dwn_data = { 
                "title": title,
                "post_url": post_url,
                "video_url": video_url
            }
            
        #WRITE TO JSON
        write_json(json.loads(dump_jsonlys))
            
    # print(target_div)
    # print(article_image)
    
    # print(photo_url)
    
if __name__ == '__main__':
    main()
