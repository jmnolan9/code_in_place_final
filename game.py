import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import os

players = [f for f in os.listdir("players") if f.endswith(".png")]
random_index = random.randint(0, 9)

while len(players) >= 1:
    i = len(players)

    random_index = random.randint(0, i - 1)
    player = players[random_index]
    player = os.path.splitext(player)[0]

    print("Guess the player by his teammates!")

    img = mpimg.imread(f"teammates/{player}.png")
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    user_input = input("Who do you think it is? ")

    if user_input == player:
        print(f"{player} is correct! Nice job, can you guess the next one correctly? ")
    else:
        print("Not quite! Try again next time :/")

    # Remove the selected player
    del players[random_index]
