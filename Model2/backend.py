import os
import random
from PIL import Image

# List of folder names representing emotions
emotions_folders = ['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise']

# Function to display a random photo from a given emotion folder
def display_random_photo(emotion):
    base_path = r'D:\ProjectFiles\Final_Project\Model2\Emo\emotions_folders'
    photos_path = os.path.join(base_path, selected_emotion)

    photo_files = [f for f in os.listdir(photos_path) if os.path.isfile(os.path.join(photos_path, f))]
    if not photo_files:
        print(f"No photos found in the '{emotion}' folder.")
        return
    selected_photo = random.choice(photo_files)
    photo_path = os.path.join(photos_path, selected_photo)
    img = Image.open(photo_path)
    img.show()

# Display a random photo from the selected emotion folder
selected_emotion = random.choice(emotions_folders)
print(f"Displaying a random photo for emotion: {selected_emotion}")
display_random_photo(selected_emotion)

# Prompt user for input
user_input = input("Enter the number corresponding to the emotion (1 to 6): ")

# Check if user input matches the selected emotion
try:
    user_choice = int(user_input)
    if user_choice >= 1 and user_choice <= 6:
        if user_choice == emotions_folders.index(selected_emotion) + 1:
            print("Success! Your input matches the emotion of the photo.")
        else:
            print("Failure! Your input does not match the emotion of the photo.")
    else:
        print("Invalid input. Please enter a number between 1 and 6.")
except ValueError:
    print("Invalid input. Please enter a number.")
