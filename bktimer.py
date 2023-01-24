import random
import winsound
import time

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


moves = ['B', "B'", 'U', "U'", "R", "R'", 'L', "L'"]
#generate scramble

def generate_scramble():
    scramble = [random.choice(moves)]
    while(len(scramble)) < 13:
        move = random.choice(moves)
        if move[0] != scramble[-1][0]:
            scramble.append(move)
            
    scram_string = ''
    for move in scramble:
        scram_string += move + ' '
        
    tips = []
    tips_count = random.randint(0, 4)
    tips_string = ''
    
    for corner in ['b', 'u', 'r', 'l']:
        corner_turn = random.choice(['ccw', 'cw', 'n/a'])
        if corner_turn == 'ccw':
            tips_string += corner + "' "
        elif corner_turn == 'cw':
            tips_string += corner + ' '

        
    
    
    
    return (scram_string + tips_string)[:-1]

def main():
    while True:
        print(generate_scramble() + '\n')
        x = input('Press space to start inspection: ')
        if x == ' ':
            #some 15-second timer starts
            j = input()
            
            
        #winsound.Beep(frequency, duration)
        


        

        