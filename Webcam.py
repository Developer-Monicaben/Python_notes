# pip install opencv-python
# pip install deepface
# pip install mtcnn
# pip install tensorflow
# pip install keras

import cv2
from deepface import DeepFace

# Activity suggestions based on mood
activities = {
    "happy": ["Dance a little!", "Call a friend", "Go for a walk"],
    "sad": ["Listen to calm music", "Write your thoughts", "Take a rest"],
    "angry": ["Take deep breaths", "Try meditation", "Go for a run"],
    "surprise": ["Celebrate the moment!", "Share with friends", "Write it down"],
    "fear": ["Stay calm", "Talk to someone you trust", "Breathe slowly"],
    "disgust": ["Step away from negativity", "Do something creative", "Watch a comedy"],
    "neutral": ["Read a book", "Relax with tea", "Enjoy some quiet time"]
}

# Start webcam
cap = cv2.VideoCapture(0)
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Resize frame for faster detection
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Detect emotions using MTCNN backend
        result = DeepFace.analyze(
            img_path=small_frame,
            actions=["emotion"],
            enforce_detection=True,
            detector_backend='mtcnn'
        )

        # Draw rectangle and display mood for each face
        if isinstance(result, list):
            faces = result
        else:
            faces = [result]

        for face in faces:
            x, y, w, h = face["region"]["x"], face["region"]["y"], face["region"]["w"], face["region"]["h"]
            mood = face["dominant_emotion"]

            # Scale back coordinates because of resizing
            x, y, w, h = x*2, y*2, w*2, h*2

            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Mood: {mood}", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
            # Display top 2 activity suggestions
            acts = activities.get(mood.lower(), ["Stay positive!"])
            y_pos = y + h + 30
            for a in acts[:2]:
                cv2.putText(frame, f"- {a}", (x, y_pos),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                y_pos += 25

    except Exception as e:
        # If face not detected
        cv2.putText(frame, "No face detected", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show video feed
    cv2.imshow("Webcam Mood Detector", frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
