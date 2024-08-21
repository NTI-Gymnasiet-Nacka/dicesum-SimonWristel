# Dice sum probability calculator
# Författare: 
# Datum:
import os
os.system('cls')

def main():
    user_input = [int(x) for x in input("Skriv in två siffror mellan 4 och 20 ").split(" ")]
    min_dice = min(user_input)
    max_dice = max(user_input)

    for sum in range(min_dice + 1, max_dice + 2):
        print(sum)

if __name__ == "__main__": 
    main()