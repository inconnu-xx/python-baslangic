# split ile verileri istediğimiz şekilde parcalarız
model = 'rs200 195.5cc tek-cilindir 24.40bg 18.06mn 166kg '

model = model.split()
print(model) #listeye cevirir
# print(model[0]) #listenin 0.indexini alir

#--------


tarih = '01/11/1999'
tarih = tarih.split('/') #split icine ne yazarsan veriyi oradan ayırır
print(tarih[2]) #günü getirir


#------


verial = input('parcalanacak veriyi gir: ')

for i in verial.split():
    #print(i, end="*") #end, for döngüsünün cıktılarını yan yana kullanmak icin iyi bir koddur. örn. end=" "
    print(i[0]) #inputun her kelimesinin 0.indexini almak icin

