all: build_all

build_all: tft_init.o tft_clear.o tft_close.o  tft_pwm.o tft_bmp.o tft.o RAIO8870.o bmp.o 
	gcc tft_init.o tft.o RAIO8870.o bmp.o -lbcm2835 -lrt -lm -o tft_init
	gcc tft_clear.o tft.o RAIO8870.o bmp.o -lbcm2835 -lrt -lm -o tft_clear
	gcc tft_pwm.o tft.o RAIO8870.o bmp.o -lbcm2835 -lrt -lm -o tft_pwm
	gcc tft_bmp.o tft.o RAIO8870.o bmp.o -lbcm2835 -lrt -lm -o tft_bmp
	gcc tft_close.o tft.o RAIO8870.o bmp.o -lbcm2835 -lrt -lm -o tft_close
		

tft.o: tft.c tft.h
	gcc -Os -c tft.c
	
RAIO8870.o: RAIO8870.c RAIO8870.h
	gcc -Os -c RAIO8870.c

bmp.o: bmp.c bmp.h RAIO8870.h
	gcc -Os -c bmp.c
	
tft_init.o: tft_init.c 
	gcc -Os -c tft_init.c
	
tft_clear.o: tft_clear.c 
	gcc -Os -c tft_clear.c

tft_close.o: tft_close.c 
	gcc -Os -c tft_close.c
	
tft_pwm.o: tft_pwm.c 
	gcc -Os -c tft_pwm.c
	
tft_bmp.o: tft_pwm.c 
	gcc -Os -c tft_bmp.c

clean:
	rm -rf *o tft_bmp
	rm -rf *o tft_clear
	rm -rf *o tft_close
	rm -rf *o tft_init
	rm -rf *o tft_pwm

