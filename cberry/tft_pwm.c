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

int main( int argc, char* argv[] )
{
   uint8_t pwm = atoi(argv[1]);
   if (!bcm2835_init())
   return 1;

   RAIO_SetBacklightPWMValue(pwm);
   return 0;
}

