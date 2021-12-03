#WHACK-A-MOLE

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics import *
import random

class Game(Widget):
	def __init__(self, **kwargs):
		super(Game, self).__init__(**kwargs)
		
		#colours
		self.red = (1, 0, 0, 1)
		self.green = (0, 1, 0, 1)
		self.blue = (0, 0, 1, 1)
		self.yellow = (1, 1, 0, 1)
		self.cyan = (0, 1, 1, 1)
		self.black = (0, 0, 0, 1)
		self.white = (1, 1, 1, 1)
		self.grey = (0.5, 0.5, 0.5, 1)
		self.orange = (1, 0.5, 0, 1)
		self.pink = (1, 0.5, 1, 1)
		self.lime = (0.5, 1, 0, 1)
		
		#background
		self.bg = (1, 1, 0.5, 1)
		with self.canvas:
			Color(rgba=self.bg)
			Rectangle(size=(720, 1400))
			
		#title
		col = ((0.7, 0, 0.7, 1))
		title = Label(text="[u]Whack-A-Mole![/u]", pos=(300, 1250), color=col, font_size=70, markup=True)
		self.add_widget(title)

		#score
		self.score = 0	
		self.scoreLabel = Label(text=f"Score: {self.score}", pos=(40, 1100), color=col, font_size=40)
		self.add_widget(self.scoreLabel)
		
		#board
		self.holes = []
		self.boxes = []
		self.radius = 120
		self.positions = [0, 900]
		
		with self.canvas:
			for i in range(5):
				for j in range(5):
					Color(rgba=self.bg)
					self.boxes.append(Rectangle(size=(self.radius, self.radius), pos=(self.positions[0], self.positions[1])))
					Color(rgba=self.black)
					self.holes.append(Ellipse(size=(self.radius, self.radius), pos=(self.positions[0], self.positions[1])))
					
					self.positions[0] += 150
					if j == 4:
						self.positions[0] = 0
						self.positions[1] -= 150
						
		#mole
		self.icon = Image(source="mole.png")
		self.add_widget(self.icon)
		
		self.x, self.y = -35, 860
		self.mole = Image(source="mole.png", pos=(self.x, self.y), size=(200, 200))
		self.add_widget(self.mole)
		
		self.molePos = []
		j = 0
		k = self.y
		for i in range(25):
			self.molePos.append((self.x+(j*150), k))
			j += 1
			if j == 5:
				j = 0
				k -= 150
			
		#timing	
		Clock.schedule_interval(self.play, 0)
		self.count = 0
		self.duration = 40
		self.currentNum = random.randint(0, 24)
		self.currentPos = self.molePos[self.currentNum]
		
		self.mole.pos = self.currentPos
		
	def play(self, dt):
		#update position
		if self.count >= self.duration:
			self.count = 0
			self.currentNum = random.randint(0, 24)
			self.currentPos = self.molePos[self.currentNum]
			self.mole.pos = self.currentPos
			
		self.count += 1
		self.scoreLabel.text = f"Score: {self.score}"
		
	def on_touch_down(self, touch):
		if touch.pos[0] >= self.holes[self.currentNum].pos[0] and touch.pos[0] <= self.holes[self.currentNum].pos[0]+self.radius and touch.pos[1] >= self.holes[self.currentNum].pos[1] and touch.pos[1] <= self.holes[self.currentNum].pos[1]+self.radius:
				self.score += 1
				
class MyApp(App):
	def build(self):
		return Game()
		
if __name__ == "__main__":
	MyApp().run()
