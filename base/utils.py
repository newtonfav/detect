import cv2
import os
from django.conf import settings


def draw_rectangle(img_up, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(img_up, (x, y), (x + w, y + h), (255, 0, 0), 2)


def detect_face(img):
    xml_path = os.path.join(settings.XML_ROOT,
                            'haarcascade_frontalface_default.xml')

    face_cascade = cv2.CascadeClassifier(xml_path)

    # Construct the full file path using Django's settings.MEDIA_ROOT
    image_path = os.path.join(settings.MEDIA_ROOT, img)
    img_up = cv2.imread(image_path)

    # Convert into grayscale
    gray = cv2.cvtColor(img_up, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    draw_rectangle(img_up, faces)

    cv2.imwrite('./static/test.jpg', img_up)

    # print(faces)
    if len(faces) == 1:
        return f'{len(faces)} face detected'

    elif len(faces) > 1:
        return f'{len(faces)} faces detected'

    else:
        return 'No Face detected'

    # Display the output
    # cv2.imshow('img', img_up)
    # cv2.waitKey()
