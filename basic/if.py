# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

bmi = input("bmi: ")
bmi = int(bmi)
if bmi < 18.5:
    print("过轻")
elif bmi <= 25:
    print("正常")
elif bmi <= 32:
    print("肥胖")
else:
    print("严重肥胖")

