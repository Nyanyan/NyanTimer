#ifndef _functions_h
#define _functions_h
#include "Arduino.h"

namespace NyanTimer {
  void bgn();
  void lightLED(int LED, bool HL);
  void printLCD(int row, int col, String str);
  void startTimer(int msec, void (*f)());
  void stopTimer();
  int touch(int mode);
  void signalOut(int output[], String statout);
  void signalBegin(void (*f)());
  void calcTime(int minute, int second, int msecond, int *output);
  String strTime(int input[]);
  bool button(int n);
}
