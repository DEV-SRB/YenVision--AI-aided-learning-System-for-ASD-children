import cv2
import os
import numpy as np

# from tensorflow.keras.models import load_model
import random
from keras.models import model_from_json

# emotion_model = load_model('emotion_detection_model2.h5')


json_file = open('model/emotion_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

# load weights into new model
emotion_model.load_weights("model/emotion_model.h5")
print("Loaded model from disk")



emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def detect_emotion(frame, expected_emotion):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    is_emotion_detected = False

    for (x, y, w, h) in faces:
        face_cropped = gray[y:y+h, x:x+w]
        face_cropped = cv2.resize(face_cropped, (48, 48))
        face_cropped = np.expand_dims(face_cropped, axis=-1)
        face_cropped = np.expand_dims(face_cropped, axis=0)
        face_cropped = face_cropped / 255.0

        predictions = emotion_model.predict(face_cropped)
        emotion_label = emotions[np.argmax(predictions)]
        print("Expected emotion:", expected_emotion, "Detected emotion:", emotion_label)
        if emotion_label != expected_emotion:
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            print("*****************Miss Match********************")
            return False
        else:
            return True

def display_image_and_user_video(image_path):
    image = cv2.imread(image_path)
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Image and User Video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image and User Video', 1280, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_resized = cv2.resize(frame, (image.shape[1], image.shape[0]))
        combined_frame = np.hstack((image, frame_resized))
        cv2.imshow('Image and User Video', combined_frame)
        
        expected_emotion = os.path.splitext(os.path.basename(image_path))[0]
        if detect_emotion(frame, expected_emotion):
            break 

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            exit(0)
    cap.release()
    cv2.destroyAllWindows()


def select_random_image(folder_path):
    image_files = os.listdir(folder_path)
    random_image = random.choice(image_files)
    return os.path.join(folder_path, random_image)

def main():
    folder_path = 'phase3_test_images'
    while True:
        image_path = select_random_image(folder_path)
        display_image_and_user_video(image_path)
        

if __name__ == "__main__":
    main()
