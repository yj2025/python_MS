# # 이름(name), 전화번호(tel) 필드와 생성자 등을 가진 Phone 클래스를 작성하고, 실행 예시와 같이 작동하는 PhoneBook클래스를 작성하라.
# class PhoneBook:
#     def __init__(self):
#         self.add_phone = {}     # 딕셔너리 형태로 저장
#         while True:
#             try:
#                 self.member = input("인원수: ")
#                 for i in range(int(self.member)):  # 인원수 입력 후 반복
#                     name, tel = input("이름과 전화번호(이름과 전화번호는 빈칸 없이 입력): ").split(' ')
#                     self.add_phone[name] = tel      # name을 키로, tel를 값으로 저장
#                 print("저장되었습니다...")  # 오류 없이 입력이 완료되었을 때 출력
#                 break  # 정상 입력 완료 후 while문 종료
#             except ValueError:
#                 print("잘못된 입력입니다. 다시 입력하세요")
#
#     def search(self):
#         while True:
#             search_name = input("검색할 이름을 입력하세요\n")
#             if search_name == "그만":
#                 break
#             if search_name in self.add_phone:
#                 print(f"{search_name}의 번호는 {self.add_phone[search_name]}입니다.")
#             else:
#                 print(f"{search_name}이 없습니다.")
#
# phonebook = PhoneBook()
# phonebook.search()

class Phone:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def set_name(self, name):
        self.name = name

    def set_tel(self, tel):
        self.tel = tel


class PhoneBook:
    def __init__(self):
        self.phone_list_max = None
        self.phone_list = []

    def add(self, name, tel):
        self.phone_list.append(Phone(name, tel))

    def input_persons(self):
        while True:
            try:
                self.phone_list_max = int(input("인원수 >> "))
                break
            except:
                print("잘못된 입력입니다. 인원수를 숫자로 입력해주세요요")
                continue

    def input_phone(self):
        is_done = False
        while True:
            try:

                for i in range(self.phone_list_max):
                    tel_name = input("이름과 전화번호 입력(빈 칸은 종료) >> ")
                    tel_name = tel_name.split(" ")
                    self.add(tel_name[0], tel_name[1])

                is_done = True
            except:
                print("잘못된 입력입니다. 처음부터 다시 입력해주세요.")
                continue

            if is_done:
                break

        print("저장되었습니다...")

    def phone_search(self):
        while True:
            try:
                name = input("검색할 이름 입력 >> ")

                if name == "그만":
                    break

                # 리스트 컴프리 헨션을 응용해서 찾기   # 중복(같은 이름)
                searched_list = [phone for phone in self.phone_list if phone.name == name]

                if len(searched_list) == 0:
                    print("찾는 이름이 없습니다.")
                else:
                    for phone in searched_list:
                        print(phone.name, phone.tel)


            except:
                print("잘못된 입력입니다. 처음부터 다시 입력해주세요.")
                continue

    def run(self):
        self.input_persons()
        self.input_phone()
        self.phone_search()


phone_book = PhoneBook()
phone_book.run()
