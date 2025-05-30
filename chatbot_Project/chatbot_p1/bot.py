# bot.py
# Python 3.6.5  -> 상위 time.clock() 삭제
# terminal) python bot.py  --실행

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer # 챗봇을 리스트 형태의 데이터로 학습

chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)

# 규칙 기반 (미리 정의된 질문-응답 쌍 데이터 학습)
trainer.train([
    "안녕하세요",
    "반갑습니다. 저는 채용 공고 사이트를 알려드릴 수 있습니다.",
])

trainer.train([
    "채용 공고 사이트 알려줘",
    "사람인: https://www.saramin.co.kr 잡코리아: https://www.jobkorea.co.kr 원티드: https://www.wanted.co.kr",
])

exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"bot : {chatbot.get_response(query)}")