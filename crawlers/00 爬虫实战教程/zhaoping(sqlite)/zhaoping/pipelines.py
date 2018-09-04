# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import sqlite3
import unicodedata

class ZhaopingPipeline(object):

	# 该函数用于处理抓取的items
	def process_item(self, item, spider):
		self.storeInDb(item)
		print('保存item'.center(50, '*'))
		# 下面的 return item 是没有用的，加上之后会在控制台上显示 item
		# return item

	def __init__(self):
		self.setupDBCon()
		self.createTables()
		print('数据库初始化完成'.center(50, '*'))

	# 连接到数据库
	def setupDBCon(self):
		self.con = sqlite3.connect('infodb') 
		self.cur = self.con.cursor()

	# 创建招聘信息表
	def createTables(self):
		self.dropZhaopingTable()
		self.createZhaopingTable()

	# 如果表已经存在，则删除存在的表
	def dropZhaopingTable(self):
		self.cur.execute("DROP TABLE IF EXISTS Zhaoping")

	# 创建招聘表
	def createZhaopingTable(self):
		self.cur.execute("create table Zhaoping (name char(50), catalog char(50), numbers char(2), location char(50), dates char(50))")

	# 将数据保存到数据库中
	def storeInDb(self,item):
		total = len(item.get('name', ''))
		for i in range(total):
			self.cur.execute("INSERT INTO Zhaoping(\
			    name, \
			    catalog, \
			    numbers, \
			    location, \
			    dates \
			    ) \
			VALUES( ?, ?, ?, ?, ?)", \
			( \
			    item.get('name','')[i],
			    item.get('catalog','')[i],
			    item.get('numbers','')[i],
			    item.get('location','')[i],
			    item.get('dates','')[i]
			))
			print('------------------------')
			print('数据成功保存到数据库中！')
			print('------------------------')
			self.con.commit()

	# 关闭数据库
	def closeDB(self):
		self.con.close()

	# 实例运行完毕后执行的操作：
	# 关闭数据库
	def __del__(self):
		self.closeDB()
