# 이름(name), 전화번호(tel) 필드와 생성자 등을 가진 Phone 클래스를 작성하고, 실행 예시와 같이 작동하는 PhoneBook클래스를 작성하라.
class PhoneBook:
    def __init__(self):
        self.add_phone = {}     # 딕셔너리 형태로 저장
        while True:
            try:
                self.member = input("인원수: ")
                for i in range(int(self.member)):  # 인원수 입력 후 반복
                    name, tel = input("이름과 전화번호(이름과 전화번호는 빈칸 없이 입력): ").split(' ')
                    self.add_phone[name] = tel      # name을 키로, tel를 값으로 저장
                print("저장되었습니다...")  # 오류 없이 입력이 완료되었을 때 출력
                break  # 정상 입력 완료 후 while문 종료
            except ValueError:
                print("잘못된 입력입니다. 다시 입력하세요")

    def search(self):
        while True:
            search_name = input("검색할 이름을 입력하세요\n")
            if search_name == "그만":
                break
            if search_name in self.add_phone:
                print(f"{search_name}의 번호는 {self.add_phone[search_name]}입니다.")
            else:
                print(f"{search_name}이 없습니다.")

phonebook = PhoneBook()
phonebook.search()