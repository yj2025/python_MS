# urllib3: HTTP 요청을 보내기 위한 라이브러리
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

http = urllib3.PoolManager()    # HTTP 요청 처리
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
            # [END] 태그가 포함되어 있으면 제거
            if '[END]' in answer:
                answer = answer[:answer.index('[END]')]

            # passage 에서 실제 답변을 다시 가져오기
            answer = passage[passage.index(answer): passage.index('[END]', passage.index(answer))]
            return answer

    josa = ''
    return '"' + q + '"' + josa + '라는 문장은 아직 제대로 이해하지 못했습니다. 이 사항은 챗봇 응답에 추가될 예정입니다.'

# 1. ETRI API 사용 설정
#    -ETRI의 AI API를 사용해 질의응답을 처리함.
#    -API 키를 설정하고 HTTP 요청을 보낼 준비를 함.

# 2. 질문 분석 및 요청 생성
#    -Okt를 이용해 입력 문장을 정규화하고 명사를 추출.
#    -명사가 포함된 경우, 질문을 ETRI API에 JSON 형식으로 전송.

# 3. API 응답 처리
#    -API로부터 신뢰도(confidence)가 0.10 이상인 경우, 답변을 추출.
#    -[END] 태그가 포함된 경우 이를 제거하고 최종 응답을 반환.
