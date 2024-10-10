#Importing the random Module
import random

#Defining the roll Function
def roll():
    min_value = 15
    max_value = 50
    roll = random.randint(min_value, max_value)

    if roll >= 80:
        print("Elon Mask: I'm such a bad public speaker! 🤩Damn. ")
    elif roll >= 45:
        print("🚀 Go to the Moon!")
    elif roll >= 20:
        print("Elon Mask: Tesla! Sustainable energy.🚙")
    
    return roll 

def random_event():
    events = [
        ("🌟 SpeaceX bonus! +50 points", 50),
        ("👤 To see one's enemy! -30 points", -30),
        ("🐶 Found a DOGE COIN! +100 points", 100),
        ("🌑 Black hole ... No effect", 0)
    ]
    event = random.choice(events)
    print(event[0])
    return event[1]

#Getting the Number of Players
while True:
    players = input("Elon Mask: Welcome to Speace X! Enter the number of players (15 - 50):")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Elon Mask: Must be between 2 - 4 players")
    else:
        print("Elon Mask: When something is important enough, you do it even if the odds are not in your favor. Try again.")

#Initializing Scores
max_score = 1500
player_scores = [0 for _ in range(players)]

#Main game Loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "Elon Mask: Are you ready? ")
        print("Total Moon Score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Are you going to the moon (d)? ")
            if should_roll.lower() != "d":
                break

            value = roll()
            if value == 1:
                print("You go to sky a 1m! Fly again")
                current_score = 0
                break
            else:
                current_score += value
                print("You go to sky a:", value)

            current_score += random_event()

            print("Total Moon Score is:", current_score)

        player_scores[player_idx] += current_score
        print("Total Moon Score is:", player_scores[player_idx])

    #Determining the Winner
        max_score = max(player_scores)
        winning_idx = player_scores.index(max_score)
        print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)



