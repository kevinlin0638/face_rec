import face_recognition
import os

import math

known_faces = []


def prepare_data():
    # Load the jpg files into numpy arrays
    for person in range(1, 51):
        images = []
        face_encodings = []

        for i in range(1, 10):
            file_str = "FaceDatabase/s" + str(person).zfill(2) + "_" + str(i).zfill(2) + ".jpg"
            if os.path.isfile(file_str):
                images.append(face_recognition.load_image_file(file_str))
        try:
            for img in images:
                face_encodings.append(face_recognition.face_encodings(img)[0])
            known_faces.append(face_encodings)
            print('編號 : s' + str(person).zfill(2) + ' 學習完成')
        except IndexError:
            print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
            quit()


