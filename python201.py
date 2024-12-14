
#veri yapıları

notlar = [90 ,80 , 70 , 50]

liste = ["a",19.2,20]

liste_genis = ["a",19.2,20 , notlar]

liste_genis[0]

type(liste_genis[3])

list = [10,20,30,40,50]

list[2]

list[0:2]

list[:2]

yeni_list = ["a" ,10 , list]

yeni_list[1]

yeni_list[2][3] #liste içindeki listedeki elamana erişmek için kullanılır

#-------------------------------------------

liste = ["ali","veli","berkcan","ayse"]

liste

liste[1] = "veli'nin babası"

liste

liste[1] = "veli"

liste[0:3] = "alinin babası","velinin babası","berkcanın babası"

liste = liste + ["kemal"]

del liste[2]

#-----------------------------------

dir(list)

liste = ["ali","veli","isik"]

liste.append("ayse") #listeye veri ekler

liste

liste.remove("ali") #listeden veri siler


#Eleman ekleme ve eleman silme işlemleri indekslere göre gerçekleştiriliyor

liste = ["ali","veli","isik"]

liste.insert(0,"ceren")

liste

liste.insert(len(liste), "beren") #listenin sonuna veri ekler

liste.pop(1) #indekse göre veri siler

#----------------------------------------

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali") #listede olan istenilen elemanın sayısını verir


liste_yedek = liste.copy()


liste.extend(["a","b",10]) #eski listeye girilen yeni listeyi birleştirerek  kalıcı bir değişiklik yapıldı

liste

liste.index("ali") #istenilen verinin indexini verir

liste.reverse() #liste elmanlarını tersten sırayla yer değiştirerek yazar

list = [10,40,5,90]

list.sort()

list

liste.clear() #liste içerisindeki elmanların hepsini yok eder


#tuple

t= ("ali","veli",1,2,3,2,[1,2,3,4])

t= "ali","veli",1,2,3,[1,2,3]

#tuple()

#t = ("eleman")
t = ("eleman",)

type(t)

t[1]
t[0]

#dictionary (sözlük)


sozluk = {"REG" : "rekresyon modeli",
          "LOJ" : "lojistik regresyon",
          "CART" : "classification and reg..."}

sozluk

len(sozluk)

sozluk2 = {"ON" : 10,
          "YIRMI" : 20,
          "OTUZ" : 30}

sozluk2

sozluk3 = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART" : ["SSE",30]}

sozluk3

sozluk["LOJ"]

sozluk2["YIRMI"]

sozluk3["CART"]

sozluk4 = {"REG" : {"RMSE":10, #iç içe sözlük yapısı
                    "MSE": 20,
                    "SSE" :30},
           
          "LOJ" : {"RMSE": 10,
                   "MSE": 20,
                   "SSE": 30},
          
          "CART" :  {"RMSE":10,
                   "MSE": 20,
                   "SSE":30}}


sozluk4["CART"]["SSE"]


sozluk["GBM"] = "gradient boosting mac" #dictionarye veri ekleme

sozluk

#setler 

l = [1,"a","ali",123]

s = set(l)

t = ("a","ali")

s = set(t)

ali = "lutfen_ata_bakma_uzaya_bak"
type(ali)

s = set(ali)
s

l = ["ali","lütfen", "aya","bakma","ata","uzaya","bak","bak","ali","git","ali"]
l

s = set(l)
s

len(ali)


l = ["gelecegi","yazanlar"]
l

s = set(l)
s

dir(s)

s.add("ile")
s.add("gelecege_git")

s

s.remove("ile")

s.remove("ali")

s.discard("ali")

#-------------------------------------

set1 = set([1,2,3])
set2 = set([1,3,5])

set1.difference(set2) #1. kümede olup 2 de olmayan elamanı verir
set2.difference(set1)  #2. kümede olup 1 de olmayan elamanı verir

set1.symmetric_difference(set2) #ikisinde ortak olmayan elemanları verir

set1 - set2
set2 - set1






























