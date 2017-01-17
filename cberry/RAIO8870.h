/*##############################################################*/
/* 																*/
/* File		: RAIO8870.h										*/
/*																*/
/* Project	: TFT for Raspberry Pi Revision 2					*/
/* 																*/
/* Date		: 2013-11-22   	    last update: 2014-02-28			*/
/* 																*/
/* Author	: Hagen Ploog   									*/
/*		  	  Kai Gillmann										*/
/*		  	  Timo Pfander										*/
/* 																*/
/* IDE	 	: Geany 1.22										*/
/* Compiler : gcc (Debian 4.6.3-14+rpi1) 4.6.3					*/
/*																*/
/* Copyright (C) 2013 admatec GmbH								*/
/*																*/
/*																*/	
/* Description  :												*/
/* 																*/
/*	This file contains the defines of the RAIO register.		*/
/*	Furthermore declared the file several functions to control	*/
/*	the graphic controller RAIO8870.							*/
/*																*/
/*	There can two different color depths to be set for the BMP	*/
/*	output. It can be changed behind the line color modes.		*/
/*																*/
/*																*/
/* License:														*/
/*																*/
/*	This program is free software; you can redistribute it 		*/ 
/*	and/or modify it under the terms of the GNU General			*/ 	
/*	Public License as published by the Free Software 			*/
/*	Foundation; either version 3 of the License, or 			*/
/*	(at your option) any later version. 						*/
/*    															*/
/*	This program is distributed in the hope that it will 		*/
/*	be useful, but WITHOUT ANY WARRANTY; without even the 		*/
/*	implied warranty of MERCHANTABILITY or 						*/
/*	FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 		*/
/*	Public License for more details. 							*/
/*																*/
/*	You should have received a copy of the GNU General 			*/
/*	Public License along with this program; if not, 			*/
/*	see <http://www.gnu.org/licenses/>.							*/
/*																*/
/*																*/
/* Revision History:											*/
/*																*/
/*	Version 1.0 - Initial release								*/
/*	Version 1.1 - added function RAIO_clear_screen( ... )		*/
/*				  added function RAIO_SetFontSizeFactor( ... )	*/
/*				  added function RAIO_print_text( ... )			*/
/*																*/
/*																*/
/*																*/
/*##############################################################*/

#ifndef RAIO8870_H
#define RAIO8870_H

#include <stdint.h>


//color modes (color depths) { CM_4K=0, CM_65K };
#define CM_65K


// TFT dimensions
#define DISPLAY_WIDTH  320
#define DISPLAY_HEIGHT 240
#define PICTURE_PIXELS ( DISPLAY_WIDTH*DISPLAY_HEIGHT )


// RAIO register -> see datasheet RAIO8870
#define PCOD 0x00
#define PWRR 0x01
#define MRWC 0x02
#define PCLK 0x04

#define SYSR 0x10
#define DRGB 0x11
#define IOCR 0x12
#define IODR 0x13

#define HDWR  0x14
#define HNDFTR 0x15
#define HNDR  0x16
#define HSTR  0x17
#define HPWR  0x18

#define VDHR0 0x19
#define VDHR1 0x1a
#define VNDR0 0x1b
#define VNDR1 0x1c
#define VSTR0 0x1d
#define VSTR1 0x1e
#define VPWR  0x1f

#define DPCR  0x20
#define FNCR0 0x21
#define FNCR1 0x22
#define CGSR  0x23
#define HOFS0 0x24
#define HOFS1 0x25
#define VOFS0 0x26
#define VOFS1 0x27
#define ROMS  0x28

#define FLDR  0x29

#define HSAW0 0x30
#define HSAW1 0x31
#define VSAW0 0x32
#define VSAW1 0x33
#define HEAW0 0x34
#define HEAW1 0x35
#define VEAW0 0x36
#define VEAW1 0x37
#define HSSW0 0x38
#define HSSW1 0x39
#define VSSW0 0x3a
#define VSSW1 0x3b
#define HESW0 0x3c
#define HESW1 0x3d
#define VESW0 0x3e
#define VESW1 0x3f

#define MWCR0 0x40
#define MWCR1 0x41
#define TFCR  0x42
#define TBCR  0x43
#define BTCR  0x44
#define CURS  0x45
#define CURH0 0x46
#define CURH1 0x47
#define CURV0 0x48
#define CURV1 0x49
#define RCURH0 0x4a
#define RCURH01 0x4b
#define RCURV0 0x4c
#define RCURV1 0x4d
#define MRCD  0x4e
#define BECR0 0x50
#define BECR1 0x51
#define LTPR0 0x52
#define LTPR1 0x53
#define HSBE0 0x54
#define HSBE1 0x55
#define VSBE0 0x56
#define VSBE1 0x57
#define HDBE0 0x58
#define HDBE1 0x59
#define VDBE0 0x5a
#define VDBE1 0x5b
#define BEWR0 0x5c
#define BEWR1 0x5d
#define BEHR0 0x5e
#define BEHR1 0x5f

#define BGCR0 0x60
#define BGCR1 0x61
#define BGCR2 0x62
#define FGCR0 0x63
#define FGCR1 0x64
#define FGCR2 0x65
#define PTNO  0x66
#define BGTR  0x67

#define TPCR0 0x70
#define TPCR1 0x71
#define TPXH  0x72
#define TPYH  0x73
#define TPXYL 0x74

#define GCHP0 0x80
#define GCHP1 0x81
#define GCVP0 0x82
#define GCVP1 0x83
#define GCC0  0x84
#define GCC1  0x85

#define PLLC1 0x88
#define PLLC2 0x89

#define P1CR  0x8a
#define P1DCR 0x8b
#define P2CR  0x8c
#define P2DCR 0x8d
#define MCLR  0x8e
#define INTC  0x8f

#define DCR   0x90
#define DLHSR0 0x91
#define DLHSR1 0x92
#define DLVSR0 0x93
#define DLVSR1 0x94
#define DLHER0 0x95
#define DLHER1 0x96
#define DLVER0 0x97
#define DLVER1 0x98
#define DCHR0  0x99
#define DCHR1 0x9a
#define DCVR0 0x9b
#define DCVR1 0x9c
#define DCRR  0x9d

#define TCR1 0xa0
#define TCR2 0xa1
#define OEHTCR1 0xa2
#define OEHTCR2 0xa3
#define OEHTCR3 0xa4
#define OEHTCR4 0xa5
#define OEHTCR5 0xa6
#define OEHTCR6 0xa7
#define OEHTCR7 0xa8
#define OEHTCR8 0xa9

#define STHTCR1 0xaa
#define STHTCR2 0xab
#define STHTCR3 0xac
#define STHTCR4 0xad

#define Q1HCR1 0xae
#define Q1HCR2 0xaf

#define OEVTCR1 0xb0
#define OEVTCR2 0xb1
#define OEVTCR3 0xb2
#define OEVTCR4 0xb3
#define CKVTCR1 0xb4
#define CKVTCR2 0xb5
#define CKVTCR3 0xb6
#define CKVTCR4 0xb7
#define STVTCR1 0xb8
#define STVTCR2 0xb9
#define STVTCR3 0xba
#define STVTCR4 0xbb
#define STVTCR5 0xbc
#define STVTCR6 0xbd
#define STVTCR7 0xbe
#define STVTCR8 0xbf

#define COMTCR1 0xc0
#define COMTCR2 0xc1
#define RGBTCR1 0xc2
#define RGBTCR2 0xc3


// colors "RRRGGGBB"
#define COLOR_RED       0xE0
#define COLOR_BLUE      0x03
#define COLOR_GREEN     0x1C
#define COLOR_BLACK     0x00
#define COLOR_WHITE     0xFF
#define COLOR_CYAN      0x1F 
#define COLOR_YELLOW    0xFC
#define COLOR_MAGENTA   0xE3
#define COLOR_DARK_GREEN 0x0C


// ROP functions
#define ROP_SOURCE  0xC


// BTE operation functions
#define BTE_MOVE_POSITIVE   0x02
#define BTE_SOLID_FILL      0x0C


// declaration of a union (used in RAIO8870.c and tft.c)
// ----------------------------------------------------------
union my_union
{
	uint32_t value;
	struct
	{
		unsigned char low;
		unsigned char high;
	} split;
};


// enumeration of drawing modes
// ----------------------------------------------------------
enum DRAW_MODES { CIRCLE_NONFILL, CIRCLE_FILL, SQUARE_NONFILL, SQUARE_FILL, LINE};


// initialization of RAIO8870
// ----------------------------------------------------------
void RAIO_init( void );


// write command to a register
// ----------------------------------------------------------
void RAIO_SetRegister( uint8_t reg, uint8_t value );


// set PWM value for backlight -> 0 (0% PWM) - 255 (100% PWM)
// ----------------------------------------------------------
void RAIO_SetBacklightPWMValue( uint8_t BL_value );


// set coordinates for active window
// ----------------------------------------------------------
void Active_Window(uint16_t XL,uint16_t XR ,uint16_t YT ,uint16_t YB);


// set mode for BET (Block Transfer Engine)
// ----------------------------------------------------------
void BTE_mode( uint8_t bte_operation, uint8_t rop_function );


// set color -> see color defines
// ----------------------------------------------------------
void Text_Background_Color( uint8_t color );
void Text_Foreground_Color( uint8_t color );


// clear memory
// ----------------------------------------------------------
void RAIO_clear_screen( void );


// set coordinates for drawing
// ----------------------------------------------------------
void Set_Geometric_Coordinate( uint16_t X1, uint16_t Y1 ,uint16_t X2 ,uint16_t Y2 );
void Set_Geometric_Coordinate_circle (uint16_t X1, uint16_t Y1 ,uint8_t rad );

// show the BMP picture on the TFT screen
// ----------------------------------------------------------
void RAIO_Write_Picture( uint16_t *data, uint32_t count );


// set draw mode -> see DRAW_MODES
// ----------------------------------------------------------  
void RAIO_StartDrawing( int16_t whattodraw );


// draw some basic geometrical forms
// ----------------------------------------------------------  
void Draw_Line( uint16_t X1, uint16_t Y1 ,uint16_t X2 ,uint16_t Y2 );
void Draw_Square( uint16_t X1, uint16_t Y1 ,uint16_t X2 ,uint16_t Y2 );


// print text
// ----------------------------------------------------------
void RAIO_print_text( uint16_t pos_x, uint16_t pos_y, unsigned char *str, uint8_t BG_color, uint8_t FG_color );


// set font size
// ----------------------------------------------------------
void RAIO_SetFontSizeFactor( uint8_t size );


#endif
