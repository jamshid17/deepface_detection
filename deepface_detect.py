from deepface import DeepFace

face_analysis = DeepFace.analyze(img_path="images/doston.jpg")[0]

print("kayfiyat ", face_analysis["dominant_emotion"])
print("age ", face_analysis["age"])
print("jinsi ", face_analysis["dominant_gender"])