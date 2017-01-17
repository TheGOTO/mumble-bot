/*##############################################################*/
/*   Reimar Barnstorf 7soft                                     */
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

   TFT_init_board();
   TFT_hard_reset();
   RAIO_init();
   return 0;
}
