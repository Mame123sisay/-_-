import random

word=[
    'messi','teacher','student', 'banana','computer',     
      'elephant','guitar','kangaroo','lemon','monkey',
      'pizza','rainbow','sunshine','tiger','unicorn',
      'watermelon','zebra'
      ]

#functions for hangman game to display different stage at each incorrect guess
def draw_hangman(stage):
    stages = [
        '''
           +---+
               |
               |
               |
             ===
        ''',
        '''
           +---+
           O   |
               |
               |
             ===
        ''',
        '''
           +---+
           O   |
           |   |
               |
             ===
        ''',
        '''
           +---+
           O   |
          /|   |
               |
             ===
        ''',
        '''
           +---+
           O   |
          /|\\  |
               |
             ===
        ''',
        '''
           +---+
           O   |
          /|\\  |
          /    |
             ===
        ''',
        '''
           +---+
           O   |
          /|\\  |
          / \\  |
             ===
        '''
    ]

    print(stages[stage])


#to get word randomly from the list of words
choosen_word=random.choice(word)

display=[]# an empty list to put all the correct letter and word 
#print(choosen_word)

for i in range(len(choosen_word)):
    display+=['_']
 # if you made 6 incorrect guess you lose the game 
incorrect_guesses=0    
game_over=False   
while not game_over:
    
    # ask the user to prompt letter
    guessed_letter=input(" please guess a letter: ").lower()
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in choosen_word:
        incorrect_guesses+=1
        if incorrect_guesses==6:
            game_over=True
            print("You lose the game!!")
    if '_' not in display:
            game_over=True
            print(" congratulation's.. You won the game !!!")
            
    draw_hangman(incorrect_guesses)






    
   
         
    
        
         
        
           
       
        
            
            
          
          
    
        
    
        
        

        
        
       
    
    
    
    
    

    
        

    
    
    

    
    
   