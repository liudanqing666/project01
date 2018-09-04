# -*- coding: utf-8 -*-

print("---------------------------------------------------------")
print("这个程序可以根据地名、职位类型或者日期来检索职位信息哦！")
reply = input("你想使用哪种方式进行查询呢？1：职位类型，2：地点，3：日期")

if int(reply) == 1:
	import fenleichaxun
elif int(reply) == 2:
	import didianchaxun
elif int(reply) == 3:
	import riqichaxun
else:
	print("输入值不符合要求！")