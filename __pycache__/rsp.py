# 가위바위보 게임
import random

class RspGame:
    def __init__(self):
        # self.rsp_list = ['가위','바위','보']
        self.dic_rsp_result= {
            '가위':('바위',"승"),
            '바위':('보',"승"),
            '보':('가위',"승"),
        }

        self.computer = None #
        self.user = '' # 

    def set_rsp(self):
        while True:
            try:
                self.user = input("가위바위보를 입력하세요 : ")
                if self.user in self.dic_rsp_result.keys(): #self.rsp_list:
                    break
                print("잘못된 입력입니다. 가위바위보중 하나만 입력하세요 : ")

            except:
                print("잘못된 입력입니다. 가위바위보중 하나만 입력하세요 : ")
                continue

        self.computer = random.choice(list(self.dic_rsp_result.keys()))

    def rsp_result(self):
        if self.computer == self.user:
            return "비겼습니다."
        elif self.dic_rsp_result[self.computer][0] == self.user:
            return "유저 당신이 이겼습니다."
        else:
            return "유저 당신이 졌습니다."

    def run(self):
        while True:
            self.set_rsp()
            print("사용자 : ",self.user)
            print("컴퓨터 : ",self.computer)
            print(self.rsp_result())

            continue_yn = input("계속 하시겠습니까? (y/n) : ")

            if continue_yn.upper() not in ['Y', 'YES'] :
                break

rsp = RspGame()
rsp.run()