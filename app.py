import datetime
import requests
import bs4

현재 = str(datetime.datetime.now())
print(현재)
날 = 현재[0:4] + 현재[5:7] + 현재[8:10]


html = requests.get('http://school.cbe.go.kr/yullyang-e/M01030501/list?ymd='+날)


수프 = bs4.BeautifulSoup(html.text, 'html.parser')


트롤 = 수프.find('a', href ="/yullyang-e/M01030501/list?ymd="+날)
식단리스트 = 트롤.find_all('li')

식단 = ''
for i in 식단리스트:
    식단 = 식단 + i.text + '\n'

if 식단 == '':
    식단 = '오늘은 급식이 없네요!'
    
import telegram
토큰 = '1248510701:AAEQGWaZ5N0O85eDs42wRJj83Draph4_YVk'
봇 = telegram.Bot(token=토큰)
    
봇.sendMessage('1431249288','오늘의 식단을 알려줄게요!')
봇.sendMessage('1431249288',식단)
