#############################
# Collaborators: (enter people or resources who/that helped you)
# If none, write none
#
#
#############################
play = input("Do you want to play? ")
if play == "No" or play == "no" or play == "NO":
    print("I'm offended. Go away.")
elif play == "Yes" or play == "yes" or play == "YES":
    print("Great, let's go!")
else:
    print("Say yes or no, please!")

num = int(input("Enter your favorite number: "))
if num % 2 == 0:
    print("Even!")
else:
    print("Odd!")