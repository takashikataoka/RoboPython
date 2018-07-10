# lv4
import hearing_player
import threading
from socket import *


class Player4(hearing_player.Player3, threading.Thread):
    def __init__(self):
        super(Player4, self).__init__()

    def getObjectMessage(self, message, keyword):
        result = ""
        index0 = message.find(keyword)
        while -1 < index0:
            index1 = message.find(")", index0+2)
            index2 = message.find(")", index1+1)
            result += message[index0:index2+1]
            result += ")"
            index0 = message.find(keyword, index2)
        return result

    def getPram(self, message, keyword, number):
        OUT_OF_RANGE = 999
        str = "(" + keyword
        index0 = message.find(str)
        if index0 < 0:
            return OUT_OF_RANGE

        index1 = message.find(" ", index0 + str.length())
        if number == 4:
            index1 = message.find(" ", index1 + 1)
        elif number == 3:
            index1 = message.find(" ", index1 + 1)
        elif number == 2:
            index1 = message.find(" ", index1 + 1)
        else:
            pass
        index2 = message.find(" ", index1+1)
        index2 = message.find(")", index1+1)
        if index3 < index2 and index3 != -1 or index2 == -1:
            index2 = index3
        result = 0.0
        try:
            result = float(message[index1:index2])
        except Exception:
            print("文字データによるエラー")
            result = OUT_OF_RANGE
        return result

    #　ボールが見えているときのplay
    def play(self, message, ballDist, ballDir):
        pass

    # ボールが見えていないときのplay
    def play(self, message):
        if self.checkInitialMode():
            self.setKickOffPosition()
            command = "(move " + str(self.m_dKickOffX) + " " \
                + str(self.m_dKickOffY) + ")"
            self.send(command)
        else:
            message = message.replace("B", "b")
            ball = self.getObjectMessage(message, "((b")
            if ball.startswith("((b"):
                ballDist = self.getPram(ball, "(b)", 1)
                ballDir = self.getPram(ball, "(b)", 2)
                self.play(message, ballDist, ballDir)
            else:
                command = "(turn 30)"
                self.send(command)

if __name__ == "__main__":
    players = []
    for i in range(22):
        p = Player4()
        players.append(p)
        if i < 11:
            teamname = "left"
        else:
            teamname = "right"
        players[i].initialize((i % 11 + 1), teamname, "localhost", 6000)
        players[i].start()
    print("試合登録完了")
