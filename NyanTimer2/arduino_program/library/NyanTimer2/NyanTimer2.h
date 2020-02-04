#include "Arduino.h"

#define PAD1OUT 15
#define PAD1IN 16
#define PAD2OUT 14
#define PAD2IN 17

namespace NyanTimer {
  void begin();
  void timing();
  void startTimer(int msec, void (*f)());
  void stopTimer();
  int touch();
  void calcTime(int minute, int second, int msecond, int *output);
  String strTime(int input[]);
  
  extern int output[7];
  extern char stat;
  volatile extern int msecond;
  extern int second;
  extern int minute;
}
