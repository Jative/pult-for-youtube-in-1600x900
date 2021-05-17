import socket

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
Window.size = (432, 825)
Window.clearcolor = (.09, .09, .09, 1)

class Root(BoxLayout):
    def Searcher(self):
        text = self.ids['inp'].text
        self.ids['inp'].text = ""

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.1.172', 9093))

        sock.send(f"Search {text}".encode("utf-8"))

    def Sender(self, request):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.1.172', 9093))

        sock.send(request.encode("utf-8"))

        
class PultApp(App):
    def build(self):
        return Root()

PultApp().run()