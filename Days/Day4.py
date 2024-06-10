import random
a = random.random() * 5
print(a)

# names = input("Enter names: ").split(", ")
name = ['Hirak', 'Amish', 'Mittal', 'Pikku']
bbh = ['Chai', 'Kaus', 'Ved', 'Dev']
l = [name, bbh]
print(l[1][0])
# # payer = names[random.randint(0, len(names)-1)]
# # or
# payer = random.choice(names) #way better
# print(f"{payer} will pay the bill")
# print(len(name))
row1 = ["o", "o", "o"]
row2 = ["o", "o", "o"]
row3 = ["o", "o", "o"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Enter position (x, y): ").split(", ")
map[int(position[0])] [int(position[1])] = "x"
print(f"{row1}\n{row2}\n{row3}")

import random
thisdict = {
  1: "Rock",
  2: "Paper",
  3: "Scissor"
}
score = [0 ,0]
print("*******Welcome to Rock Paper Scissors********")
print("1 for Rock\n2 for Paper\n3 for Scissors\n")
for i in range (0, 5):
     user_choice = int(input("Enter choice: "))
    comp_choice = random.randint(1, 3)
    print(f"Userchoice: {thisdict[user_choice]}\nCompchoice: {thisdict[comp_choice]}")
    if user_choice == comp_choice:
    elif (comp_choice == 1 and user_choice == 3) or (comp_choice == 2 and user_choice == 1) or (comp_choice == 3 and user_choice == 2):
        score[0] += 1
    else:
        score[1] += 1

print(f"ScoreUser: {score[1]}\nScoreComp: {score[0]}")
if score[0] > score[1]:
    print(f"Computer wins by {score[0]-score[1]}")
else:
    print(f"User wins by {score[1] - score[0]}")

