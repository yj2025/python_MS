# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    "Chatpot",
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)

trainer = ListTrainer(chatbot)
trainer.train([
    "채용정보 알려줘",
    "사람인 : https://www.saramin.co.kr/zf_user/?srsltid=AfmBOopSA89ZwyeaMQKTA-UqlxWA3brKPJxvZl8uTGqAdrXtSaJszvFH",
    "잡코리아 : https://www.jobkorea.co.kr/?utm_source=google&utm_medium=cpc&utm_campaign=pc_%eb%b8%8c%eb%9e%9c%eb%93%9c_tcpa&utm_content=pc_%EB%B8%8C%EB%9E%9C%EB%93%9C_tcpa_%EC%9E%A1%EC%BD%94%EB%A6%AC%EC%95%841%EC%9C%84&utm_term=%EC%9E%A1%20%EC%BD%94%EB%A6%AC%EC%95%84&gad_source=1&gclid=CjwKCAiAnpy9BhAkEiwA-P8N4pcHZHI4jjkQuJMhJb_7TWbOsJ4ALnaTcF64z0w8ogM6B93nTHcjzRoCAf4QAvD_BwE",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        if response.confidence < 0.5:  # 신뢰도가 낮으면
            print("bot : 잘 모르겠어요. 다른 질문을 해 주세요.")
        else:
            # 응답을 개행 문자로 분리하여 출력
            print(f"bot : {response}")


