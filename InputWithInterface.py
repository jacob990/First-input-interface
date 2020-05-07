#qpy:quiet
#-*-coding:utf8;-*-

import qpy
import androidhelper
try:
    import urllib.request as ur
except:
    import urllib as ur
from qsl4ahelper.fullscreenwrapper2 import *

droid = androidhelper.Android()

class MainScreen(Layout):
    def __init__(self):
        super(MainScreen,self).__init__(str("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background=""
	android:orientation="vertical"
	xmlns:android="http://schemas.android.com/apk/res/android">
	<ImageView
		android:id="@+id/logo"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="10"
	/>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="20">

		<TextView
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:textSize="8dp"
			android:text="Hello, Jacob"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
		/>
    </LinearLayout>

	<ListView
		android:id="@+id/data_list"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="55"/>

	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Carica"
			android:id="@+id/but_load"
			android:textSize="8dp"
			android:background="#ffEFC802"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Esci"
			android:id="@+id/but_exit"
			android:textSize="8dp"
			android:background="#ff06AF00"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
</LinearLayout>
"""),"SL4AApp")

    def on_show(self):
        self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.exit))
        self.views.but_load.add_event(click_EventHandler(self.views.but_load, self.load))

        pass

    def on_close(self):
        pass

    def load(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Load")

        saved_logo = qpy.tmp+"/qpy.logo"
        ur.urlretrieve("https://img.icons8.com/material-two-tone/384/github.png", saved_logo)
        self.views.logo.src = "file://"+saved_logo

    def exit(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Exit")
        FullScreenWrapper2App.close_layout()

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        # display a button with the text : Hello QPython 
        return Button(text='Hello Jacob990')

TestApp().run()

#-*-coding:utf8;-*-
#qpy:3
#qpy:webapp:Sample 
#qpy://localhost:8080/
"""
This is a sample for qpython webapp
"""
from bottle import route, run

@route('/')
def hello():
    return "Hello jacob"

run(host='localhost', port=8080)
#-*-coding:utf8;-*-
#qpy:pygame

import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))
# Only one built in font is available on Android
myfont = pygame.font.SysFont("DejaVuSans", 64)
label = myfont.render("Hello, Jacob", 1, (255, 255, 255))
clock = pygame.time.Clock()

while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    # Framelimiter
    clock.tick(60)
    surface.fill((0, 0, 0))
    surface.blit(label, (0, 0))
    pygame.display.flip()
#qpy:quiet
#-*-coding:utf8;-*-
"""
This is a sample project which use SL4A UI Framework,
There is another Sample project: https://github.com/qpython-android/qpy-calcount
"""
import qpy
import androidhelper
try:
    import urllib.request as ur
except:
    import urllib as ur
from qsl4ahelper.fullscreenwrapper2 import *

droid = androidhelper.Android()

class MainScreen(Layout):
    def __init__(self):
        super(MainScreen,self).__init__(str("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background="#ff0E4200"
	android:orientation="vertical"
	xmlns:android="http://schemas.android.com/apk/res/android">
	<ImageView
		android:id="@+id/logo"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="10"
	/>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="20">

		<TextView
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:textSize="8dp"
			android:text="Hello, QPython"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
		/>
    </LinearLayout>

	<ListView
		android:id="@+id/data_list"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="55"/>

	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Load"
			android:id="@+id/but_load"
			android:textSize="8dp"
			android:background="#ffEFC802"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Exit"
			android:id="@+id/but_exit"
			android:textSize="8dp"
			android:background="#ff06AF00"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
</LinearLayout>
"""),"SL4AApp")

    def on_show(self):
        self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.exit))
        self.views.but_load.add_event(click_EventHandler(self.views.but_load, self.load))

        pass

    def on_close(self):
        pass

    def load(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Load")

        saved_logo = qpy.tmp+"/qpy.logo"
        ur.urlretrieve("https://www.corsinvest.it/wp-content/uploads/2019/10/github-logo-300x300.png", saved_logo)
        self.views.logo.src = "file://"+saved_logo

    def exit(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Exit")
        FullScreenWrapper2App.close_layout()

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
#qpy:quiet
#-*-coding:utf8;-*-
"""
This is a sample project which use SL4A UI Framework,
There is another Sample project: https://github.com/qpython-android/qpy-calcount
"""
import qpy
import androidhelper
try:
    import urllib.request as ur
except:
    import urllib as ur
from qsl4ahelper.fullscreenwrapper2 import *

droid = androidhelper.Android()

class MainScreen(Layout):
    def __init__(self):
        super(MainScreen,self).__init__(str("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background="#ff0E4200"
	android:orientation="vertical"
	xmlns:android="http://schemas.android.com/apk/res/android">
	<ImageView
		android:id="@+id/logo"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="10"
	/>
	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="20">

		<TextView
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:textSize="8dp"
			android:text="Hello, QPython"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
		/>
    </LinearLayout>

	<ListView
		android:id="@+id/data_list"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="55"/>

	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Load"
			android:id="@+id/but_load"
			android:textSize="8dp"
			android:background="#ffEFC802"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:text="Exit"
			android:id="@+id/but_exit"
			android:textSize="8dp"
			android:background="#ff06AF00"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"/>
	</LinearLayout>
</LinearLayout>
"""),"SL4AApp")

    def on_show(self):
        self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.exit))
        self.views.but_load.add_event(click_EventHandler(self.views.but_load, self.load))

        pass

    def on_close(self):
        pass

    def load(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Load")

        saved_logo = qpy.tmp+"/qpy.logo"
        ur.urlretrieve("https://www.qpython.org/static/img_logo.png", saved_logo)
        self.views.logo.src = "file://"+saved_logo

    def exit(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        droid.makeToast("Exit")
        FullScreenWrapper2App.close_layout()

if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()
#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        # display a button with the text : Hello QPython 
        return Button(text='Hello QPython')

TestApp().run()

#stima il tuo rischio di CoVid-19 con poche domande

def covid():
    
    print('Benvenuto nel test Covid-19, puoi calcolare una stima sulla tua % di rischio rispondendo a queste 5 domande')

    name = input('Nome: ')
    age = int(input('Età: '))

    print('\nHai qualcuno di questi sintomi?')
    fever = int(input('Febbre (0= no, 1= si): '))
    cough = int(input('Tosse (0= no, 1= si): '))
    sob = int(input('Problemi respiratori (0= no, 1= si): '))
    sore = int(input('Mal di gola o naso che cola (0= no, 1= si): '))
    vomit = int(input('Vomito (0= no, 1= si): '))
    ill = int(input('Diabete, problemi ai reni o malattie cardiache (0= no, 1= si): '))
    epi = int(input('Sei stato in una regione epidemica o in contatto con una persona di quella regione negli ultimi 14 giorni? (0= no, 1= si): '))

    risk = fever*2 + cough*2 + sob*2 + sore + vomit + ill

    print('\nok, caro', name)
    if epi ==0:
        if risk > 4: print("non hai un alto rischio di COVID 19, probabilmente è influenza,")
        else: print("hai il rischio di infezione da COVID 19,")
    if epi ==1:
        if risk > 4: print('hai il rischio di infezione, dovresti indossare una maschera chirurgica ed essere isolato fino a quando non esegui il test')
        else: print("non hai segni di COVID 19, ma potresti avere dei rischi a causa della regione epidemica, ")

    if -1<age<41: rate = "0.2 %"
    if 40<age<51: rate = "0.4 %"
    if 50<age<61: rate = '1.3 %'
    if 60<age<71: rate = "3.6 %"
    if 70<age<81: rate = '8 %'
    if 80<age: rate = '14.8 %'
    print('in base alla tua età, se vieni infettato, il tasso di mortalità è:', rate)

covid()
