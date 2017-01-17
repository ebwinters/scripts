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

def refineSearch(muscleName, equipmentName):
	ex = []
	muscleName = ' ' + muscleName + ' '
	c.execute("select * from exercises where muscle=(?)", (muscleName,))
	ex = c.fetchall()
	for e in ex:
		e[0].strip()
		e[1].strip()
		e[2].strip()
	for e1 in ex:
		if e[2] == equipmentName:
			print (e[0])



