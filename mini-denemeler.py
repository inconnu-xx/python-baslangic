import random

#dosyayı okur
with open("motivation.txt", "r", encoding="utf-8") as dosya:     # with, bir context manager başlatıp iş bitince kaynakları otomatik temizler. "r" ile dosyayı okuma modunda açıyoruz.
    cumleler = dosya.readlines()                                 # .readlines() dasyayı okur ve her satırı sonundaki /n ile birlikte bir eleman olarak alır.

#rastgele seçim
secili = random.choice(cumleler)                                 # .choice() verilen koleksiyondan rastgele bir eleman döndürür

print(secili.strip())                                            # .strip() baş ve sondaki gereksiz karakterleri siler (örn. /n)

#.txt dosyasındaki satırların aralarına boşluk bırakırsan, 15 dk mal gibi niye boş sonuç dönüyor diye hata ararsın.

#_________________________________________


import random, string

#şifre uzunluğu alır
uzunluk = int(input("şifre uzunluğu: "))

#kullanılacak karekterler
karakter = string.ascii_letters + string.digits + string.punctution

#uzunluk kadar karışık seçim yapılır
sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))

print("oluşturulan şifre:", sifre)


#__________________________________________


import random

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#bilgisayarın secimi
sayi = random.choice(sayilar)

#kullanıcının secimi
while True:
    secim = int(input("bir sayı seçiniz; "))  #while ile sayı bulunana kadar sonsuz döngü

    if secim == sayi:
        print("tebrikler, doğru tahmin!")
        break                                 #sayi bulununca döngüden cikis
    else:
        print("yanlış seçim, tekrar deneyin.")


#__________________________________________


import random

zarlar = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}           #sözlük, anahtar değeri 0

for i in range(1000000):                          #bir milyon kere döndür
    zar = random.randint(1,6)                     #1,6 dahil rastgele tam sayı secer
    zarlar[zar] +=1                               #anahtarın her seferinde sayısı artar

for zar in zarlar:                                #sonucu yazdırır (f, stringin icinde py kodu calıştırır)
    print(f"{zar} gelme olasılığı: {zarlar[zar] / 1000000}")



#---------------------------------------


birinci_sayi = int(input("birinci sayıyı giriniz: "))
ikinci_sayi = int(input("ikinci sayıyı giriniz: "))
islem = input("yapmak istediğiniz işleni giriniz (örn. + - * /): ")

if islem == "+":
    print(birinci_sayi + ikinci_sayi)
elif islem == "-":
    print(birinci_sayi - ikinci_sayi)
elif islem == "*":
    print(birinci_sayi * ikinci_sayi)
elif islem == "/":
    print(birinci_sayi / ikinci_sayi)
else:
    print("yanlış input!")

      #yorum satırına gerek yok

#-----------------------------------------

isim1 = "ahmet"
isim2 = "mehmet"

print(type(isim2))

#----

ters = "GALATASARAY sk"

print(ters.swapcase())

#----

#çlışmıyor, regex ile yeniden kodla
metin = "merhaba amk beyinsizi tam bir yarrağa benziyorsun oç"
yasakli = ("yarrak", "oç")
for i in yasakli:
    metin = metin.replace(i, "")
print(metin)

#------

metin = "merhaba ben hic kimseyim, sen kimsin kendimi tanıtmadan seni tanımaya calışmak gibi bir hareket yapıyorum evet begenmediysen siktir git"

if "siktir" in metin.split():
    print("kufur var")


liste = ["mavi", "kırmızı", "sarı", "yeşil"]
print(liste[0])
liste[2]="gri" #ikinci indexi gri ile degiştirir
# print(liste)
liste[0:3] = [] #sıfırdan üce kadar siler. ücü almaz yani sıfırdan üce kadar
print(liste)



yas = 17

if yas<18:
    print("yaşın tutmuyor, kayboll")
else:
    print("yaşın tutuyor")




x = 50
y = 5
x+=y
print(y)







