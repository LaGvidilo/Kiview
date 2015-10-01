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
from kivy.properties import StringProperty
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
import os, fnmatch, glob

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

def find_f(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

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
	if var.sup.count(self.id)==0:
		if self.id !="PHOTO SUPPRIMEE":
			self.parent.parent.parent.img.source=self.id
			var.current=self.id
	if var.sup.count(self.id)!=0:
		var.current=""
		self.id="PHOTO SUPPRIMEE"


def callback_btn_ouv(self):
	if var.sup.count(var.current)==0:
		if var.current!="":
			os.system("screen -d -m -L nautilus "+var.current)

def callback_Yes(self):
	if var.sup.count(var.current)==0:
		if var.current!="":
			os.remove(var.current)
			var.sup.append(var.current)

def callback_No(self):
	pass

def callback_btn_sup(self):
	content=BoxLayout(orientation='vertical')
	subcontent=BoxLayout(orientation='horizontal',size_hin_y=.1)
	btn1 = Button(text="Yes")
	#btn1.bind(on_press=callback_Yes)
	subcontent.add_widget(btn1)
	btn2 = Button(text="No")
	#btn2.bind(on_press=callback_No)
	subcontent.add_widget(btn2)
	label=Label(text='Voulez-vous supprimer cette photo?')
	
	content.add_widget(label)
	content.add_widget(subcontent)
	
	popup = Popup(title='Test popup', content=content,
		      auto_dismiss=True,id="popup",size=(200,200))
	btn1.bind(on_press=callback_Yes)
	btn2.bind(on_press=callback_No)
	btn1.bind(on_release=popup.dismiss)
	btn2.bind(on_release=popup.dismiss)
	popup.open()

def callback_btnplus(self):
	n,e=0,len(var.curwidget)
	while n<e-1:
		if var.curwidget[n]!="None":
			print (var.curwidget[n],self.parent)
			self.parent.remove_widget(var.curwidget[n])
		n=n+1
	
	dernierbtn=var.curwidget[n]
	var.curwidget=[]
	layout=self.parent
	#layout.bind(minimum_height=layout.setter('height'))
	i,k=var.curs,0
	if (i+1==len(var.lst)): var.curs,i=0,0
	while i<len(var.lst):
		print ("<",i,"/",len(var.lst),">")
		btn = ToggleButton(text="", size_hint_y=None, height=80, group='tg1',size_hint_x=.1,id=var.lst[i])
		btn.bind(on_press=callback_btn)
		img = Image(source=var.lst[i],size_hint_x=.9)
		var.curwidget.append(img)
		var.curwidget.append(btn)
		layout.add_widget(img)
		layout.add_widget(btn)
		if (k>100) or (i+1>=len(var.lst)): 
			var.curs=i
			i=len(var.lst) 
			btn = Button(text="plus...", size_hint_y=None, height=80,size_hint_x=.2)
			btn.bind(on_press=callback_btnplus)
			var.curwidget.append(btn)
			layout.add_widget(btn)
		k=k+1
		i=i+1
	self.parent.remove_widget(dernierbtn)
	
"""

def charge():
	layout = GridLayout(cols=2, spacing=10, size_hint_y=None,id="layout")
	# Make sure the height is such that there is something to scroll.
	layout.bind(minimum_height=layout.setter('height'))
	i,k=0,0
	while i<len(var.lst):
		btn = ToggleButton(text=var.lst[i], size_hint_y=None, height=80, group='tg1',size_hint_x=.7)
		btn.bind(on_press=callback_btn)
		img = Image(source=var.lst[i],size_hint_x=.25)
		var.curwidget.append(img)
		var.curwidget.append(btn)
		layout.add_widget(img)
		layout.add_widget(btn)
		if k>100: 
			var.curs=i
			i=len(var.lst) 
			btn = Button(text="Afficher plus...", size_hint_y=None, height=80,size_hint_x=.2)
			btn.bind(on_press=callback_btnplus)
			#var.curwidget.append(btn)
			layout.add_widget(btn)
		k=k+1
		i=i+1
	return layout
"""

class mainApp(App):
	App.icon=''
	App.title="Kiview"

	def build(self):
		racine = ["/home"]
		aZ,bZ=find_files(racine[0]+"/*"),find_files(racine[0]+"/*.*")
		n,e=0,len(bZ)
		while n<e:
			aZ.remove(bZ[n])
			n=n+1		
		
		racine = add_lst(racine,aZ)		
		n,e=0,len(racine)
		lsta,lstb=[],[]

		#os.chdir(racine[0])
		#for file in glob.glob("*.JPG"):
		#	lstb.append(file)
		#for file in glob.glob("*.jpg"):
		#	lstb.append(file)
		##for file in glob.glob("*.PNG"):
		#	lstb.append(file)
		#for file in glob.glob("*.png"):
		#	lstb.append(file)
		#for file in glob.glob("*.bmp"):
		#	lstb.append(file)
		#for file in glob.glob("*.BMP"):
		#	lstb.append(file)
		while n<e:
			for filename in find_f(racine[n]+"/","*.JPG"):
				lstb.append(filename)
			lsta = add_lst(lsta,lstb)
			lstb=[]

			for filename in find_f(racine[n]+"/","*.jpg"):
				lstb.append(filename)
			lsta = add_lst(lsta,lstb)
			lstb=[]

			for filename in find_f(racine[n]+"/","*.png"):
				lstb.append(filename)
			lsta = add_lst(lsta,lstb)
			lstb=[]
			
			for filename in find_f(racine[n]+"/","*.PNG"):
				lstb.append(filename)
			lsta = add_lst(lsta,lstb)
			lstb=[]
			
			for filename in find_f(racine[n]+"/","*.bmp"):
				lstb.append(filename)
			lsta = add_lst(lsta,lstb)
			lstb=[]
			
			for filename in find_f(racine[n]+"/","*.BMP"):
				lstb.append(filename)
			lsta = add_lst(lsta,lstb)
			lstb=[]
			
			n=n+1

		var.lst = add_lst(var.lst,lsta)
        #===============================================================
        #Création de la fenêtre, en fesant appel aux differentes classes
        #===============================================================
		layout = GridLayout(cols=2, spacing=10, size_hint_y=None,id="layout")
		# Make sure the height is such that there is something to scroll.
		layout.bind(minimum_height=layout.setter('height'))
		i,k=0,0
		while i<len(var.lst):
			btn = ToggleButton(text="", size_hint_y=None, height=80, group='tg1',size_hint_x=.1,id=var.lst[i])
			btn.bind(on_press=callback_btn)
			img = Image(source=var.lst[i],size_hint_x=.9)
			var.curwidget.append(img)
			var.curwidget.append(btn)
			layout.add_widget(img)
			layout.add_widget(btn)
			if k>100: 
				var.curs=i
				i=len(var.lst) 
				btn = Button(text="plus...", size_hint_y=None, height=80,size_hint_x=.2)
				btn.bind(on_press=callback_btnplus)
				var.curwidget.append(btn)
				layout.add_widget(btn)

			k=k+1
			i=i+1
		root = ScrollView(size_hint=(None, None), size=(180, 600))
		root.add_widget(layout)
		r = Builder.load_string("BoxLayout:"+chr(10)+"	id:'Box'"+chr(10)+"	img:img"+chr(10)
			+"	Image:"+chr(10)+"		id: img"+chr(10)+"		source:'' "+chr(10)+"		name:'img'"+chr(10))
		
		layoutcom = BoxLayout(orientation="vertical",spacing=5,id="boxcom",size_hint_x=.1)
		#btn = Button(text="Envoyer...", size_hint_y=None, height=80)
		#btn.bind(on_press=callback_btn_env)

		#layoutcom.add_widget(btn)
		btn = Button(text="Ouvrir", size_hint_y=None, height=80)
		btn.bind(on_press=callback_btn_ouv)

		layoutcom.add_widget(btn)

		btn = Button(text="Supprimer", size_hint_y=None, height=80)
		btn.bind(on_press=callback_btn_sup)

		layoutcom.add_widget(btn)

		r.add_widget(layoutcom)
		r.add_widget(root)
		#Builder.load_file("popup.kv")
		return r


	def _on_answer(self, instance, answer):
		print ("USER ANSWER: " , repr(answer))
		self.popup.dismiss()
	
#if __name__ == '__main__':
Config.set('kivy','exit_on_escape','0')
Config.write()
Config.set('graphics','width','1000')
Config.set('graphics','height','600')
Config.write()
mainApp().run()
