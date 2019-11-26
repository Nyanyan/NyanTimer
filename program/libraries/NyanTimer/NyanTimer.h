#include "Arduino.h"

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

namespace NyanTimer {
  void begin(bool signal);
  void timing();
  void lightLED(int LED, bool HL);
  void printLCD(int row, int col, String str);
  void printLCD(int col, int row, char c);
  void startTimer(int msec, void (*f)());
  void stopTimer();
  int touch();
  void calcTime(int minute, int second, int msecond, int *output);
  String strTime(int input[]);
  bool inputButton(int n);
  void setLCDclear(int mode);
  void powersave();
  
  extern int output[7];
  extern char stat;
  volatile extern int msecond;
  extern int second;
  extern int minute;
}
