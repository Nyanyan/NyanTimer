#include "NyanTimer.h"
#include "Arduino.h"

//ST7032 lcd;

void NyanTimer::begin() {
  lcd.begin(16, 2);
  lcd.setContrast(40);
  lcd.setCursor(0, 0); //when power is off: print "Nyan Timer"
  lcd.print("NyanTimer       ");
  lcd.setCursor(0, 1);
  lcd.print("      by Nyanyan");
  delay(1000);
}

void NyanTimer::lightLED(int LED, bool HL) {
  _LED = LED;
  _HL = HL;
  digitalWrite(_LED, _HL);
}


void NyanTimer::setLCD(int col, int row, String str) {
  _row = row;
  _col = col;
  _str = str;
  lcd.setCursor(_col, _row);
  lcd.print(_str);
}
