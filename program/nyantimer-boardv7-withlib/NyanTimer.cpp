#include "NyanTimer.h"
#include "Arduino.h"
/*
#include <MsTimer2.h>
#include <TimerOne.h>
#include <Wire.h>
#include <ST7032.h>
*/


void NyanTimer::lightLED(int LED, bool HL) {
  _LED = LED;
  _HL = HL;
  digitalWrite(_LED, _HL);
}

void NyanTimer::setLCD(int row, int col, char str) {
  _row = row;
  _col = col;
  _str = str;
  lcd.setCursor(_row, _col);
  lcd.print(_str);
}
