hardlopers = open('d:/HU/Programmeren/Opdrachten/Files/hardlopers.txt', 'a')
naam = input('Geef de naam van de hardloper:')
import datetime
vandaag = datetime.datetime.today()
date = vandaag.strftime("%a %d %b %Y")
time = vandaag.strftime("%H:%M:%S")
registratie = hardlopers.write(date+', '+time+', '+naam+'\n')
print (hardlopers)