import random 

max_lines = 4
max_bet= 1000
min_bet = 1

ROWS = 3
COLS= 3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_spin(rows,cols,symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        cur_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(cur_symbols)
            cur_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns) :
            if i!= len(columns)-1:
                 print(column[row], end=" | ")
            else:
                 print(column[row],end = "")
        
        print()
        
        
def deposit():
     while True:
         amt = input("how much would you like to deposit?")
         if amt.isdigit():
             amt = int(amt)
             if amt>0:
                 break
             else:
                 print("amount must be greater than 0.")
         else:
             print("Please enter a number.")
             
     return amt
 
def noline():
    while True:
         lines= input("enter the number of lines to bet on (1-"+str(max_lines)+")?")
         if lines.isdigit():
             lines= int(lines)
             if 1<= lines<= max_lines:
                 break
             else:
                 print("enter a valid number of lines.")
         else:
             print("Please enter a number.")
             
    return lines
 
def bet():
    while True:
            amt = input("what would you like to bet on each line?")
            if amt.isdigit():
                amt = int(amt)
                if min_bet<=amt<=max_bet:
                    break
                else:
                    print(f"amount must be between {min_bet} - {max_bet}.")
            else:
                print("Please enter a number.")
                
    return amt
 
def spin(bal):
    lines = noline()
    while True: 
        betamt=bet()
        total_bet = betamt*lines
        
        if total_bet>bal:
            print(f"you dont have enough balance to bet that amount. your balance is {bal}.")
        else :
            break 
    print(f"you are betting {betamt} on {lines} lines. Total bet amount is {betamt}") 
     
    slots= get_spin(ROWS,COLS,symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_win(slots,lines,betamt,symbol_value )
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
     bal = deposit()
     while True:
         print(f"current balance is {bal}")
         user=input("press enter to play(q to quit.) ")
         if user == "q":
            break
         bal += spin(bal)

     print(f"You left with ${bal}")
main()