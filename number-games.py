import random


def get_guess():
    user_num = int(input("Give me your shot:"))
    return user_num


def greeting_at_start():
    print("Welcome to  our funny game\nHere you gotta guess a number between 1 and 30")
    print("Let's see if you can guess the correct number that I have in mind")
    print("Good luck with you newbies!")


def win(computer_num, user_num):
    if computer_num == user_num:
        return True
    else:
        return False


def outcome(computer_num, user_num, count):
    if computer_num > user_num:
        return "Sorry, my number is a bit larger!\nGuess again."
    elif computer_num < user_num:
        return "Oops, my number is smaller. go on again.\nGuess again."
    elif computer_num == user_num:
        print(f"Holly shit!\nYou got right to the point\nThe correct number was {
              computer_num}")
        if computer_num in records:
            best_record = min(records[computer_num], count)
            print(f"Sorry, but the best guessing record for {
                  computer_num} was {best_record} till now")
        else:
            records[computer_num] = count
            print(f"The best guessing times for {computer_num} is {count}")
        print(records)


def finish_game(computer_num, user_num):
    print(f"The number was {computer_num} and your guess was {
          user_num}\nThis was a pretty good game, hope to see you again!")
    res = input("Do you wanna play again? (Y/N) ")
    res = res.upper()
    if res in ['Y', 'YES', 'BALE', 'ARE', 'YEP']:
        return True
    else:
        return False


records = {}
greeting_at_start()
continue_game = True
user_num = 0
while (continue_game):
    count = 0
    computer_num = random.randint(1, 30)

    while (not win(computer_num, user_num)):
        count += 1
        user_num = get_guess()
        print(outcome(computer_num, user_num, count))

    continue_game = finish_game(computer_num, user_num)
# Just to say thanks for reading this!
# I am just adding another line to make a change!
