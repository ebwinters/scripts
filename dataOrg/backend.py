import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def searchMuscleName(muscleName):
	ex = []
	muscleName = ' ' + muscleName + ' '
	c.execute("select * from exercises where muscle=(?)", (muscleName,))
	ex = c.fetchall()
	for e in ex:
		print (e[0].strip())

def searchEquipmentName(equipmentName):
	ex = []
	equipmentName = ' ' + equipmentName + ' '
	c.execute("select * from exercises where equipment=(?)", (equipmentName,))
	ex = c.fetchall()
	for e in ex:
		print (e[0].strip())


