from gtts import gTTS
import playsound
import os,time, wikipedia
from datetime import datetime
import speech_recognition as sr

ngaygio = datetime.now()

def say(text):
    tts = gTTS(text=text,lang='vi')
    tenfile='audio.mp3'
    tts.save(tenfile)
    playsound.playsound(tenfile)

def facebook():
    return os.system("open \"\" https://facebook.com")
def nhacplay():
    return os.system("open \"\" https://www.youtube.com/watch?v=fGqaLEfycEA&t=1735s&ab_channel=SCRemix")
def mobaihat(tenbaihat):
    url ="https://www.youtube.com/results?search_query="
    tenbaihat = tenbaihat.replace(" ", "+")
    url = url+tenbaihat
    return os.system("open \"\""+url)
def foody():
    return os.system("open \"\" https://www.foody.vn/hue")

r = sr.Recognizer()
exit = 0
while True:
    if exit == 4:
        say('bạn không cần tôi hỗ trợ hả, nếu cần thì hãy gọi tôi nhé. chào tạm biệt ')
        break
    with sr.Microphone() as source:
        #khử nhiễu môi trường thu
        r.adjust_for_ambient_noise(source, duration=1)
        print("tôi đang lắng nghe đây...")
        #lắng nghe và tạo file audio
        file_audio = r.listen(source, timeout=4)
        try:
            #chuyển audio sang text dùng server google
            text = r.recognize_google(file_audio,language="vi")
        #xử lý ngoại lệ
        except:
            text = ""
        print("ghi nhận từ bạn: " + text)

        if text == "":
            robot_traloi = "tôi chưa nghe được gì cả, vui lòng nói lại"
            say(robot_traloi)
            exit += 1
        elif "Xin chào" in text or "xin chào" in text or "Hello" in text:
            robot_traloi = "chào bạn, rất vui được phục vụ"
            say(robot_traloi)
        elif "Ngày mấy" in text or "ngày mấy" in text or "Ngày bao nhiêu" in text:
            robot_traloi = ngaygio.strftime('hôm nay là ngày %d tháng %m năm %Y')
            print(robot_traloi)
            say(robot_traloi)
        elif "Mấy giờ" in text or "mấy giờ" in text:
            robot_traloi = ngaygio.strftime('bây giờ là %H giờ %M phút')
            say(robot_traloi)
        elif "Thứ mấy" in text or "thứ mấy" in text:
            robot_traloi = ngaygio.strftime('hôm nay là ngày thứ %w')
            say(robot_traloi)
        elif "Ăn gì" in text or "ăn gì" in text:
            robot_traloi = ngaygio.strftime('tôi sẽ gợi ý cho bạn ')
            say(robot_traloi)
            foody()
        elif "Mở Facebook" in text or "mở Facebook" in text:
            robot_traloi = 'vâng, tôi sẽ mở facebook ngay đây'
            say(robot_traloi)
            facebook()
        elif "Mở nhạc" in text or "mở nhạc" in text or "nghe nhạc" in text or "Nghe nhạc" in text:
            robot_traloi = 'vâng, tôi sẽ mở nhạc cho bạn'
            say(robot_traloi)
            nhacplay()
        elif "Nghe bài" in text or "nghe bài" in text or "mở bài" in text or "Mở bài" in text:
            robot_traloi = 'vâng, tôi sẽ mở bài này cho bạn'
            say(robot_traloi)
            mobaihat(text)
        elif "Cám ơn" in text or "cám ơn" in text or "Cảm ơn" in text or "cảm ơn" in text or "thank" in text or "Thank" in text:
            robot_traloi = 'không có gì, tôi luôn sẵn sàng phục vụ. bạn cần gì nữa không? '
            say(robot_traloi)
        elif "bye" in text or "Tạm biệt" in text or "tạm biệt" in text:
            robot_traloi = "cám ơn, hẹn gặp lại"
            say(robot_traloi)
            break
        elif "là gì" in text or "là ai" in text or "ở đâu" in text or "là đâu" in text or "muốn biết về" in text:
            wikipedia.set_lang("vi")
            robot_traloi = wikipedia.summary(text, sentences=1)
            say(robot_traloi)
        else:
            robot_traloi = "tôi chưa hiểu lắm, bạn có thể nói lại không"
            say(robot_traloi)

