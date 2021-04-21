import mysql.connector
import time
import re

##判断表是否存在
def table_exists(con,table_name):
    sql = "show tables;"
    con.execute(sql)
    tables = [con.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return 1
    else:
        return 0
##创建数据表
def creat_database():
    global db
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    print("检测有无目标数据表存在...")
    time.sleep(0.3)
    if(table_exists(cursor,'information') == 0):
        # 创建数据表SQL语句
        sql = """CREATE TABLE information (
         name  VARCHAR(50) NOT NULL ,
         number VARCHAR(20), 
         cla VARCHAR(20),
         sex VARCHAR(20),
         age VARCHAR(20))default charset=utf8"""
        cursor.execute(sql)
        print("不存在，已为你自动创建")
    else:
        print("已存在,可直接写入至数据表")

##查询数据
def find_data(data):
    value = "'"+data+"'"
    sql = "SELECT * FROM information WHERE number = %s" %(value)
    cursor = db.cursor()
    # print(data)
    # print(type(data))
    # print(sql)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
       # 执行sql语句
        # print(list(results[0]))
        # print(len(results))
        if len(results): 
            print("信息存在")
            return 1
        else:
            print("信息不存在")
            return 0
    except:
       # Rollback in case there is any error
       print("error")

##添加数据
def add_data(name,number,cla,sex,age):
    cursor = db.cursor()
    values = (name,number,cla,sex,age)
    sql = "INSERT INTO information (name,number,cla,sex,age) VALUES "+str(values)
    try:
       # 执行sql语句
       cursor.execute(sql)# 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
db = mysql.connector.connect(host='localhost',port=3306,user='root',passwd='123456',database='face')
if(db):
    print("数据库连接成功")
    # creat_database()
# name = '杨耀威'
# number = '20171008184'
# cla = '1'
# sex = '男'
# age = '22'
# if find_data(number):
#     tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
# else:
#     tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     add_data(name,number,cla,sex,age)
# t = find_data('123')[1]
# print(t)