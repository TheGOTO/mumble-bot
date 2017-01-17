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
  {
	printf("could not init");
   return 1;
  }
  
  RAIO_SetRegister( P1CR, 0x88 ); 	 // Enable PWM1 output devider 256
  RAIO_SetRegister( P1DCR, 0 ); // -> BL_vaue = 0 (0% PWM) - 255 (100% PWM)

  RAIO_SetRegister(PWRR,0x00);//turn of

	if (!bcm2835_close()) { // close the interface
     printf("could not close");
    }
	 

   return 0;
}



