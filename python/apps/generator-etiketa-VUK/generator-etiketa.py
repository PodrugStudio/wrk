import csv
from datetime import date

order=["JA",2000,"06/2023",""]
Etiketa_Total = order[1];
KlijentID=order[0]
sad = date.today()
orderDateCode=sad.strftime("%y")+str(sad.month)


#read last line of orders and get details
def getLastPrintedNumber( newOrderID ):
	generirano=1
	with open('naruceno.csv', 'rt') as f:
		reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
		for row in reader:
			generirano = generirano + int(row[0])
	with open("naruceno.csv", "a") as f:
		f.write( "\n"+newOrderID )
	return generirano


#load client data
def loadClientData():
	with open('klijenti.csv', 'rt') as f:
	    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
	    for row in reader:
	        if (row[0] == KlijentID):
	        	KlijentData = row
	return KlijentData

#create and write file
def writeNewFile(orderFilename, brojac):
	with open(orderFilename+".txt", "w") as text_file:
		text_file.write("CODE\tADRESA\tROK\tBARCODE")

	with open(orderFilename+".txt", "a") as text_file:
		for i in range(0,Etiketa_Total):
			text_file.write("\n")
			text_file.write("%X%s%s%s\t" 
				% (
					sad.month, 
					sad.strftime("%y"),
					KlijentData[0],
					str(brojac).zfill(4)
					)
				)
			text_file.write(KlijentData[1]+", ")
			text_file.write("%s, %s\t" % (KlijentData[2],KlijentData[3]))
			text_file.write("%s" % order[2])
			if len(order)>3:
				text_file.write("\t"+order[3])
			brojac +=1


#__main__

#print ("%d,%s,%s,%s" % (order[1],order[0],orderDateCode,order[2]))

newOrder =  ",".join((str(order[1]),order[0],orderDateCode,order[2],str(sad)))
if len(order)>3: newOrder = newOrder + ","+order[3]
#print (newOrder)

noviStartniBroj = getLastPrintedNumber(newOrder)
KlijentData = loadClientData()
writeNewFile(KlijentID+orderDateCode+"x"+str(order[1]), noviStartniBroj)

print (noviStartniBroj)
