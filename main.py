from gtts import gTTS
import playsound
import os,time, wikipedia
from datetime import datetime
import speech_recognition as sr
import locale
from youtube_search import YoutubeSearch
import webbrowser
ngaygio = datetime.now()
os.environ["PYTHONIOENCODING"] = "utf-8"
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8")
locale.setlocale(category=locale.LC_ALL, locale="vi")
def say(text):
    tts = gTTS(text=text,lang='vi')
    tenfile='audio.mp3'
    tts.save(tenfile)
    playsound.playsound(tenfile)
    os.remove(tenfile)

def facebook():
    return os.system("start https://facebook.com")
def nhacplay():
    return os.system("start https://www.youtube.com/watch?v=fGqaLEfycEA&t=1735s&ab_channel=SCRemix")
def mobaihat(tenbaihat):
    url ="https://www.youtube.com/results?search_query="
    tenbaihat = tenbaihat.replace(" ", "+")
    url = url+tenbaihat
    return os.system("start "+url)
def foody():
    return os.system("start https://www.foody.vn/hue")
def open_google_and_search(text):
  
    os.system("start https://www.google.com/search?q="+text+"")  
def play_song(text):
    mysong = text
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['channel_link']
    webbrowser.open(url)
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
        elif "Ngày mấy" in text or "ngày mấy" in text or "ngày bao nhiêu" in text:
            robot_traloi = ngaygio.strftime('hôm nay là ngày %d tháng %m năm %Y')
            print(robot_traloi)
            say(robot_traloi)
        elif "Mấy giờ" in text or "mấy giờ" in text:
            hours=ngaygio.strftime('%H').encode('ascii', 'ignore').decode('ascii')
            minutes=ngaygio.strftime('%M').encode('ascii', 'ignore').decode('ascii')
            robot_traloi = "Bây giờ là "+hours+" giờ "+minutes+" phút"
            say(robot_traloi)
            # UnicodeEncodeError: 'locale' codec can't encode character '\u1edd' in position 6: encoding error
        elif "Thứ mấy" in text or "thứ mấy" in text:
            robot_traloi = ngaygio.strftime('%w').encode('ascii', 'ignore').decode('ascii')
            robot_traloi = "Hôm nay là thứ "+robot_traloi
            say(robot_traloi)
            # UnicodeEncodeError: 'locale' codec can't encode character '\u1edd' in position 6: encoding error
        elif "Ăn gì" in text or "ăn gì" in text:
            robot_traloi = 'tôi sẽ gợi ý cho bạn '
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
            #play_song(text)
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
        elif "Tìm kiếm trên google" in text or "tìm kiếm trên google" in text or "Tìm kiếm" in text or "tìm kiếm" in text :
            
            robot_traloi = "Thực hiện tìm kiếm trên google"
            say(robot_traloi)
            open_google_and_search(text)    
        else:
            robot_traloi = "tôi chưa hiểu lắm, bạn có thể nói lại không"
            say(robot_traloi)

