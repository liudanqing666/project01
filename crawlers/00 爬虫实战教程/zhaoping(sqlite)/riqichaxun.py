# -*- coding: utf-8 -*-

from sqlite3 import connect

print("---------------------------------------------------------")
print("如果数据库中没有这个日期的职位信息，是不会有输出的！")
print("日期的输入格式范例：2016-07-29")
riqi = input("请输入你想要查看的日期：")
print("---------------------------------------------------------")

conn = connect('infodb')
curs = conn.cursor()
cmd = 'select * from Zhaoping where dates = "%s"' % riqi
curs.execute(cmd)

print("---------------------------------------------------------")
print("%-8s%-8s%-11s%-8s%-50s\n" % ("地点", "分类", "发布日期", "招聘人数", "职位"))
for row in curs.fetchall():
	print("%-8s%-8s%-16s%-8s%-50s\n" % (row[3], row[1], row[4], row[2], row[0]))

conn.commit()
conn.close()