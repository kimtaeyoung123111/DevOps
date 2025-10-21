# dbms_mySQL _insert.py

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
sql = """ INSERT INTO employees(ID,name,deptID,managerID)
VALUES(106,"TAEYOUNG",8,101)"""

cursor.execute(sql)

# sql = """ INSERT INTO employees(ID,name,deptID,managerID)
# VALUES(%s,%s,%s,%s)"""
# cursor.execute(sql,(106,'TAEYOUNG',8,101))

conn.commit()

print("데이터 삽입 완료")

# 연결 해제
conn.close()

