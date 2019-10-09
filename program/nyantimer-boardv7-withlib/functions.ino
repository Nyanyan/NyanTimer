#include "functions.h"
#include <MsTimer2.h>
#include <TimerOne.h>
#include <Wire.h>
#include <ST7032.h>

ST7032 lcd;

int pad1inthreshold;
int pad2inthreshold;
int output[7] = {0, 0, 0, 0, 0, 0, 0};
String statout;

static void signalOut() {
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


void NyanTimer::bgn() {
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
  lcd.setCursor(0, 0);
  lcd.print("NyanTimer       ");
  lcd.setCursor(0, 1);
  lcd.print("      by Nyanyan");
  delay(1000);
  pad1inthreshold = analogRead(PAD1IN) * 0.8; //calibration
  pad2inthreshold = analogRead(PAD2IN) * 0.8;
  digitalWrite(PAD1OUT, LOW);
  digitalWrite(PAD2OUT, LOW);
  Timer1.initialize(125000);
  Timer1.attachInterrupt(signalOut);
  Timer1.start();
}

void NyanTimer::lightLED(int LED, bool HL) {
  digitalWrite(LED, HL);
}


void NyanTimer::printLCD(int col, int row, String str) {
  lcd.setCursor(col, row);
  lcd.print(str);
}

void NyanTimer::startTimer(int msec, void (*f)()) {
  MsTimer2::set(msec, f);
  MsTimer2::start();
}

void NyanTimer::stopTimer() {
  MsTimer2::stop();
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

void NyanTimer::calcTime(int minute, int second, int msecond, int *output) {
  int a[7];
  a[0] = int(minute / 10);
  a[1] = minute - a[0] * 10;
  a[2] = int(second / 10);
  a[3] = second - a[2] * 10;
  a[4] = int(msecond / 100);
  a[5] = int(msecond / 10) - a[4] * 10;
  a[6] = msecond - a[4] * 100 - a[5] * 10;
  for (int i = 0; i < 7; i++) {
    *output = a[i];
    ++output;
  }
}

String NyanTimer::strTime(int input[]) {
  return String(input[0]) + String(input[1]) + ':' + String(input[2]) + String(input[3]) + '.' + String(input[4]) + String(input[5]) + String(input[6]);
}

bool NyanTimer::button(int n) {
  if (digitalRead(n) == HIGH)
    return true;
  else
    return false;
}
