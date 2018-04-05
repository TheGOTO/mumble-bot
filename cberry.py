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
from signal import alarm, signal, SIGALRM, SIGKILL




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

lib_root="/home/pi/devel/mumble-bot/cberry/"
line_offset=16
font_size=16
font_size_bottom=14
bmp_file="/home/pi/devel/mumble-bot/img/temp.bmp"
image_file=bmp_file[:-4]


class Cberry:	
	window=None
	font1=None
	font2=None
	font3=None
	current_line_pos=0
	

	def __init__(self, filename=None):

		os.environ["SDL_VIDEODRIVER"] = "dummy"
		
		pygame.font.init()
		
		# this section is an unbelievable nasty hack - for some reason Pygame
		# needs a keyboardinterrupt to initialise in some limited circs (second time running)
		class Alarm(Exception):
			pass
		def alarm_handler(signum, frame):
			raise Alarm
		signal(SIGALRM, alarm_handler)
		alarm(3)
		try:
			#pygame.init()
			self.window = pygame.display.set_mode((320,240),0,24)#c-berry need 24 bit bmp
			alarm(0)
		except Alarm:
			raise KeyboardInterrupt

		self.window = pygame.display.set_mode((320,240),0,24)#c-berry need 24 bit bmp
		
		#print("pygame initalized")
		
		self.font1 = pygame.font.SysFont("dejavusans", font_size)
		#self.font1.set_bold(1)
		self.font2 = pygame.font.SysFont("dejavusansmono",font_size_bottom)
		#self.font2.set_bold(1)
		
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
		self.print_line("PbtH Mumble-Bot")
		self.next_line()
		self.next_line()
		self.print_line("Date/Time: "+time.strftime("%Y-%m-%d", lt)+" "+time.strftime("%H:%M:%S", lt))		
		self.next_line()
		#self.print_line(ip)
		#self.next_line()
		self.next_line()
				
		
		for user in online_users:
			user_obj=online_users[user]
			
			self.print_line(user_obj.name)
			

			if user_obj.event_counter%2!=0:
				color="online"
				pygame.draw.circle(self.window, GREEN, (100,int(self.current_line_pos+line_offset/2)), 6)
				self.print_line(user_obj.last_active,self.font2,0,110,GREEN)
				
			else:
				color="offline"
				pygame.draw.circle(self.window, WHITE, (100,int(self.current_line_pos+line_offset/2)), 6, 1)
				self.print_line(user_obj.last_active,self.font2,0,110)
			

			self.next_line()
				
		self.print_line("Certificate: "+cert_exp,self.font1,200)
			
			
		pygame.image.save(self.window, bmp_file)#generate image		
		os.system(lib_root+"tft_bmp "+bmp_file)	#show image
		self.current_line_pos=0

	def next_line(self):
		self.current_line_pos=self.current_line_pos+line_offset	

	def print_line(self,line,font=None,y_pos=0,x_pos=0,color=WHITE):		
		global current_line_pos		
		
		if font==None:
			font=self.font1
			
		if y_pos==0:		
			y_pos=self.current_line_pos

		line=self.replace_special_chars(line)
			
		label2 = font.render(line.encode('utf-8'), True, color,BLACK)	
		self.window.blit(label2, (x_pos,y_pos))

	def replace_special_chars(self,value):

		value=value.replace(u'ü', 'ue')
		value=value.replace(u'ß', 'ss')
		value=value.replace(u'ö', 'oe')
		value=value.replace(u'ä', 'ae')	
		return value

	def clear_screen(self):
		os.system(lib_root+"tft_clear")
		return
		

		
	



