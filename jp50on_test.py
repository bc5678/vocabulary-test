#!/usr/bin/env python
# -*- coding: utf8 -*-
import random

jp50on_hiragana = 'あ い う え お か き く け こ さ し す せ そ た ち つ て と な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ わ を ん'
jp50on_katakana = 'ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ワ ヲ ン'

list_jp50onEng=[['a'],['i'],['u'],['e'],['o'],['ka'],['ki'],['ku'],['ke'],['ko'],['sa'],['shi', 'si'],['su'],['se'],['so'],['ta'],['chi','ti'],['tsu','tu'],['te'],['to'],['na'],['ni'],['nu'],['ne'],['no'],['ha'],['hi'],['fu','hu'],['he'],['ho'],['ma'],['mi'],['mu'],['me'],['mo'],['ya'],['yu'],['yo'],['ra'],['ri'],['ru'],['re'],['ro'],['wa'],['o', 'wo'],['n']]

list_jp50on_hiragana=jp50on_hiragana.split(' ')
list_jp50on_katakana=jp50on_katakana.split(' ')

def jpn_to_Eng(jpn_list):
	while(True):
		q = random.choice(range(len(jpn_list)))
		print(str(jpn_list[q]))
		ans = input('Your answer: ')
		if ans.lower() in list_jp50onEng[q]:
			print('***** Correct! *****\n')
		else:
			print('Wrong! Answer is %s\n' %  list_jp50onEng[q])

fun = input('1.平假名   2.片假名 :')

if (fun == '1'):
	jpn_to_Eng(list_jp50on_hiragana)
else:
	jpn_to_Eng(list_jp50on_katakana)

