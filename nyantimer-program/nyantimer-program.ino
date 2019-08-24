#include <MsTimer2.h>
#include <TimerOne.h>
#include <Wire.h>
#include <ST7032.h>

ST7032 lcd;

#define BUTTON1 6 //reset
#define BUTTON2 8 //inspection mode
#define BUTTON3 7 //lap up
#define BUTTON4 4 //lap down
#define BUZZER 14 //buzzer
#define LEDR 13 //red led
#define LEDG 12 //green led
#define PAD1OUT 15
#define PAD1IN 2
#define PAD2OUT 5
#define PAD2IN 17

int minute, second, msecond = 0;
int output[7] = {0, 0, 0, 0, 0, 0, 0};
char stat = 'I'; //status
bool ledr = 0; //red led status
bool ledg = 0; //green led status
int inspmode = 0; //0:off 1:sndOFF 2:sndON
int lapmode = 1;
int lapcount = 0;
const int maxlap = 99;
int lap[maxlap + 1][3];
int inspstat = 0; //1=during inspstatection time
int inspstatcount = 16; //inspstatection time count
bool buz = 0;
long batterycount = 0;
const long batterythreshold = 60000; //1000 per 30s
String statout;

void setup() {
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

  resettime();

  lcd.setCursor(0, 0); //when power is off: print "Nyan Timer"
  lcd.print("NyanTimer       ");
  lcd.setCursor(0, 1);
  lcd.print("      by Nyanyan");
  delay(1000);
  setLCDclear(2);
  MsTimer2::set(125, out);
  MsTimer2::start();
  lap[0][0] = 0;
  lap[0][1] = 0;
  lap[0][2] = 0;
}


void out() { //serial output, every 125msec
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


void inspection() {
  inspstatcount--;
}




void count() { //every 1 msec
  msecond++;
  if (msecond == 1000) {
    msecond = 0;
    second++;
  }
  if (second == 60) {
    second = 0;
    minute++;
  }
  if (stat == ' ' && msecond % 100 == 0) {
    ledg = ledr;
    ledr = !ledr;
  }
  if (minute >= 100)
    Timer1.stop();
  output[0] = int(minute / 10);
  output[1] = minute - output[0] * 10;
  output[2] = int(second / 10);
  output[3] = second - output[2] * 10;
  output[4] = int(msecond / 100);
  output[5] = int(msecond / 10) - output[4] * 10;
  output[6] = msecond - output[4] * 100 - output[5] * 10;
}





void convertLCD() {
  lcd.setCursor(7, 0); //print time
  String lcdouta = String(output[0]) + String(output[1]) + ':' + String(output[2]) + String(output[3]) + '.' + String(output[4]) + String(output[5]) + String(output[6]);
  lcd.print(lcdouta);

  lcd.setCursor(7, 1); //print lap time
  String lcdoutb;
  if (lapcount >= 1) {
    int a[7];
    int t;
    if (stat == 'I')
      t = lapcount + 1;
    else
      t = lapcount;
    a[0] = lap[t][0] / 10;
    a[1] = lap[t][0] - a[0] * 10;
    a[2] = lap[t][1] / 10;
    a[3] = lap[t][1] - a[2] * 10;
    a[4] = lap[t][2] / 100;
    a[5] = lap[t][2] / 10 - a[4] * 10;
    a[6] = lap[t][2] - a[4] * 100 - a[5] * 10;
    lcdoutb = String(a[0]) + String(a[1]) + ':' + String(a[2]) + String(a[3]) + '.' + String(a[4]) + String(a[5]) + String(a[6]);
  } else
    lcdoutb = "         ";
  lcd.print(lcdoutb);

  if (inspstat == 0) {
    lcd.setCursor(0, 0); //print mode & status
    if (inspmode == 1)
      lcd.print("I     ");
    else if (inspmode == 2)
      lcd.print("Is    ");
    else if (inspmode == 0)
      lcd.print("      ");
  }
  lcd.setCursor(0, 1);
  lcd.print("L");
  lcd.setCursor(1, 1);
  lcd.print(int(lapcount / 10));
  lcd.setCursor(2, 1);
  lcd.print(lapcount - int(lapcount / 10) * 10);
  lcd.setCursor(3, 1);
  lcd.print("/");
  lcd.setCursor(4, 1);
  lcd.print(int(lapmode / 10));
  lcd.setCursor(5, 1);
  lcd.print(lapmode - int(lapmode / 10) * 10);
}



void convertLED() {
  digitalWrite(LEDR, ledr);
  digitalWrite(LEDG, ledg);
}




int touch(int mode) {
  float threshold = 20;
  float VAL1 = 0;
  float VAL2 = 0;
  float t = 20;
  float k = 0.9;
  for (int i = 0; i < t; i++) {
    float val1 = 0;
    float val2 = 0;
    digitalWrite(PAD1OUT, HIGH);
    while (digitalRead(PAD1IN) == LOW) {
      val1++;
      if (val1 > threshold)
        break;
    }
    digitalWrite(PAD1OUT, LOW);

    digitalWrite(PAD2OUT, HIGH);
    while (digitalRead(PAD2IN) == LOW) {
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

    delayMicroseconds(400);
  }
  /*
    lcd.setCursor(0, 0);
    lcd.print(VAL1 / t);
  */
  if (mode == 0) {
    if (VAL1 > threshold * t * k && VAL2 > threshold * t * k)
      return 1;
    else
      return 0;
  } else {
    if (VAL1 > threshold * t * k && VAL2 > threshold * t * k)
      return 1;
    else if (VAL1 > threshold * t * k && VAL2 <= threshold * t * k)
      return 2;
    else if (VAL1 <= threshold * t * k && VAL2 > threshold * t * k)
      return 3;
    else
      return 0;
  }

}

void resettime() {
  minute = 0;
  second = 0;
  msecond = 0;
  for (int i = 0; i < 7; i++)
    output[i] = 0;
  for (int i = 0; i < maxlap; i++) {
    for (int j = 0; j < 3; j++)
      lap[i][j] = 0;
  }
  lapcount = 0;
}


void lapUP() {
  if (stat == 'I') {
    lapmode++;
    if (lapmode > maxlap)
      lapmode = 1;
  } else if (stat == 'S') {
    lapcount++;
    if (lapcount > lapmode) {
      lapcount = 1;
    }
  }
}

void lapDOWN() {
  if (stat == 'I') {
    lapmode--;
    if (lapmode < 1)
      lapmode = maxlap;
  } else if (stat == 'S') {
    lapcount--;
    if (lapcount < 1)
      lapcount = lapmode;
  }
}

void setLCDclear(int m) {
  if (m == 0 || m == 2) {
    lcd.setCursor(0, 0);
    lcd.print("                ");
  }
  if (m == 1 || m == 2) {
    lcd.setCursor(0, 1);
    lcd.print("                ");
  }
}

void button() {
  if (digitalRead(BUTTON1) == HIGH) {//reset
    batterycount = 0;
    stat = 'I';
    Timer1.stop();
    //resettime();
  } else if (digitalRead(BUTTON2) == HIGH) { //inspstatection mode
    batterycount = 0;
    inspmode += 1;
    if (inspmode > 2)
      inspmode = 0;
    while (digitalRead(BUTTON2) == HIGH);
  } else if (digitalRead(BUTTON3) == HIGH) { //lap mode up
    batterycount = 0;
    lapUP();
    convertLCD();
    bool flag = false;
    for (int i = 0; i < 1000; i++) {
      if (digitalRead(BUTTON3) == LOW)
        break;
      delay(1);
    }
    while (digitalRead(BUTTON3) == HIGH) {
      lapUP();
      delay(100);
      convertLCD();
    }
  } else if (digitalRead(BUTTON4) == HIGH) { //lap mode down
    batterycount = 0;
    lapDOWN();
    convertLCD();
    bool flag = false;
    for (int i = 0; i < 1000; i++) {
      if (digitalRead(BUTTON4) == LOW)
        break;
      delay(1);
    }
    while (digitalRead(BUTTON4) == HIGH) {
      lapDOWN();
      delay(100);
      convertLCD();
    }
  } else if (stat == 'I')
    batterycount++;
}



void timer() {
  if (touch(0) == 1) {

    if (stat == ' ') { //when timer stops
      if (lapcount == lapmode - 1) {
        stat = 'S';
        Timer1.stop();
        ledr = 0;
        ledg = 0;
      }
      lapcount++;
      lap[lapcount][0] = minute;
      lap[lapcount][1] = second;
      lap[lapcount][2] = msecond;
      for (int i = lapcount - 1; i >= 0; i--) {
        lap[lapcount][0] -= lap[i][0];
        lap[lapcount][1] -= lap[i][1];
        lap[lapcount][2] -= lap[i][2];
        if (lap[lapcount][1] < 0) {
          lap[lapcount][1] += 60;
          lap[lapcount][0]--;
        }
        if (lap[lapcount][2] < 0) {
          if (lap[lapcount][1] == 0) {
            lap[lapcount][1] += 60;
            lap[lapcount][0]--;
          }
          lap[lapcount][2] += 1000;
          lap[lapcount][1]--;
        }
      }
      bool touchflag = true;
      while (touchflag == true) {
        int cnt = 0;
        int touchthreshold = 20;
        for (cnt = 0; cnt <= touchthreshold; cnt++) {
          if (touch(0) == 1)
            break;
        }
        if (cnt >= touchthreshold)
          touchflag = false;
      }


    } else if (stat == 'I') { //timer ready to start
      if (inspmode == 0 || (inspmode == 1 && inspstat == 2) || (inspmode == 2 && inspstat == 2)) { //not inspstatection mode
        int i = 0;
        ledr = 1;
        ledg = 0;
        convertLED();
        while (touch(0) == 1 && i < 20) { //wait about 0.55sec
          i++;
          delay(1);
        }
        if (i >= 20)  //timer is able to start
          stat = 'A';
      } else if ((inspmode == 1 && inspstat == 0) || (inspmode == 2 && inspstat == 0)) { //inspstatection mode
        int i = 0;
        while (touch(0) == 1 && i < 20) { //wait about 0.55sec
          i++;
          delay(1);
        }
        ledr = 1;
        ledg = 0;
        convertLED();
        if (i >= 20)  //timer is able to start
          inspstat = 1;
        while (touch(0) == 1);
        ledr = 0;
        ledg = 0;
        convertLED();
      }
    }
  }




  else { //when pads are open


    if (stat == 'A') { //start solving
      stat = ' ';
      inspstat = 0;
      Timer1.stop();
      Timer1.initialize(1000);
      Timer1.attachInterrupt(count);
      Timer1.start();
      setLCDclear(1);
      while (touch(0) == 1);
    }


    else if (stat == 'I' && inspstat == 1) { //inspection time starts
      Timer1.stop();
      while (touch(0) == 1);
      Timer1.initialize(1000000);
      Timer1.attachInterrupt(inspection);
      Timer1.start();
      inspstatcount = 16;
      lcd.setCursor(3, 0);
      lcd.print(String(15));
      inspstat = 2;
    }
  }





  if (stat == 'I' && inspstat == 2) {

    if (inspstatcount > 0) {
      String inspstatcountstr = String(int(inspstatcount / 10)) + String(inspstatcount - 10 * int(inspstatcount / 10));
      lcd.setCursor(3, 0);
      lcd.print(inspstatcountstr);
    } else if (inspstatcount > -2) {
      lcd.setCursor(3, 0);
      lcd.print("+2");
    } else {
      lcd.setCursor(3, 0);
      lcd.print("DNF");
      Timer1.stop();
    }

    if (inspmode == 2) {
      if (inspstatcount == 7 || inspstatcount == 3)
        buz = 1;
      else
        buz = 0;
    } else
      buz = 0;

  } else
    buz = 0;
  digitalWrite(BUZZER, buz);
}



void loop() {
  button();
  if (stat == 'I' || stat == 'A') {
    resettime();
  }

  timer();

  if (stat != 'I') //autopower off unit
    batterycount = 0;
  if (batterycount >= batterythreshold) {
    lcd.clear();
    for (;;);
  }

  if (stat == 'S') {
    ledr = 0;
    ledg = 1;
  } else if (stat == 'A') {
    ledr = 1;
    ledg = 1;
  } else if (stat == 'I') {
    ledr = 0;
    ledg = 0;
  }

  if (stat == 'I' && touch(1) == 2)
    statout = 'R';
  else if (stat == 'I' && touch(1) == 3)
    statout = 'L';
  else
    statout = String(stat);

  convertLCD();
  convertLED();
}
