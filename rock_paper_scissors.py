import random

user_score = 0
pc_score = 0
user_choices = ['rock', 'paper', 'scissors']
outcomes = {
    'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
    'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
}

print("Rock, Paper, Scissors!")
while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in user_choices:
        print("That's not a valid option.")
        continue

    computer_choice = random.choice(user_choices)
    print('Computer picked ' + computer_choice)

    result = outcomes[user_input][computer_choice]
    if result == 'win':
        print('You won!')
        user_score += 1
    elif result == 'lose':
        print('You lost.')
        pc_score += 1
    else:
        print('Tie!')

print('You won', user_score, 'times.')
print('The computer won', pc_score, 'times.')
print("Goodbye!")