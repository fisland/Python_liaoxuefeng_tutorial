import pymysql
connect = pymysql.Connect(
    user = 'root',
    password = 'Zjf9437879228.',
    db = 'test_py',
    charset = 'utf8'
)

cursor = connect.cursor()
# ''' 插入
# cursor.execute('create table person (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into person (id, name) values (%s, %s)', ['2', 'Ken'])
# cursor.execute('insert into person (id, name) values (%s, %s)', ['3', 'Peter'])

# connect.commit()
# connect.close()

print('ok')
# '''

# 查询
cursor.execute('select * from person')
values = cursor.fetchall()
print(values)

cursor.close()
connect.close()

