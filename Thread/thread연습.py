import threading

class NumbersThread(threading.Thread):
    def __init__(self,num1,num2):
        super().__init__()
        self.num1 = num1
        self.num2 = num2

    def run(self):
        for i in range(self.num1 + self.num2):
            print(i)

class LettersThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for letter in 'abcdefghij':
            print(letter)

numbers_thread = NumbersThread(1, 100)
letters_thread = LettersThread()

numbers_thread.start()
letters_thread.start()