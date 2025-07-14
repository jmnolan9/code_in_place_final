import matplotlib.pyplot as plt
import matplotlib.image as mpimg

players = ["lahm", "messi", "ronaldo"]

for i in range(len(players)):
    player = players[i]

    img = mpimg.imread(f"players/{player}_teammates.jpg")
    plt.imshow(img)
    plt.axis('off')  # Hide axis
    plt.title(f"{player}")
    plt.show()
# Load and display an image

img = mpimg.imread(f"players/lahm_teammates.png")
plt.imshow(img)
plt.axis('off')  # Hide axis
plt.show()