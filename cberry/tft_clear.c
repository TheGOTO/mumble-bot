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
   if (!bcm2835_init())
   return 1;

   // rectangle
   Draw_Square(0, 0, 319, 239);
   Text_Foreground_Color( COLOR_BLACK );
   RAIO_StartDrawing( SQUARE_FILL );

   return 0;
}

