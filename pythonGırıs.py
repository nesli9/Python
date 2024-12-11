
123

type(123)

"123"

"a" + "b"

"a" "b"

"a" " b"

"a" + "-b"

"a"*3

#string metodları

mvk = "python_programlama"
#del(mvk)

mtn = "python_programlama"

a=9
b=2

a*b

len(mtn) #verilen stringin karakter uzunluğunu bulan fonksiyon

#upper - lower metodu

mtn.upper()

mtn.lower()

mtn.islower() #gelen metnin büyük/küçük harfmi olup olmadığı kontrolü

mtn.isupper()

b = mtn.upper()

b.isupper()


#replace metodu (karakter değiştirme)

mtn.replace("a", "e")

#strip metodu (karekter dizilerinde kırpma işlemi - sağ ve soldan) 

mtn2 = " python_programlama "

mtn2.strip()

mtn3 = "*python_programlama*"

mtn3.strip("*")

#Karakter dizilerine uygulanabilecek metodlara nasıl erişilebilir

dir(mtn)

dir(str)

dir(int)

#substringler (karakter dizilerinin alt kümelerine erişme işlemleri)

mtn[0] #değişkendeki değerin köşeli parantez içrisine yazılan index değerine karşılık gelen karakter yazdırılır

mtn[0:3] #0 dan 3 e kadar olan karakterleri yazdırır

#değişkenler

type(100)
type(10.2)
type(1+2j)

#tip değişimi

toplama_bir = input()
toplama_iki= input()

toplama_bir + toplama_iki

int(toplama_bir)+ int(toplama_iki)

int(11.0)

float(12)

str(15)

#-----------------------------

print("python" , "programlama")

print("python" , "programlama" , sep ="_")

"10" + 2


"_python_".strip("_")

















