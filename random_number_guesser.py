import random

while True:
    start_range = input("Enter the start of the range: ")
    try:
        start = int(start_range)
        break
    except Exception:
        print("Please enter a valid number.")

while True:
    end_range = input("Enter the end of the range: ")
    try:
        end = int(end_range)
        if end > start:
            break
        else:
            print("Please enter a valid number.")
            continue
    except Exception:
        print("Please enter a valid number.")

number = random.randint(start, end)
count = 0

while True:
    user_input = input("Guess a number: ")
    try:
        user_input = int(user_input) 
        count += 1
        if user_input == number:
            break     
    except Exception:
        print("Please enter a valid number.")

if count > 1:
    print(f"You guessed the number in {count} attempts")
else:
    print(f"You guessed the number in {count} attempt")
