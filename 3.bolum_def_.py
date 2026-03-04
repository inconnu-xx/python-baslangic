
isim = input('isminiz: ')
yas = input('yasınız: ')
meslek = input('mesleğiniz: ')
hobi = input('hobiniz: ')

print(f"eleman adı: {isim}\neleman yası: {yas}\neleman mesleği: {meslek}\neleman hobisi: {hobi}")

#--------------------

def bilgi_al(ad, spor, meslek, hobi):
    print(f"eleman adı: {ad}\neleman sporu: {spor}\neleman mesleği: {meslek}\neleman hobisi: {hobi}")


bilgi_al("esam", "callisthenics", "satış", "gitar")

# --------------------

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
