import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    host='localhost',   # MySQL 서버 주소
    user='scott',       # 사용자 이름
    password='tiger',
    db='scott',
    charset='utf8')     # 문자 인코딩

# Connection으로부터 Cursor 생성
# cursor 객체 생성 => 커서 객체의 역활은 sql 문장을 실행하고 결과를 가져오는 역할
curs = conn.cursor()

# SQL문 실행 (dept 테이블 조회)
sql = "SELECT * FROM dept;"
curs.execute(sql)

# 데이터 Fetch
rows = curs.fetchall()
print(rows) # 전체 rows

for row in rows:
    print(row)

# 테이블 생성
sql = 'CREATE TABLE users (id char(4), name char(15), email char(20))'
curs.execute(sql)

# 데이터 삽입
sql = "insert into users values ('1', '홍길동', 'hong@gmail.com')"
curs.execute(sql)

sql = "insert into users values ('2', '김길동', 'kim@gmail.com')"
curs.execute(sql)

conn.commit() # 영구 저장

# Connetcion 닫기
conn.close()