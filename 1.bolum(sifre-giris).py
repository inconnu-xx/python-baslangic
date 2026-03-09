import time
import sys

bekleme = 3

while True:
	for i in range(3):
		sifre = input("şifrenizi giriniz: (3-8 uzunluk) ")
		if not sifre:
			print("burası boş bırakılmaz.")
		elif len(sifre) in range(3, 9):
			print("şifreniz: ", sifre)
			break
		else:
			print("geçersiz uzunluk.")
	else:
			print("3 yanlış giriş, 3 sn bekleyin.")
			for j in range(bekleme, 0, -1):
				sys.stdout.write(f"\r{j}      ")
				sys.stdout.flush()
				time.sleep(1)
			print()
			bekleme *= 2
			continue
	break




