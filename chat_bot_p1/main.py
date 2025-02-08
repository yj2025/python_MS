  # konlpy 라이브러리 설치 한국어 자연어 처리를 위한 파이썬 라이브러리
# import sys
# import subprocess

# subprocess.check_call([sys.executable, "-m", "pip", "install", "konlpy"])


# main.py
# coding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import chatbot

# JVM 시작 (자신의 JDK 경로로 수정)
import jpype
# JVM이 이미 실행 중이 아니면 시작하도록 처리
if not jpype.isJVMStarted():
    jpype.startJVM(r"C:\Program Files\Java\jdk-21\bin\server\jvm.dll")

# 객체 생성
app = Flask(__name__)
board = []

# 특정 URL 경로에 대한 처리를 정의
@app.route('/')
def index():
    return render_template('main.html', rows=board, qnas=chatbot.src)

# POST 요청 처리
@app.route('/question', methods=["POST"])
def question():
    if request.method == "POST":
        board.append([request.form["context"], chatbot.action(request.form["context"])])
        return redirect(url_for("index"))
    else:
        return render_template("main.html", rows=board, qnas=chatbot.src)

# 실행
if __name__ == '__main__':
    app.run(
        host='0.0.0.0', # 모든 IP에서 접근 가능하도록 설정 (기본값 : '127.0.0.1'(localhost))
        debug=True,     # 디버그 모드 활성화 (코드 변경 시 자동 재시작, 에러 상세 출력)
        port=8888       # 8888번 포트에서 서버 실행 (기본값: 5000)
    )