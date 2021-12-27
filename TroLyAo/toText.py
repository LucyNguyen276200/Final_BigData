import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Xin chào, bạn cần tôi giúp ")
    r.adjust_for_ambient_noise(source, duration=1)
    print("tôi đang lắng nghe...")
    #lắng nghe và tạo file audio
    file_audio = r.listen(source, timeout=4)
    try:
        #chuyển audio sang text dùng server google
        text = r.recognize_google(file_audio,language="vi")
        print(text)
    #xử lý ngoại lệ
    except:
        text="tôi chưa nghe gì từ bạn"
        print(text)
