
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






