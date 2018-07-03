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


def recognize(m_name):
    if os.path.isfile(m_name):
        unknow_person = face_recognition.load_image_file(m_name)
    else:
        print('檔案不存在')
        return
    unknown_person_encoding = face_recognition.face_encodings(unknow_person)[0]

    for index, konw in enumerate(known_faces):
        results = face_recognition.compare_faces(konw, unknown_person_encoding)
        count = 0
        for res in results:
            if res:
                count += 1
        success_rate = float(count / len(results))
        if success_rate > 0.5:
            print('您要辨識的臉是 ' + str(index + 1) + ' 號 - 符合率 : ' + str(math.floor(success_rate * 100)) + '%')
            return

    print('我們無法辨別此臉，尚未學習過')



