import requests
import pandas as pd
import json
import datetime
from slacker import Slacker
# open API 가 호출되는 url
url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"

today =datetime.datetime.now()
d1 = today.strftime("%Y-%m-%d")
d1

now = datetime.datetime.now()
d2 = now.strftime('%Y-%m-%d %H:%M:%S')
d2
# 3개의 파라미터 값
param = {
    'authkey' : '본인의 토큰값',
    'searchdate' : str(d1),
    'data' : 'AP01'
}

# json 형식으로 확인
req = requests.get(url, param)
json_data = req.json()
json_data

# json에서 미국 달러 부분만 추출(미국달러는 22번째)
json_dollar = json_data[22]
json_dollar

# json 에서 미국 달러의 거래금액만 추출
exhange_dollar = json_dollar.get('deal_bas_r')
exhange_dollar
# json 에서 데이터 조회 결과 반환. (1: 성공, 2: 데이터 코드 오류, 3: 인증코드 오류, 4: 일일 제한횟수 1000회 마감)

req_result = json_dollar.get('result')
req_result

# 슬랙봇으로 실시간 환율 전송하기
import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

myToken = "xoxb-2325432872545-2341172726128-e9X9XWoFAbjsAUcXZA7LlV7m"

post_message(myToken,"#dollar", '현재 달러: ' +exhange_dollar + '\n현재 시각: ' + d2)



# 판다스의 dataframe 형식으로 확인
data_frame = pd.DataFrame(json_data)
data_frame

# 복수의 컬럼 데이터를 추출하는 경우에는 대괄호를 두 번 사용
frame_all = data_frame[['cur_unit', 'deal_bas_r']]
frame_all

frame_dollar = frame_all.loc[22]
frame_dollar
