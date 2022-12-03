#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
ターミナルにきれいに文字を出力する、既にある文字の移動もできる
drawを連続で呼ぶことでアニメーションできる
ANSI でカーソルを移動して入力するのも、リストでまるごと操作するのも両方に良さnがありそう

休憩します
fix me ： 
layer にあるすべてを書くのではなく、スペース以外を上書きしていく感じで
clerの追加と、ANSIによるカーソル移動が必須
あと、適当に文字をズラしたりして検証したい
'''
import os
import time # for debug

TOP = "\u001b[0;0H"
FORWARD = "\u"

class Pydter:
    def __init__(self):
        '''
        初期化
        ・ターミナルの1行がいくらかを取得
        ・既にターミナルに書かれている文字を消す
        ・入力用のリストを作成する
        '''
        self.columns = os.get_terminal_size().columns
        self.lines = os.get_terminal_size().lines
#        self.clear()
        self.layers = [[[" " for col in range(self.columns)] for line in range(self.lines)]]
    def clear(self):
        pass
    def draw(self):
        '''
        リストを上から描画する
        すべてのレイヤを出力できる
        '''
        for layer in self.layers:
            for line in layer:
                for col in line:
                    print(col, end="")
            print(TOP)
        time.sleep(5)
    def add_layer(self):
        '''レイヤをわけれる'''
        self.layers.append([[" " for col in range(self.columns)] for line in range(self.lines)])
        return len(self.layers)

    class  object_(pydter, name):
        self.name = name
        def move(self):
            '''文字を指定した方向に移動する'''
        def foward(self):
            '''文字を1マス後ろにずらす'''
            # fix me ： move をオーバライドする
	def back(self):
	        '''文字を1マス前にずらす'''
	        # fix me ： move をオーバライドする
	def up(self):
	        '''文字を1マス上にずらす'''
	        # fix me ： move をオーバライドする
	def down(self):
	        '''文字を1マス下にずらす'''
	        # fix me ： move をオーバライドする
	def begin(self):
	        '''文字を行頭にずらす'''
	        # fix me ： move をオーバライドする
	def end(self):
	        '''文字を行末にずらす'''
	        # fix me ： move をオーバライドする
	def head(self):
	        '''文字を頭に'''
	        # fix me ： move をオーバライドする
	def bottom(self):
	        '''文字を底に'''
	        # fix me ： move をオーバライドする



        
def main():
    pydt = Pydter()
    layer_num = pydt.add_layer()
    while True:
        pydt.draw()
        
if __name__ == "__main__":
    main()
