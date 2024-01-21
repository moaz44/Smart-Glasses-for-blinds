import threading
import speech_recognition as sr
from Threading import Threading
from CurrencyDetection import *

if __name__ == "__main__":
    thread = Threading

    object = threading.Thread(target=thread.thread_objectDetection, args=(lambda: thread.stop_thread_objectDetection,))

    object.start()

    while (True):
        speak = wincl.Dispatch("SAPI.SpVoice")

        r = sr.Recognizer()  # initialize recognizer
        mic = sr.Microphone()
        print("speak")
        try:
            print("speak+++++++++++")
            with mic as source:
                audio = r.listen(source)
                words = r.recognize_google(audio)
                print(words)
        except:
            print('error')
            continue
        if words == "currency":
            thread.stop_thread_objectDetection = False
            currncy = threading.Thread(target=thread.thread_currncydetection(self=Threading()), )
            currncy.start()
            currncy.join()
            print("currency detection")
            thread.stop_thread_objectDetection = True
            object = threading.Thread(target=thread.thread_objectDetection,
                                      args=(lambda: thread.stop_thread_objectDetection,))
            object.start()
            continue

        if words == "text":
            thread.stop_thread_objectDetection = False
            text = threading.Thread(target=thread.thread_textdetection(self=Threading()),
                                    )
            text.start()
            text.join()
            print("Text detection")
            thread.stop_thread_objectDetection = True
            object = threading.Thread(target=thread.thread_objectDetection,
                                      args=(lambda: thread.stop_thread_objectDetection,))
            object.start()
            continue

        if words == "time":
            time = threading.Thread(target=thread.thread_time(self=Threading()),)
            time.start()
            time.join()
            continue

        if words == 'exit':
            speak.Speak('goodbye Baby')
            thread.stop_thread_objectDetection = False
            break
