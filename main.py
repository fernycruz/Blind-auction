from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print (logo)

name = input("What is your name?: ")
bid = input("What is your bid?: $")
user_choice = []
first_user = {
    "user_name" : name,
    "user_bid" : bid
            
}

more_players = True
while more_players == True:
    user = user_choice
    finish = input ("Are there other bidders? Type yes or no:\n ").lower()
    
    def new_user(new_name, new_bid):
        new_user = {}
        new_user["name"] = new_name
        new_user["bid"] = new_bid
        user_choice.append(new_user)
    
    if finish == "yes":
        clear()
        name = input("What is your name?: ")
        bid = input("What is your bid?: ")
        new_user(new_name=name, new_bid=bid)

    else:
        more_players = False
        clear()
        highest_bid = max(user_choice, key=lambda x: x['bid'])
        print(f"The highest bid is ${highest_bid['bid']} by {highest_bid['name']}")
        