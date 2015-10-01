# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 13:47:00 2014

@author: coelho
"""
from __future__ import print_function
import kivy
kivy.require('1.8.0')


from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import Metrics
from kivy.uix.togglebutton import ToggleButton
#from kivy.properties import NumericProperty
#from kivy.properties import StringProperty
#from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.treeview import TreeView, TreeViewLabel,TreeViewNode
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
#from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SwapTransition, WipeTransition, SlideTransition
#from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
#from kivy.graphics import Color, Ellipse, Rectangle
from kivy.config import Config
#from kivy.logger import Logger
from kivy.core.audio import SoundLoader
import kivy.core 
import random
import math
import datetime
#import hashlib
import os

import var

def read_file(fichier):
    f=open(fichier,"r")
    dta=[]
    tmp=" "
    while tmp!="":
        tmp=f.readline()
	dta.append(tmp.replace('\n','').replace(".asc",""))
    f.close()            
    return dta

def find_files(f="*.*"):
	os.system("echo "+f+">tmp.txt")		
	tmpa=" "
	tmpb=""
	flm=open("tmp.txt","r")
	while tmpa!="":
		tmpa=flm.read(1)
		if tmpa==chr(32):
			tmpa=chr(10)
		tmpb=tmpb+tmpa
	flm.close()
	flm=open("tmp.txt","w")
	flm.write(tmpb)
	flm.close()

	xf=read_file("tmp.txt")
	os.remove("tmp.txt")
	xf.remove("")
	Verif=xf[0]
	if Verif[-5:]==f[-5:]: xf=[]
	return xf


def add_lst(lsta,lstb):
	n,e=0,len(lstb)
	while n<e:
		lsta.append(lstb[n])
		n=n+1
	return lsta

"""
	DEBUT DES CLASSES DE L'INTERFACE
"""



def callback_btn(self):
	#print ("CALLBACK "+self.text)
	#print (self.parent.parent.parent.img)
	self.parent.parent.parent.img.source=self.text
	var.current=self.text

def callback_btn_env(self):
	print (var.current)

class mainApp(App):
	App.icon=''
	App.title="game"

	def build(self):
		racine = ["~/Images"]
		aZ,bZ=find_files(racine[0]+"/*"),find_files(racine[0]+"/*.*")
		n,e=0,len(bZ)
		while n<e:
			aZ.remove(bZ[n])
			n=n+1		
		
		racine = add_lst(racine,aZ)		
		n,e=0,len(racine)
		lsta=[]
		while n<e:
			lstb = find_files(racine[n]+"/*.JPG")
			lsta = add_lst(lsta,lstb)
			lstb = find_files(racine[n]+"/*.jpg")
			lsta = add_lst(lsta,lstb)
			lstb = find_files(racine[n]+"/*.png")
			lsta = add_lst(lsta,lstb)
			lstb = find_files(racine[n]+"/*.PNG")
			lsta = add_lst(lsta,lstb)
			lstb = find_files(racine[n]+"/*.bmp")
			lsta = add_lst(lsta,lstb)
			lstb = find_files(racine[n]+"/*.BMP")
			lsta = add_lst(lsta,lstb)
			n=n+1

		var.lst = add_lst(lsta,var.lst)
        #===============================================================
        #Création de la fenêtre, en fesant appel aux differentes classes
        #===============================================================
		layout = GridLayout(cols=2, spacing=10, size_hint_y=None,id="grid")
		# Make sure the height is such that there is something to scroll.
		layout.bind(minimum_height=layout.setter('height'))
		i=0
		while i<len(var.lst):
			btn = ToggleButton(text=var.lst[i], size_hint_y=None, height=80, group='tg1',size_hint_x=.7)
			btn.bind(on_press=callback_btn)
			img = Image(source=var.lst[i],size_hint_x=.3)
			layout.add_widget(img)
			layout.add_widget(btn)
			i=i+1
		root = ScrollView(size_hint=(None, None), size=(500, 800))
		root.add_widget(layout)
		r = Builder.load_string("BoxLayout:"+chr(10)+"	id:'Box'"+chr(10)+"	img:img"+chr(10)
			+"	Image:"+chr(10)+"		id: img"+chr(10)+"		source:'' "+chr(10)+"		name:'img'"+chr(10))
		
		layoutcom = BoxLayout(orientation="vertical",spacing=5,id="boxcom",size_hint_x=.1)
		btn = Button(text="Envoyer...", size_hint_y=None, height=80, group='tg2')
		btn.bind(on_press=callback_btn_env)

		layoutcom.add_widget(btn)
		btn = Button(text="Ouvrir...", size_hint_y=None, height=80, group='tg2')

		layoutcom.add_widget(btn)
		btn = Button(text="Supprimer...", size_hint_y=None, height=80, group='tg2')

		layoutcom.add_widget(btn)
		#r.add_widget(layoutcom)
		r.add_widget(root)
		return r


	
if __name__ == '__main__':
    Config.set('kivy','exit_on_escape','0')
    Config.write()
    Config.set('graphics','width','1500')
    Config.set('graphics','height','800')
    Config.write()
    mainApp().run()
