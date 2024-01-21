# import threading
# import speech_recognition as sr
# from objectDetection import *
# from CurrencyDetection import *
# from TextDetection import *
# from time import ctime
#
#
# class Treading_Object_Detection:
#     stop_thread_objectDetection = True
#
#     stop_thread_currncydetection = False
#
#     stop_thread_textdetection = False
#
#     stop_thread_time = False
#
#     def thread_objectDetection(stop):
#         objectDetection(stop)
#
#     def thread_currncydetection(stop):
#         if stop:
#             SaveImage()
#             currncydetection()
#             # i = 0
#             # while (i < 1000):
#             #     i += 1
#             #     print(str(i)+"currncy")
#
#     def thread_textdetection(stop):
#         if stop:
#             SaveTextImage()
#             TextToSpeach()
#             # i = 0
#             # while (i < 1000):
#             #     i += 1
#             #     print(str(i)+"text")
#
#     def thread_time(stop):
#         if stop:
#             speak.Speak(ctime())
#
#
# if __name__ == "__main__":
#     thread = Treading_Object_Detection
#
#     object = threading.Thread(target=thread.thread_objectDetection, args=(lambda: thread.stop_thread_objectDetection,))
#
#     object.start()
#
#     while (True):
#         speak = wincl.Dispatch("SAPI.SpVoice")
#
#         r = sr.Recognizer()  # initialize recognizer
#         mic = sr.Microphone()
#         print("speak")
#         try:
#             print("speak+++++++++++")
#             with mic as source:
#                 audio = r.listen(source)
#                 words = r.recognize_google(audio)
#                 print(words)
#         except:
#             print('error')
#             continue
#         if words == "currency":
#             thread.stop_thread_textdetection = False
#             thread.stop_thread_currncydetection = True
#             thread.stop_thread_objectDetection = False
#             currncy = threading.Thread(target=thread.thread_currncydetection,
#                                        args=(lambda: thread.stop_thread_currncydetection,))
#             currncy.start()
#             currncy.join()
#             print("currncy detection")
#             thread.stop_thread_objectDetection = True
#             thread.stop_thread_currncydetection = False
#             object = threading.Thread(target=thread.thread_objectDetection,
#                                       args=(lambda: thread.stop_thread_objectDetection,))
#             object.start()
#             continue
#
#         if words == "text":
#             cap = cv2.VideoCapture(1)
#             thread.stop_thread_textdetection = True
#             thread.stop_thread_currncydetection = False
#             thread.stop_thread_objectDetection = False
#             text = threading.Thread(target=thread.thread_textdetection,
#                                     args=(lambda: thread.stop_thread_textdetection,))
#             text.start()
#             text.join()
#             print("Text detection")
#             thread.stop_thread_objectDetection = True
#             object = threading.Thread(target=thread.thread_objectDetection,
#                                       args=(lambda: thread.stop_thread_objectDetection,))
#             object.start()
#             continue
#         if words == 'what is the time':
#             thread.stop_thread_time = True
#             thread.stop_thread_textdetection = False
#             thread.stop_thread_currncydetection = False
#             thread.stop_thread_objectDetection = False
#             time = threading.Thread(target=thread.thread_time,
#                                     args=(lambda: thread.stop_thread_time,))
#             time.start()
#             time.join()
#             thread.stop_thread_objectDetection = True
#             thread.stop_thread_time = False
#             object = threading.Thread(target=thread.thread_objectDetection,
#                                       args=(lambda: thread.stop_thread_objectDetection,))
#             object.start()
#             continue
#         if words == 'exit':
#             speak.Speak('goodbye Baby')
#
#             thread.stop_thread_objectDetection = False
#
#             thread.stop_thread_currncydetection = False
#
#             thread.stop_thread_textdetection = False
#
#             thread.stop_thread_time = False
#             break
