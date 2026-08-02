a = int(input("please enter age: "))
b = input("please enter your gender: ")
if a >= 18: 
    if b == "male":
      print("allowed")
elif a < 18:
    print("not allowd")
else :
    print("wrong data enter")