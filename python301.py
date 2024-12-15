#fonksiyonlar

def kare_al (x):
   print(x**2) 

kare_al(3)

def kare_al (x):
   print("girilen sayının karesi : " + str(x**2)) 


def carpma_yap(x,y):
    print(x*y)


carpma_yap(3, 5)

#ön tanımlı fonksiyonlar

def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(3)
carpma_yap(3,4)


carpma_yap(y=2 , x=5) #şeklinde argüman sırası bilinmediğinde bilinen argümanlar belirtilerek değer veilir


#fonksiyon çıktısını girdi olarak kullanma

def direk_hesap(isi,nem,sarj):
    return ((isi+nem)/sarj)

direk_hesap(10, 40, 70)
direk_hesap(10, 40, 70)*5

cikti = direk_hesap(10, 40, 70)
print(cikti)

#--------------------------------------------

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    
x   

eleman_ekle(5)
eleman_ekle("ali")

#-----------------------------------------

sinir = 500

sinir == 400 #sınır 400 eşit mi kontrolu yapılır

sinir == 500


#----------------------------------------


sinir = 50000
gelir = 40000

if gelir < sinir:
    print("gelir sınırdan küçük")
    print(gelir*2)

if gelir > sinir:
    print("gelir sınırdan büyük")

#--------------------------------------------

if gelir > sinir:
    print("gelir sınırdan küçük")
else:
    print("gelir sınırdan büyük")

#---------------------------------------

sinir = 5000
gelir = 5100

if gelir == sinir:
    print("gelir sınıra eşit")
else:
    print("gelir sınıra eşit değil")

#---------------------------------------------

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 25000


if gelir1 > sinir:
    print("tebrikler hediye kazandınız")
elif gelir1 < sinir:
    print("uyarı")
else:
    print("takibe devam")
    
#-----------------------------
sinir = 50000
magaza_adi = input("magaza adı girin : ")
gelir = int(input("gelirinizi girin : "))

if gelir1 > sinir:
    print("tebrikler " + magaza_adi + " promosyon kazandınız")
elif gelir1 < sinir:
    print("uyarı ! çok düşük gelir: " + str(gelir))
else:
    print("takibe devam")



#döngüler

ogrenci = ["ali","veli","ayse","mert"]

for i in ogrenci :
    print(i)


#---------------------

maaslar = [1000,2000,3000,4000,5000]

def yeni_maas(x):
    print((x*20)/100 + x)

for i in maaslar :
    yeni_maas(i)


#--------------------------------

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print((x*10)/100 + x)

def maas_alt(x):
    print((x*20)/100 + x)

for i in maaslar :
    if i <= 3000:
        maas_alt(i)
    else :
        maas_ust(i)


#------------------------------------

maaslar = [8000,2000,1000,3000,5000,7000]

maaslar.sort()

maaslar

for i in maaslar :
    if i == 3000:
        print("kesildi")
        break
    print(i)
        

for i in maaslar :
    if i == 3000:
        continue
    print(i)


#----------------------------

sayi = 1

while sayi < 9:
    sayi += 1
    print(sayi)
















