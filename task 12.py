# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.


print("Петя загадай 2 числа")

a= int(input("число А "))

b= int(input("число Б "))

s= a+b
p= a*b

print(f"Катя вот тебе 2 подсказки, сумма этих чисел {s} и их произведение {p}")

f=1000
i=0
j=0

while i<f:
    while j<f:
       if (i+j==s and i*j==p):
          break
       j+=1
    if (i+j==s and i*j==p):
          print(f"Катя ответила что первое число это {i} и второе это {j}")  
          break 
    j=0
    i+=1