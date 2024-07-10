# import os
# import random
# import tkinter as tk
# from tkinter import messagebox
# import serial
# from PIL import Image, ImageTk

# # List of folder names representing emotions
# emotions_folders = ['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise']

# class EmotionRecognitionApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Emotion Recognition")
        
#         # Serial communication setup
#         self.ser = serial.Serial('COM9', 9600) # Adjust COM port as needed
        
#         # Displaying a random photo
#         self.display_random_photo()
        
#         # Prompt for user input
#         self.label = tk.Label(master, text="Enter the number corresponding to the emotion (1 to 6):")
#         self.label.pack()
        
#         self.entry = tk.Entry(master)
#         self.entry.pack()
        
#         self.submit_button = tk.Button(master, text="Submit", command=self.check_emotion)
#         self.submit_button.pack()
        
#     def display_random_photo(self):
#         self.selected_emotion = random.choice(emotions_folders)
#         base_path = r'D:\ProjectFiles\Final_Project\Model2\Emo\emotions_folders'
#         photos_path = os.path.join(base_path, self.selected_emotion)
        
#         photo_files = [f for f in os.listdir(photos_path) if os.path.isfile(os.path.join(photos_path, f))]
#         if not photo_files:
#             messagebox.showinfo("Error", f"No photos found in the '{self.selected_emotion}' folder.")
#             return
        
#         self.selected_photo = random.choice(photo_files)
#         photo_path = os.path.join(photos_path, self.selected_photo)
        
#         self.img = Image.open(photo_path)
#         self.img.thumbnail((400, 400))  # Resize image if needed
        
#         self.photo = ImageTk.PhotoImage(self.img)
        
#         self.canvas = tk.Canvas(self.master, width=self.img.width, height=self.img.height)
#         self.canvas.pack()
#         self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
#     def check_emotion(self):
#         user_input = self.entry.get()
#         try:
#             user_choice = int(user_input)
#             if user_choice >= 1 and user_choice <= 6:
#                 if user_choice == emotions_folders.index(self.selected_emotion) + 1:
#                     messagebox.showinfo("Result", "Success! Your input matches the emotion of the photo.")
#                     self.master.destroy()  # Close current window
#                     new_window = tk.Tk()  # Open new window
#                     new_app = EmotionRecognitionApp(new_window)
#                 else:
#                     messagebox.showinfo("Result", "Failure! Your input does not match the emotion of the photo.")
#             else:
#                 messagebox.showinfo("Invalid Input", "Please enter a number between 1 and 6.")
#         except ValueError:
#             messagebox.showinfo("Invalid Input", "Please enter a number.")

# def main():
#     root = tk.Tk()
#     app = EmotionRecognitionApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
import os
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import serial

# List of folder names representing emotions
emotions_folders = ['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise']

class EmotionRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Emotion Recognition")
        
        # Displaying a random photo
        self.display_random_photo()
        
        # Prompt for user input
        self.label = tk.Label(master, text="Enter the number corresponding to the emotion (1 to 6):")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.submit_button = tk.Button(master, text="Submit", command=self.check_emotion)
        self.submit_button.pack()
        
        # Initialize serial communication with Arduino
        self.ser = serial.Serial('COM9', 9600)  # Adjust COM port and baud rate as needed
        
    def display_random_photo(self):
        self.selected_emotion = random.choice(emotions_folders)
        base_path = r'D:\ProjectFiles\Final_Project\Model2\Emo\emotions_folders'
        photos_path = os.path.join(base_path, self.selected_emotion)
        
        photo_files = [f for f in os.listdir(photos_path) if os.path.isfile(os.path.join(photos_path, f))]
        if not photo_files:
            messagebox.showinfo("Error", f"No photos found in the '{self.selected_emotion}' folder.")
            return
        
        self.selected_photo = random.choice(photo_files)
        photo_path = os.path.join(photos_path, self.selected_photo)
        
        self.img = Image.open(photo_path)
        self.img.thumbnail((400, 400))  # Resize image if needed
        
        self.photo = ImageTk.PhotoImage(self.img)
        
        self.canvas = tk.Canvas(self.master, width=self.img.width, height=self.img.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
    def check_emotion(self):
        user_input = self.entry.get()
        arduino_input = self.read_serial_input()
        print(f"Received input from Arduino: {arduino_input}")
        
        try:
            user_choice = int(user_input)
            if user_choice >= 1 and user_choice <= 6:
                if user_choice == emotions_folders.index(self.selected_emotion) + 1:
                    messagebox.showinfo("Result", "Success! Your input matches the emotion of the photo.")
                    self.master.destroy()  # Close current window
                    new_window = tk.Tk()  # Open new window
                    new_app = EmotionRecognitionApp(new_window)
                else:
                    messagebox.showinfo("Result", "Failure! Your input does not match the emotion of the photo.")
            else:
                messagebox.showinfo("Invalid Input", "Please enter a number between 1 and 6.")
        except ValueError:
            messagebox.showinfo("Invalid Input", "Please enter a number.")
    
    def read_serial_input(self):
        if self.ser.in_waiting > 0:
            return self.ser.readline().decode().strip()
        else:
            return ""

def main():
    root = tk.Tk()
    app = EmotionRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
