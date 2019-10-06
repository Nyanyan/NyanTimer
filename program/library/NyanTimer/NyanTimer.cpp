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

  digitalWrite(PAD1OUT, HIGH);
  digitalWrite(PAD2OUT, HIGH);
  lcd.begin(16, 2);
  lcd.setContrast(40);
  lcd.setCursor(0, 0); //when power is off: print "Nyan Timer"
  lcd.print("NyanTimer       ");
  lcd.setCursor(0, 1);
  lcd.print("      by Nyanyan");
  delay(1000);
  pad1inthreshold = analogRead(PAD1IN) * 0.8; //calibration
  pad2inthreshold = analogRead(PAD2IN) * 0.8;
  digitalWrite(PAD1OUT, LOW);
  digitalWrite(PAD2OUT, LOW);
}

void NyanTimer::lightLED(int LED, bool HL) {
  digitalWrite(LED, HL);
}


void NyanTimer::printLCD(int col, int row, String str) {
  lcd.setCursor(col, row);
  lcd.print(str);
}

void NyanTimer::startTimer(int mode, int msec, void (*f)()) {
  if (mode == 1) {
    Timer1.initialize(msec * 1000);
    Timer1.attachInterrupt(f);
    Timer1.start();
  } else if (mode == 2) {
    MsTimer2::set(msec, f);
    MsTimer2::start();
  }
}

void NyanTimer::stopTimer(int mode) {
  if (mode == 1) {
    Timer1.stop();
  } else if (mode == 2) {
    MsTimer2::stop();
  }
}

int NyanTimer::touch(int mode) {
  float threshold = 20;
  float t = 4;
  float k = 0.5;
  float VAL1 = 0;
  float VAL2 = 0;

  for (int i = 0; i < t; i++) {
    float val1 = 0;
    float val2 = 0;
    digitalWrite(PAD1OUT, HIGH);
    while (analogRead(PAD1IN) < pad1inthreshold) {
      val1++;
      if (val1 > threshold)
        break;
    }
    digitalWrite(PAD1OUT, LOW);

    digitalWrite(PAD2OUT, HIGH);
    while (analogRead(PAD2IN) < pad2inthreshold) {
      val2++;
      if (val2 > threshold)
        break;
    }
    digitalWrite(PAD2OUT, LOW);
    if (val1 > 0 && val2 > 0) {
      VAL1 += val1;
      VAL2 += val2;
    } else
      i--;

    delayMicroseconds(5);
  }
  if (mode == 0) {
    if (VAL1 > threshold * t * k && VAL2 > threshold * t * k)
      return 1;
    else
      return 0;
  } else {
    if (VAL1 > threshold * t * k && VAL2 > threshold * t * k)
      return 1;
    else if (VAL1 >= threshold * t * k && VAL2 < threshold * t * k)
      return 2;
    else if (VAL1 < threshold * t * k && VAL2 >= threshold * t * k)
      return 3;
    else
      return 0;
  }
}

void NyanTimer::signalOut() {
  String serout = statout;
  for (int i = 1; i < 7; i++)
    serout += output[i];
  int tmp = 0;
  for (int i = 1; i < 7; i++) {
    tmp += output[i];
  }
  char checksum = 64 + tmp;
  serout += String(checksum);
  Serial.print(serout);
  Serial.print(char(13));
  Serial.print(char(10));
}