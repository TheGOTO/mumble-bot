/*##############################################################*/
/*   Reimar Barnstorf                                           */
/*##############################################################*/

#include <bcm2835.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include "tft.h"
#include "RAIO8870.h"
#include "bmp.h"

int main( int argc, char *argv[] )
{
   uint16_t picture[1][ PICTURE_PIXELS ];

   if (!bcm2835_init())
   return 1;

   // depict a BMP file
   // ---------------------------------------------
   Read_bmp2memory ( argv[1], &picture[0][ PICTURE_PIXELS-1 ] );
   RAIO_Write_Picture( &picture[0][0], PICTURE_PIXELS );
   return 0;
}

