# -*- coding: utf-8 -*-

from pymysql import connect

print("---------------------------------------------------------")
print("如果数据库中没有这个地方的职位信息，是不会有输出的！")
didian = input("请输入你想要查看的地方：")
print("---------------------------------------------------------")

conn = connect(host='localhost', 
				user='root', 
				password='Cisc0123',
				db='crawl', 
				charset='utf8') 
curs = conn.cursor()
cmd = 'select * from Zhaoping where location = "%s"' % didian
curs.execute(cmd)

print("---------------------------------------------------------")
print("%-8s%-8s%-11s%-8s%-50s\n" % ("地点", "分类", "发布日期", "招聘人数", "职位"))
for row in curs.fetchall():
	print("%-8s%-8s%-16s%-8s%-50s\n" % (row[3], row[1], row[4], row[2], row[0]))

conn.commit()
conn.close()