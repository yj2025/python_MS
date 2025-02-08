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

app = Flask(__name__)
board = []

@app.route('/')
def index():
    return render_template('main.html', rows=board, qnas=chatbot.src)

@app.route('/question', methods=["POST"])
def question():
    if request.method == "POST":
        board.append([request.form["context"], chatbot.action(request.form["context"])])
        return redirect(url_for("index"))
    else:
        return render_template("main.html", rows=board, qnas=chatbot.src)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8888)