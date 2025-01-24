import threading
import time
import pyautogui

def print_numbers():
    for i in range(1, 11):
        time.sleep(1)   # 1초 동안 다른 쓰레드를 돌려라
        print(i)

thread_gui = threading.Thread(target=print_numbers)
thread_gui.start()

pyautogui.alert('코딩 유치원 자주 찾아주세요.')
print_numbers()

# 모든 프로그램이 쓰레드 기반인 증거
print('쓰레드 확인',threading.current_thread().name)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

# print_numbers()
# print_letters()

# 파라미터가 있는 함수
def first_thread(num,num2):
    for i in range(num +num2):
        print("음성나오기") #음성

def second_thread(num,num2):
    for i in range(num + num2):
        print("비디오나오기") #비디오


thread_first = threading.Thread(target=first_thread, args=(1,100))
thread_second = threading.Thread(target=second_thread, args=(1,100))

# thread_first.start()
# thread_second.start()

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# thread1.start()
# thread2.start()

