import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# Create a Card Class
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

# Create a Deck Class

class Deck:
    
    def __init__(self):
        
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                mycard=Card(suit,rank)
                self.deck.append(mycard)
    
    def __str__(self): # start with an empty string
        deck_cards=''
        for card in self.deck:
            deck_cards+='\n'+card.__str__()
        return deck_cards
        

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        dealed_card=self.deck.pop()
        
        return dealed_card

# Create a Hand Class

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   
        
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
    
    def adjust_for_ace(self):
        while self.value>21 and 'Ace' in self.cards:
            self.value -= 10
            
# Create a Chips Class

class Chips:
    
    def __init__(self,total,bet=0):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = bet
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet

#  A function for taking bets

def take_bet(chips):
    
    while True:
    
        try:
            chips.bet=int(input('How many chips would you like to bet? '))
        except:
            print('Please enter an integer !')
        else:
            if chips.bet>chips.total:
                print('You do not have enough money! please take a lower bet!')
                continue
            else:
                break

#  A function for taking hits

def hit(deck,hand):
     
    dealed_card=deck.deal()
    hand.add_card(dealed_card)
    
    hand.adjust_for_ace()
    
# A function that prompting the Player to Hit or Stand

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        playing=input('Would you like to Hit or Stand? ')
        if playing=='hit':
            hit(deck,hand)
        elif playing=='stand':
            print("Player stands. Dealer is playing.")
            playing=False
        else:
            print('Please try again')
            continue
        break

# functions to display cards

def show_some(player,dealer):
    print(" \n Player's hand: \n ")
    for card in player.cards:
        print(card)
    print("\n Dealer's hand: \n")
    print('**hidden card**')
    print(dealer.cards[1])    

def show_all(player,dealer):
    print("\n Player's hand: \n")
    for card in player.cards:
        print(card)
    print("The player's value is: ",player.value)
    print("\n Dealer's hand: \n")
    for card in dealer.cards:
        print(card)
    print("The dealer's value is: ",dealer.value)

# functions to handle end of game scenarios

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("You have won!")
    chips.win_bet()    

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("You have lose!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

# the game itself :
while True:
    # Print an opening statement
    print('Welcome to blackjack game! ')

    
    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    total=int(input('How much money do you have? '))
    chips=Chips(total)
    
    
    # Prompt the Player for their bet
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            
            player_busts(player_hand,dealer_hand,chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:
    
        while dealer_hand.value<17:
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand,dealer_hand,chips)
        else:
            push(player_hand,dealer_hand)
  
    # Inform Player of their chips total 
    print(f'Your total chips is:{chips.total}')
    
    # Ask to play again
    
    x=input("Are you want to play again? please enter 'yes' or 'no' \n")
    if x=='yes':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break



    
    

