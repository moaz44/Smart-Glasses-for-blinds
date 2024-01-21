from time import ctime
from objectDetection import *
from CurrencyDetection import *
from TextDetection import *


class Threading:
    stop_thread_objectDetection = True
    speak = wincl.Dispatch("SAPI.SpVoice")
    imageCam = ImageCam()

    def thread_objectDetection(stop):
        object = ObjectDetection()
        object.objectDetection(stop)

    def thread_currncydetection(self):
            currency=CurrencyDetection()
            self.imageCam.SaveImage('currency')
            # currency.SaveImage()
            currency.currncydetection()

    def thread_textdetection(self):
            text = TextDetection()
            self.imageCam.SaveImage('text')
            # text.SaveTextImage()
            text.TextToSpeach()

    def thread_time(self):
            self.speak.Speak(ctime())
