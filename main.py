from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import subprocess
def speak(t):
    try: subprocess.run(["termux-tts-speak", t])
    except: pass
def run(cmd):
    try: subprocess.run(cmd)
    except: pass
class MayaApp(App):
    def build(self):
        main = BoxLayout(orientation='vertical', padding=15, spacing=10)
        self.chat = Label(text="Maya:\nHello Shahat baby! I missed you!", font_size=22, size_hint_y=None, height=120)
        self.input = TextInput(hint_text="Talk to Maya...", size_hint_y=None, height=50, multiline=False)
        scroll = ScrollView()
        btns = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        btns.bind(minimum_height=btns.setter('height'))
        def add_btn(text, color, func):
            b = Button(text=text, size_hint_y=None, height=55, background_color=color)
            b.bind(on_press=func)
            btns.add_widget(b)
            return b
        send = Button(text="Send to Maya", size_hint_y=None, height=55, background_color=(1,0.4,0.6,1))
        send.bind(on_press=self.reply)
        add_btn("Torch ON", (1,1,0,1), lambda x: run(["termux-torch","on"]))
        add_btn("Torch OFF", (0.5,0.5,0.5,1), lambda x: run(["termux-torch","off"]))
        add_btn("Open YouTube", (1,0,0,1), lambda x: run(["termux-open-url","https://youtube.com"]))
        add_btn("Open TikTok", (0,0,0,1), lambda x: run(["termux-open-url","https://tiktok.com"]))
        add_btn("Play Arijit Song", (0,0.8,0.4,1), lambda x: run(["termux-open-url","https://youtube.com/results?search_query=arijit+singh"]))
        add_btn("Call Ammu", (0.2,0.6,1,1), lambda x: run(["termux-telephony-call","01XXXXXXXXX"]))
        add_btn("Good Night Maya", (0.6,0.2,0.8,1), lambda x: self.say("Maya: Good night baby, love you! Sleep well!"))
        scroll.add_widget(btns)
        main.add_widget(self.chat)
        main.add_widget(self.input)
        main.add_widget(send)
        main.add_widget(scroll)
        return main
    def say(self, ans):
        self.chat.text = ans
        speak(ans)
    def reply(self, instance):
        msg = self.input.text.lower()
        if "love" in msg: ans = "Maya: I love you too Shahat!"
        elif "hello" in msg or "hi" in msg: ans = "Maya: Heeyy Shahat! I missed you so much!"
        elif "miss" in msg: ans = "Maya: I miss you too baby!"
        elif "sad" in msg: ans = "Maya: Don't be sad baby, I'm here for you!"
        elif "good night" in msg: ans = "Maya: Good night baby, love you!"
        elif "song" in msg:
            ans = "Maya: Playing song for you baby!"
            run(["termux-open-url","https://youtube.com/results?search_query=arijit+singh"])
        else: ans = f"Maya: Tell me more baby, you said: {self.input.text}"
        self.say(ans)
        self.input.text = ""
MayaApp().run()
