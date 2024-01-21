import os
import cv2
from ArabicOcr import arabicocr
from googletrans import Translator
from gtts import gTTS
import playsound
import time
from imageCam import ImageCam




class TextDetection:
    imageCam = ImageCam()

    def TextToSpeach(self):
        image_path = self.imageCam.imagePath
        out_image = 'out.jpg'
        results = arabicocr.arabic_ocr(image_path, out_image)

        f = ""
        for i in range(len(results)):
            f+= " " + results[i][1]

        translator = Translator()
        t = translator.translate(f, dest="ar").text

        myobj = gTTS(text=t, lang='ar', slow=False)
        myobj.save("welcome2.mp3")
        playsound.playsound("welcome2.mp3")
        os.remove("welcome2.mp3")

