import urllib3, json
from konlpy.tag import Okt

# API 키 입력
openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"     #  ETRI의 API에 요청
accessKey = "81319711-16d7-47a0-a339-5880a0b3f13e"  

# info.txt 파일 경로 확인 후 파일 읽기
try:
    src = open('info.txt', 'r', encoding='utf-8').readlines()
    passage = ''.join(src)
except FileNotFoundError:
    print("info.txt 파일을 찾을 수 없습니다.")
    passage = ''

http = urllib3.PoolManager()
okt = Okt()     # (Open Korea Text)

def action(q):
    q = okt.normalize(q)    #  정규화

    if len(okt.nouns(q)):
        requestJson = {"argument": {"question": q, "passage": passage}}
        response = http.request("POST", openApiURL,
                                headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": accessKey},
                                body=json.dumps(requestJson))
        
        # 서버로부터 받은 응답을 JSON 형식으로 변환
        response = json.loads(str(response.data, "utf-8"))

        # 서버에서 응답한 데이터 중 'confidence' 값 확인   ->   신뢰도가 0.10보다 높으면 그에 해당하는 답변 생성
        if float(response['return_object']['MRCInfo']['confidence']) > 0.10:
            answer = response['return_object']['MRCInfo']['answer'] #  실제 답변을 받아오기
            if '[END]' in answer:
                answer = answer[:answer.index('[END]')]

            answer = passage[passage.index(answer): passage.index('[END]', passage.index(answer))]
            return answer

    josa = ''
    return '"' + q + '"' + josa + '라는 문장은 아직 제대로 이해하지 못했습니다. 이 사항은 챗봇 응답에 추가될 예정입니다.'
