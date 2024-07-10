import tkinter as tk
from PIL import Image, ImageTk
import subprocess

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
        
    def display_random_photo(self):
        # Execute backend code to get image path
        photo_path = subprocess.check_output(['python', 'backend.py']).decode().strip()
        
        # Load and display the image
        self.img = Image.open(photo_path)
        self.img.thumbnail((400, 400))  # Resize image if needed
        self.photo = ImageTk.PhotoImage(self.img)
        
        self.canvas = tk.Canvas(self.master, width=self.img.width, height=self.img.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
    def check_emotion(self):
        user_input = self.entry.get()
        try:
            user_choice = int(user_input)
            # Send user input to backend for validation
            result = subprocess.check_output(['python', 'backend.py', user_input]).decode().strip()
            tk.messagebox.showinfo("Result", result)
        except ValueError:
            tk.messagebox.showinfo("Invalid Input", "Please enter a number.")

def main():
    root = tk.Tk()
    app = EmotionRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
