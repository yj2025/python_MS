# api key : 4da9533d78f44fe23b6fe73a2395beca
from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1
# span - item_title
results = soup.findAll('span','item-title')

search_rank_file = open("rankresult.txt","a")

print(response.txt)

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1