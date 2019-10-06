#include "NyanTimer.h"
#include "Arduino.h"

ST7032 lcd;

void NyanTimer::begin() {
  Serial.begin(1200);
  pinMode(BUTTON1, INPUT);
  pinMode(BUTTON2, INPUT);
  pinMode(BUTTON3, INPUT);
  pinMode(BUTTON4, INPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(PAD1OUT, OUTPUT);
  pinMode(PAD2OUT, OUTPUT);
  pinMode(PAD1IN, INPUT);
  pinMode(PAD2IN, INPUT);
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


void NyanTimer::printLCD(int col, int row, String str) {
  _row = row;
  _col = col;
  _str = str;
  lcd.setCursor(_col, _row);
  lcd.print(_str);
}

void NyanTimer::startTimer(int mode, int msec, void (*f)()) {
  _mode = mode;
  _msec = msec;
  _f = f;
  if (mode == 1) {
    Timer1.initialize(_msec * 1000);
    Timer1.attachInterrupt(_f);
    Timer1.start();
  } else if (mode == 2) {
    MsTimer2::set(_msec, _f);
    MsTimer2::start();
  }
}

void NyanTimer::stopTimer(int mode) {
  _mode = mode;
  if (mode == 1) {
    Timer1.stop();
  } else if (mode == 2) {
    MsTimer2::stop();
  }
}