#include "NyanTimer.h"
#include <MsTimer2.h>
//#include <Wire.h>
#include <TimerOne.h>
#include <ST7032_SoftI2CMaster.h>
#include <math.h>

ST7032 lcd;

static int pad1inthreshold = 0;
static int pad2inthreshold = 0;
int NyanTimer::output[7] = {0, 0, 0, 0, 0, 0, 0};
char NyanTimer::stat;
int NyanTimer::minute;
int NyanTimer::second;
volatile int NyanTimer::msecond;
static String serout = "I000000@";
static char statout;

static void signalOut() {
  Serial.print(serout);
  Serial.print(char(13));
  Serial.print(char(10));
}

static void swap(double* a, double* b) {
  double c = *a;
  *a = *b;
  *b = c;
}

static void sort(double* array) {
  int size = sizeof(array) / sizeof(double);
  for(int i = 0;i < size;i++)
    for(int j = size - 1;j > i; j--)
      if(array[j] < array[j - 1])
        swap(&array[j], &array[j - 1]);
}

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
  int arr[9] = {0,1,2,3,9,10,11,18,19};
  for (int i = 0; i < 9; i++)
    pinMode(arr[i], OUTPUT);
  NyanTimer::stat = 'I';
  NyanTimer::minute = 0;
  NyanTimer::second = 0;
  NyanTimer::msecond = 0;

  lcd.begin(16, 2);
  lcd.setContrast(40);
  NyanTimer::printLCD(0, 0, "NyanTimer       ");
  NyanTimer::printLCD(0, 1, "      by Nyanyan");
  digitalWrite(PAD1OUT, HIGH);
  digitalWrite(PAD2OUT, HIGH);
  Timer1.initialize(125000);
  Timer1.attachInterrupt(signalOut);
  Timer1.start();
  for (int i=0;i<10;i++) {
    delay(10);
    pad1inthreshold = max(pad1inthreshold, analogRead(PAD1IN) * 0.9); //calibration
    pad2inthreshold = max(pad2inthreshold, analogRead(PAD2IN) * 0.9);
  }
  digitalWrite(PAD1OUT, LOW);
  digitalWrite(PAD2OUT, LOW);
  delay(900);
}


void NyanTimer::timing() {
  if (NyanTimer::msecond >= 1000) {
    NyanTimer::msecond -= 1000;
    NyanTimer::second++;
  }
  if (NyanTimer::second >= 60) {
    NyanTimer::second -= 60;
    NyanTimer::minute++;
  }
  if (NyanTimer::minute >= 100)
    NyanTimer::stopTimer();
  NyanTimer::calcTime(NyanTimer::minute, NyanTimer::second, NyanTimer::msecond, NyanTimer::output);
  
  if (NyanTimer::stat == 'I' && NyanTimer::touch() == 2)
    statout = 'R';
  else if (NyanTimer::stat == 'I' && NyanTimer::touch() == 3)
    statout = 'L';
  else
    statout = NyanTimer::stat;

  serout = String(statout);
  int tmp = 0;
  for (int i = 1; i < 7; i++) {
    serout += NyanTimer::output[i];
    tmp += NyanTimer::output[i];
  }
  char checksum = 64 + tmp;
  serout += String(checksum);
}

void NyanTimer::lightLED(int LED, bool HL) {
  digitalWrite(LED, HL);
}


void NyanTimer::printLCD(int col, int row, String str) {
  lcd.setCursor(col, row);
  lcd.print(str);
}

void NyanTimer::printLCD(int col, int row, char c) {
  lcd.setCursor(col, row);
  lcd.print(c);
}

void NyanTimer::startTimer(int msec, void (*f)()) {
  MsTimer2::set(msec, f);
  MsTimer2::start();
}

void NyanTimer::stopTimer() {
  MsTimer2::stop();
}

int NyanTimer::touch() {
  float touchthreshold = 500;
  const int t = 20;
  double VAL1[t];
  double VAL2[t];
  float breakthreshold = 50;
  const float exceptratio = 0.2;

  for (int i = 0; i < t; i++) {
    double val1 = 0;
    double val2 = 0;
    unsigned long tmp;
    digitalWrite(PAD1OUT, HIGH);
    tmp = micros();
    while (analogRead(PAD1IN) < pad1inthreshold) {
      val1 = micros() - tmp;
      if (val1 > breakthreshold) {
        int tim = micros() - tmp;
        int vol = analogRead(PAD1IN);
        float gamma = -log(1 - vol / (pad1inthreshold / 0.9)) / tim;
        val1 = -log(1 - 0.9) / gamma;
        break;
      }
    }
    digitalWrite(PAD1OUT, LOW);
    delayMicroseconds(100);
    digitalWrite(PAD2OUT, HIGH);
    tmp = micros();
    while (analogRead(PAD2IN) < pad2inthreshold) {
      val2 = micros() - tmp;
      if (val2 > breakthreshold) {
        int tim = micros() - tmp;
        int vol = analogRead(PAD2IN);
        float gamma = -log(1 - vol / (pad1inthreshold / 0.9)) / tim;
        val2 = -log(1 - 0.9) / gamma;
        break;
      }
    }
    digitalWrite(PAD2OUT, LOW);

    if (val1 > 0 && val2 > 0) {
      VAL1[i] = val1;
      VAL2[i] = val2;
    } else
      i--;

    delayMicroseconds(100);
  }
  sort(VAL1);
  sort(VAL2);
  int except = t * exceptratio;
  int tmp = t - 2 * except;
  float VAL1sum = 0;
  float VAL2sum = 0;
  for(int i = except; i < t - except; i++) {
    VAL1sum += VAL1[i];
    VAL2sum += VAL2[i];
  }
  //NyanTimer::printLCD(0,0,String(VAL1sum / tmp));
  //NyanTimer::printLCD(0,1,String(VAL2sum / tmp));
  //NyanTimer::printLCD(7,0,String(threshold1));
  //NyanTimer::printLCD(7,1,String(threshold2));
  if (VAL1sum >= touchthreshold * tmp && VAL2sum >= touchthreshold * tmp)
    return 1;
  else if (VAL1sum >= touchthreshold * tmp && VAL2sum < touchthreshold * tmp)
    return 2;
  else if (VAL1sum < touchthreshold * tmp && VAL2sum >= touchthreshold * tmp)
    return 3;
  else
    return 0;
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

bool NyanTimer::inputButton(int n) {
  if (digitalRead(n) == HIGH)
    return true;
  else
    return false;
}

void NyanTimer::setLCDclear(int mode) {
  if (mode == 0)
    NyanTimer::printLCD(0, 0, "                ");
  else if (mode == 1)
    NyanTimer::printLCD(0, 1, "                ");
  else if (mode == 2)
    lcd.clear();
}

void NyanTimer::powersave() {
  NyanTimer::setLCDclear(2);
  NyanTimer::lightLED(LEDR, false);
  NyanTimer::lightLED(LEDG, false);
  delay(1000);
  SMCR |= (1 << SM1);
  SMCR |= 1;
  ADCSRA &= ~(1 << ADEN);
  MCUCR |= (1 << BODSE) | (1 << BODS);
  MCUCR = (MCUCR & ~(1 << BODSE)) | (1 << BODS);
  asm("sleep");
}