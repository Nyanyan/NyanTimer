#include "NyanTimer.h"
#include "Arduino.h"
#include <MsTimer2.h>
#include <TimerOne.h>
#include <Wire.h>
#include <ST7032.h>

#define BUTTON1 6 //reset
#define BUTTON2 8 //inspection mode
#define BUTTON3 7 //lap up
#define BUTTON4 4 //lap down
#define BUZZER 5 //buzzer
#define LEDR 13 //red led
#define LEDG 12 //green led
#define PAD1OUT 15
#define PAD1IN 16
#define PAD2OUT 14
#define PAD2IN 17


void NyanTimer::lightLED(int LED, bool HL) {
  digitalWrite(LED, HL);
}
