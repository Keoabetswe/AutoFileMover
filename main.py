import os
import shutil

image_format = ["jpg", "png", "gif"]
docs_format = ["txt", "docx", "pdf", "odt"]
audio_format = ["mp3"]

while True:
    files = os.listdir("./")

    for file in files:
        if os.path.isfile(file) and file != "main.py":
            ext = (file.split(".")[-1]).lower()

            if ext in docs_format:
                shutil.move(file, "C:/Users/Keoabetswe.Nthite/Documents/" + file)
            elif ext in image_format:
                shutil.move(file, "C:/Users/Keoabetswe.Nthite/Pictures/" + file)
            elif ext in audio_format:
                shutil.move(file, "C:/Users/Keoabetswe.Nthite/Music/" + file)
            else:
                shutil.move(file, "others/" + file)
