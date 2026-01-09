user_guess = input("Guess a letter: ").lower()

e1 = False
e2 = False
e3 = False

if len(user_guess) > 1:
    e1 = True

if not (user_guess.isalpha() and user_guess.isascii()):
    e2 = True

if e1 and e2:
    e3 = True

if e3:
    print("E3")
elif e2:
    print("E2")
elif e1:
    print("E1")
else:
    print(user_guess)