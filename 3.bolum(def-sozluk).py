
isim = input('isminiz: ')
yas = input('yasınız: ')
meslek = input('mesleğiniz: ')
hobi = input('hobiniz: ')

print(f"eleman adı: {isim}\neleman yası: {yas}\neleman mesleği: {meslek}\neleman hobisi: {hobi}")

# --------------------

# parametresiz fonksiyon örn.

def topla():
    birinci_sayi = int(input("taplanacak ilk sayı: "))
    ikinci_sayi = int(input("toplanacak ikinci sayı :"))
    islem = birinci_sayi + ikinci_sayi
    print(islem)

topla()

# --------------------

# parametreli fonksiyon örn.

def bilgi_al(ad, spor, meslek, hobi):
    print(f"eleman adı: {ad}\neleman sporu: {spor}\neleman mesleği: {meslek}\neleman hobisi: {hobi}")


bilgi_al("esam", "callisthenics", "satış", "gitar")

# --------------------

# basit su hesaplama

def su_hesap_basit():
    kilo = int(input("kilonuzu giriniz: "))
    islem = kilo * 0.03
    print("icmeniz gereken su miktarı: ", islem)

su_hesap_basit()

# ---------------------

# parametreli ve cinsiyete göre su hesaplama

def su_hesapla(kilo):
    e_hesapla = kilo*0.04
    k_hesapla = kilo*0.03

    cinsiyet = input("cinsiyetinizi giriniz: (kadın/erkek)").lower()

    if cinsiyet == "erkek":
        print("-"*30)
        print("cinsiyetiniz: ", cinsiyet)
        print(e_hesapla, "litre su icmelisiniz.")
        print("-"*30)
    elif not cinsiyet:
        print("cinsiyeti bos bırakma")
    elif cinsiyet == "kadın":
        print("-"*30)
        print("cinsiyetiniz: ", cinsiyet)
        print(k_hesapla, "litre su icmelisiniz.")
        print("-"*30)


kilo_al = int(input("kilonuzu giriniz: "))

su_hesapla(kilo_al)

# kilo parametresini kiloal ile dışarıdan alıyoruz kodumuz bunun üzerine kurulu
# sadelik icin hesap değişkenlerini icerden aldık ama dışardanda alabilirdik

# ----------------------


def toplama(x, y):
    # islem = x + y
    return x + y

a = toplama(5, 5)
b = 10 

print(a + b)


#islemi yorum satırından cıkarıp return yerine print toplama yazsaydık
#printin sonucu fonksiyonun dışındaki değişkene atanamazdı bu yüzden 
#return ile değerimizi dış dünyaya yollayarak kullanabiliriz. 

#-----------------------


def kullaniici_bilgileri(ad, soyad, yas, meslek="işsiz"):
    print(f"adınız: {ad}\nsoyadınız: {soyad}\nyasiniz: {yas}\nmesleğiniz: {meslek}")
    print("_"*30)

kullaniici_bilgileri("ahmo", "ışık", "20")


# def fonksiyonlarının parametrelerine yukarıdaki gibi varyasılan değer atayabiliriz
# yazdırırken değer vermezsek, varsayılan değer yazdırılır
# yalnız bu varsayılan değerli parametrelerin en sonda olması gerekir, sayısı farketmez

#-----------------------


#Yerel değişken (fonksiyonun içindeki) dışarıdaki kodda kullanılamaz. Global değişken (tüm kodda kullanılabilen değişken) fonksiyonun içinde kullanılabilir. Örn. yerel değişken yoksa ve fonksiyonun içinden global bir değişken  çağrılırsa ozaman global değişkenin değeri yazdırılır. 

a = 10

def degisken():
    print(a)

degisken()

#Örnekte global değişkenin yerelde kullanım şekli vardır. Değişkenin değerini yerelde değiştirmek için ise printten önce:

global a
a = 30

#Artık değer değişmiştir.


#-----------------------------------------------------------------------


sozluk = {"apple":"elma", "isim":"fatma", "yas":"25"}

# print(sozluk["isim"])

#sözlükler de listeler gibidir, key ve value bir degerdir bunu ölcmek icin len kullanılabilir

for i,j in sozluk.items():
    print(i, j)

# sözlüğü for ile yazdıracaksak key ve value icin iki değer aldırmalyız i, j 
# tüm elementleri yazdırmak icinde .items kullanmalıyız


#---------------------


protein = {"yumurta" : "6.5 gr protein", "yoğurt" : "1.5 gr protein", "fıstık ezmesi" : "5 gr protein"}
yiyecek = input("gıda ismi giriniz: ").capitalize

print(yiyecek, ":", protein.get(yiyecek, "aradığınız takım listede yok..."))

#get ikili fonksiyondur, if işlevi görür. ilk parametre var ise ikinci parametre yok ise çıktı verir. get ikili değer alan bir fonksiyondur.












