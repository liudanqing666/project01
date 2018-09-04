# -*- coding: utf-8 -*-

from sqlite3 import connect

print("---------------------------------------------------------")
print("如果数据库中没有这个类型的职位信息，是不会有输出的！")
leixing = input("请输入你想要查看的职位类型：")
print("---------------------------------------------------------")

conn = connect('infodb')
curs = conn.cursor()
cmd = 'select * from Zhaoping where catalog = "%s"' % leixing
curs.execute(cmd)

print("---------------------------------------------------------")
print("%-8s%-8s%-11s%-8s%-50s\n" % ("地点", "分类", "发布日期", "招聘人数", "职位"))
for row in curs.fetchall():
	print("%-8s%-8s%-16s%-8s%-50s\n" % (row[3], row[1], row[4], row[2], row[0]))

# 如果我们对数据库做了除了查询之外的操作，我们需要commit，让这些操作对数据库生效
conn.commit()
conn.close()