import random
r = random.randint(0,5)
lists = ["apple","brown","perfume","medicine","book","pterodactyl"]
word = lists[r]
wrong = 0
stages = ["",
          "_________         ",
          "|                 ",
          "|        |        ",
          "|        0        ",
          "|       /|\       ",
          "|       / \       ",
          "|                 "
          ]
remaining_letters = list(word)
board = ["___"] * len(word)
win = False
print("Welcome to Hangman")

while wrong < len(stages) - 1:
    print("\n")
    msg = "Guess a letter"
    char = input(msg)
    if char in remaining_letters:
        cind = remaining_letters.index(char)
        board[cind]=char
        remaining_letters[cind]='$'
    else:
        wrong += 1
    print(" ".join(board))
    e = wrong + 1
    print("\n".join(stages[0:e]))
    if "___" not in board:
        print ("You Win!")
        print(" ".join(board))
        win = True
        break
if not win:
    print("\n".join(stages[0:wrong]))
    print("You Lose! It was {}.".format(word))
