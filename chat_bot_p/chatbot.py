import urllib3, json
from konlpy.tag import Okt

# 실제 API 키 입력
openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "81319711-16d7-47a0-a339-5880a0b3f13e"  # 여기에 실제 키 입력

# info.txt 파일 경로 확인 후 파일 읽기
try:
    src = open('info.txt', 'r', encoding='utf-8').readlines()
    passage = ''.join(src)
except FileNotFoundError:
    print("info.txt 파일을 찾을 수 없습니다.")
    passage = ''

http = urllib3.PoolManager()
okt = Okt()

def action(q):
    q = okt.normalize(q)

    if len(okt.nouns(q)):
        requestJson = {"argument": {"question": q, "passage": passage}}
        response = http.request("POST", openApiURL,
                                headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": accessKey},
                                body=json.dumps(requestJson))
        response = json.loads(str(response.data, "utf-8"))

        if float(response['return_object']['MRCInfo']['confidence']) > 0.10:
            answer = response['return_object']['MRCInfo']['answer']
            if '[END]' in answer:
                answer = answer[:answer.index('[END]')]

            answer = passage[passage.index(answer): passage.index('[END]', passage.index(answer))]
            return answer

    josa = ''
    return '"' + q + '"' + josa + '라는 문장은 아직 제대로 이해하지 못했습니다. 이 사항은 챗봇 응답에 추가될 예정입니다.'
