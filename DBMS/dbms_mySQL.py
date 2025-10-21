# dbms_mySQL.py

import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host = "localhost",      # MySQL 서버 주소(ip)
    user = "root",           # 사용자명 (기본 = root)
    password = "1234",
    database = "exampledb",
    charset = "utf8mb4",      # 인코딩 정보 (UTF-8 확장버전)   
    cursorclass = pymysql.cursors.DictCursor
)

# 커서 생성 => 명령어 작성가능
cursor = conn.cursor()

# 명령어 실행
cursor.execute("SELECT DATABASE()")
# 한번 호출에 하나의 Row를 가져올 때 사용
print(f"현재 데이터 베이스 : {cursor.fetchone()}")      # 하나의 데이터만 추출
# print(f"현재 데이터 베이스 : {cursor.fetchall()}")    # 모든 데이터 추출
# print(f"현재 데이터 베이스 : {cursor.fetchmany(2)}")  # ()안의 숫자에 갯수만큼 데이터 추출

# 연결 해제
conn.close()

