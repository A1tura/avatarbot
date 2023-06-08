import cv2 as cv
import numpy as np
from datetime import datetime, timedelta

a = 1

start_time = datetime.strptime("2023-06-08", "%Y-%m-%d")
end_time = start_time + timedelta(days=1)
def convert_time_to_string(dt):
    return f"{dt.hour}_{dt.minute:02}"

convert_time_to_string(start_time)
def get_black_background():
    return np.zeros((500, 500))

def generate_image_with_text(text):
    image = get_black_background()
    font = cv. FONT_HERSHEY_TRIPLEX
    cv.putText(image, text, (int(image.shape[0]*0.35), int(image.shape[1]*0.5)), font, 1.5, (255, 255, 0), 2, cv.LINE_AA)
    return image

while start_time < end_time:
    text = convert_time_to_string(start_time).replace("_", ":")
    image = generate_image_with_text(text)
    cv.imwrite(f'image_time/{text.replace(":", "_")}.jpg', image)
    start_time += timedelta(minutes=1)
    a += 1