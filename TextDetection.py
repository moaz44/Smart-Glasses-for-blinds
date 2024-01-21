# import os
# import cv2
# from ArabicOcr import arabicocr
# from googletrans import Translator
# from gtts import gTTS
# import playsound
# import time
# sorry = "Sorry could not recognize any text"
#
# def SaveTextImage():
#     TIMER = int(10)
#     while True:
#         cap = cv2.VideoCapture(0)
#         ret, img = cap.read()
#         # cv2.imshow('a', img)
#         if True:
#             prev = time.time()
#             while TIMER >= 0:
#                 ret, img = cap.read()
#
#                 # Display countdown on each frame
#                 # specify the font and draw the
#                 # countdown using puttext
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 cv2.putText(img, str(TIMER),
#                             (200, 250), font,
#                             7, (0, 255, 255),
#                             4, cv2.LINE_AA)
#                 cv2.imshow('a', img)
#                 cv2.waitKey(125)
#
#                 # current time
#                 cur = time.time()
#
#                 # Update and keep track of Countdown
#                 # if time elapsed is one second
#                 # than decrease the counter
#                 if cur - prev >= 1:
#                     prev = cur
#                     TIMER = TIMER - 1
#
#             else:
#                 ret, img = cap.read()
#
#                 # Display the clicked frame for 2
#                 # sec.You can increase time in
#                 # waitKey also
#                 cv2.imshow('a', img)
#
#                 # time for which image displayed
#                 cv2.waitKey(10)
#
#                 # Save the frame
#                 cv2.imwrite('test2.jpg', img)
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 break
#
# def TextToSpeach():
#     image_path = 'test2.jpg'
#     out_image = 'out.jpg'
#     results = arabicocr.arabic_ocr(image_path, out_image)
#
#     f = ""
#     for i in range(len(results)):
#         f+= " " + results[i][1]
#
#     translator = Translator()
#     t = translator.translate(f, dest="ar").text
#
#     myobj = gTTS(text=t, lang='ar', slow=False)
#     myobj.save("welcome2.mp3")
#     playsound.playsound("welcome2.mp3")
#     os.remove("welcome2.mp3")
#
#
import speech_recognition as sr


while (True):
    # speak = wincl.Dispatch("SAPI.SpVoice")

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
