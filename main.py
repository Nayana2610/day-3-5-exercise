# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
upper_name1=name1.upper()
#print(upper_name1)

upper_name2=name2.upper()
#print(upper_name2)

new_name=upper_name1+upper_name2
#print(new_name)

T_count=new_name.count("T")
print(f"T occurs {T_count} times ")
R_count=new_name.count("R")
print(f"R occurs {R_count} times")
U_count=new_name.count("U")
print(f"U occurs {U_count} times")
E_count=new_name.count("E")
print(f"E occurs {U_count} times")

total1=(T_count+R_count+U_count+E_count)
print(f"total_true = {total1}")

L_count=new_name.count("L")
print(f"L occurs {L_count} times")
O_count=new_name.count("O")
print(f"O occurs {O_count} times")
V_count=new_name.count("V")
print(f"V occurs {V_count} times")
E_count1=new_name.count("E")
print(f"E occurs {E_count1} times")

total2=(L_count+O_count+V_count+E_count1)
print(f"total_love = {total2}")

#print(type(total1))
#print(type(total2))

total1=str(total1)
total2=str(total2)

Love_score=int(total1+total2)
#print(f"Your score is {Love_score}.")

if Love_score < 10 or Love_score > 90:
  print(f"Your score is {Love_score},you are together like coke and mentos.")
elif Love_score >= 40 and Love_score <= 50:
  print(f"Your score is {Love_score},you are alright together.")
else:
  print(f"Your score is {Love_score}.")
