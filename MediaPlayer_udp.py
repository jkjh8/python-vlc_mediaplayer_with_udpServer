# -*- coding: utf-8 -*-
import sys, vlc, socket, os.path, threading
from _thread import *

instance = vlc.Instance()
player = instance.media_player_new()

class main_UdpServer():
    def __init__(self):
        port = 12302
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((socket.gethostbyname(socket.gethostname()), port))
        print("Udp Server Start {} : {}".format(socket.gethostbyname(socket.gethostname()), port))

    def run(self):
        while True:
            data, info = self.sock.recvfrom(65535)
            recv_Msg = data.decode()
            print(recv_Msg)
            self.dataParcing(recv_Msg)
            
    def dataParcing(self, data):
        if data == "play":
            mp.play("1.mp4")
        elif data == "stop":
            mp.stop()

class media_Player():
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def setNewPlayer(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def setEventManager(self):
        self.Event_Manager = player.event_manager()
        self.Event_Manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.songFinished)
    
    def setMedia(self, mediaFile):
        self.media = self.instance.media_new(mediaFile)
        self.player.set_media(self.media)

    def play(self, mediaFile):
        print(mediaFile)
        if not self.player:
            self.setNewPlayer()
            print("media player refresh")
        self.setEventManager()
        self.setMedia(mediaFile)
        self.player.play()

    def stop(self):
        self.player.stop()


    def songFinished(self,evnet):
        print("song Finish")


if __name__ == "__main__":
    mp = media_Player()
    app = main_UdpServer()
    app.run()