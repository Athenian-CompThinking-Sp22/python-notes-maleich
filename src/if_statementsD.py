#############################
# Collaborators: (enter people or resources who/that helped you)
# If none, write none
#
#
#############################
# play_game = input("Do you want to play? ")
# # if play_game == "Yes" or play_game == "yes":
# if play_game.title() == "Yes":
#     print("Yay, let's go!")
# elif play_game == "YES":
#     print("Yikes - all caps!")
# else:
#     print("Bummer!")

user_num = int(input("What's your favorite number? "))
if user_num % 2 == 0 and user_num < 10:
    print("Even!")
    print("Less than 10")
elif user_num % 2 == 0 and user_num > 10:
    print("Even and > 10!")
elif user_num == 10:
    print(user_num)
else:
    print("Odd!")
print("end")