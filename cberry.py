#!/usr/bin/python
# -*- coding: utf-8 -*-

#****************************************************
#   Reimar Barnstorf www.7soft.de                   *
#****************************************************

# Python Imports
import os
import pygame
import sys
import time


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

lib_root="/home/pi/devel/C-Berry/SW/python/"
line_offset=15
font_size=16
font_size_bottom=14
bmp_file="/home/pi/devel/mumble_bot/temp.bmp"

class Cberry:	
	window=None
	font1=None
	font2=None
	font3=None
	current_line_pos=0

	def __init__(self, filename=None):

		os.environ["SDL_VIDEODRIVER"] = "dummy"
		
		pygame.font.init()
		
		self.window = pygame.display.set_mode((320,240),0,24)#c-berry need 24 bit bmp
		
		self.font1 = pygame.font.SysFont("droidsans", font_size)
		self.font1.set_bold(1)
		self.font2 = pygame.font.SysFont("droidsans",font_size_bottom)
		self.font2.set_bold(1)
		
	def turn_screen_on(self):
		os.system(lib_root+"tft_init")
		self.clear_screen()
		os.system(lib_root+"tft_pwm 10")
		
	def turn_screen_off(self):
		os.system(lib_root+"tft_close")
		return

	def print_on_screen(self,online_users,ip,cert_exp):		
		lt = time.localtime()			
		self.window.fill(BLACK)		
		
		self.print_line("Date: " +time.strftime("%d/%m/%Y", lt))
		self.print_line("Time: " +time.strftime("%H:%M:%S", lt))
		self.print_line("IP: "+ip)
		self.print_line("")		
		
		for user in online_users:
			if online_users[user]%2!=0:
				color="online"
				pygame.draw.circle(self.window, GREEN, (150,self.current_line_pos+line_offset/2), 6)
			else:
				color="offline"
				pygame.draw.circle(self.window, GREEN, (150,self.current_line_pos+line_offset/2), 6, 1)
			   
			self.print_line(user)
			
				
		self.print_line("Cert validity : "+cert_exp,self.font2,200)
			
			
		pygame.image.save(self.window, bmp_file)#generate image		
		os.system(lib_root+"tft_bmp "+bmp_file)	#show image
		self.current_line_pos=0

	def print_line(self,line,font=None,pos=0):		
		global current_line_pos
		
		position=self.current_line_pos
		
		if font==None:
			font=self.font1
			
		if pos!=0:		
			position=pos
			
		label2 = font.render(line.encode('utf-8'), True, WHITE,BLACK)	
		self.window.blit(label2, (0,position))
		self.current_line_pos=self.current_line_pos+line_offset		

	def clear_screen(self):
		os.system(lib_root+"tft_clear")
		return
		
	



