# Visualization for Water Area problem
import pygame
import time

class Visual(object):
	"""
	A simple pygame window to display the visualization
	for the pipe problem
	"""
	BG = (255,255,255)
	GREEN = (0,255,0)
	BLACK = (0,0,0)
	BLUE = (0,0,255)

	def __init__(self, pipes, w ,h, water=True):
		self.pipes = pipes
		self.w = w
		self.h = h
		max_y = max(self.pipes)
		max_x = len(self.pipes)
		self.inc_x = self.w // max_x
		self.inc_y = self.h // max_y
		self.win = pygame.display.set_mode((self.inc_x * max_x,self.inc_y * max_y))
		self.water = water

	def draw(self, water=False):
		self.win.fill(self.BG)

		# If we want to draw water
		if self.water:
			self.draw_water()

		# Draw the pipes
		cur_x = 0
		for pipe in self.pipes:
			pygame.draw.rect(self.win, self.GREEN, (cur_x, self.h - (self.inc_y * pipe), self.inc_x, self.inc_y * pipe))	
			cur_x += self.inc_x

		# Draw Grid Lines
		for x in range(0, self.w+1, self.inc_x):
			pygame.draw.line(self.win, self.BLACK, (x, 0), (x, self.h), 5)

		for y in range(0, self.h, self.inc_y):
			pygame.draw.line(self.win, self.BLACK, (0, y), (self.w, y), 5)

		# update display
		pygame.display.update()

	def draw_water(self):
		"""
		Draws the water using the solution for this problem
		"""
		ind = 0

		while ind < len(self.pipes)-1:
			for x in range(ind+1, len(self.pipes)):
				pipe = self.pipes[x]
				if pipe >= self.pipes[ind]:  
					
					for p in range(ind+1,x):
						pipee = self.pipes[p]
						for y in range(pipee, min(pipe, self.pipes[ind])):
							pygame.draw.rect(self.win, self.BLUE, (p * self.inc_x, self.h - (self.inc_y * min(pipe, self.pipes[ind])), self.inc_x, self.h))
					ind = x 
					break
			else:
				large_pipe = max(self.pipes[ind+1:]) 
				pipe_ind = self.pipes[ind+1:].index(large_pipe) + ind + 1
				for p in range(ind+1,pipe_ind):
					pipee = self.pipes[p]
					pygame.draw.rect(self.win, self.BLUE, (p * self.inc_x, self.h - (self.inc_y * large_pipe), self.inc_x, self.h))  
			
				ind = pipe_ind 
			
	def show(self):
		"""
		Show pygame window
		"""
		clock = pygame.time.Clock()
		run = True

		while run:
			clock.tick(30)
			self.draw(self.water)

			# if user presses x or any key quit
			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
					run = False
					break

		pygame.quit()
