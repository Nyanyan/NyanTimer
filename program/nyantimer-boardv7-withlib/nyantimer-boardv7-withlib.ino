#include "NyanTimer.h"

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
String inspresult = "";

void setup() {
  resettime();
  NyanTimer::begin();
  setLCDclear(2);
  lap[0][0] = 0;
  lap[0][1] = 0;
  lap[0][2] = 0;
}


void inspection() {
  inspstatcount--;
}




void count() { //every 1 msec
  NyanTimer::msecond++;
  if (NyanTimer::msecond == 1000) {
    NyanTimer::msecond = 0;
    NyanTimer::second++;
  }
  if (NyanTimer::second == 60) {
    NyanTimer::second = 0;
    NyanTimer::minute++;
  }
  if (NyanTimer::stat == " " && NyanTimer::msecond % 100 == 0) {
    ledg = ledr;
    ledr = !ledr;
  }
  if (NyanTimer::minute >= 100)
    NyanTimer::stopTimer();
  NyanTimer::calcTime(NyanTimer::minute, NyanTimer::second, NyanTimer::msecond, NyanTimer::output);
}





void convertLCD() {
  String lcdouta = NyanTimer::strTime(NyanTimer::output);
  NyanTimer::printLCD(7, 0, lcdouta);

  String lcdoutb;
  if (lapcount >= 1) {
    int a[7];
    int t;
    if (NyanTimer::stat == "I")
      t = lapcount + 1;
    else
      t = lapcount;
    NyanTimer::calcTime(lap[t][0], lap[t][1], lap[t][2], a);
    lcdoutb = NyanTimer::strTime(a);
  } else
    lcdoutb = "         ";
  NyanTimer::printLCD(7, 1, lcdoutb);

  if (inspstat == 0) {
    if (inspmode == 1)
      NyanTimer::printLCD(0, 0, "I ");
    else if (inspmode == 2)
      NyanTimer::printLCD(0, 0, "Is");
    else if (inspmode == 0)
      NyanTimer::printLCD(0, 0, "  ");
  }
  NyanTimer::printLCD(0, 1, "L");
  NyanTimer::printLCD(1, 1, String(int(lapcount / 10)));
  NyanTimer::printLCD(2, 1, String(lapcount - int(lapcount / 10) * 10));
  NyanTimer::printLCD(3, 1, "/");
  NyanTimer::printLCD(4, 1, String(int(lapmode / 10)));
  NyanTimer::printLCD(5, 1, String(lapmode - int(lapmode / 10) * 10));
}



void convertLED() {
  NyanTimer::lightLED(LEDR, ledr);
  NyanTimer::lightLED(LEDG, ledg);
}



void resettime() {
  NyanTimer::minute = 0;
  NyanTimer::second = 0;
  NyanTimer::msecond = 0;
  for (int i = 0; i < 7; i++)
    NyanTimer::output[i] = 0;
  for (int i = 0; i < maxlap; i++) {
    for (int j = 0; j < 3; j++)
      lap[i][j] = 0;
  }
  lapcount = 0;
}


void lapUP() {
  if (NyanTimer::stat == "I") {
    lapmode++;
    if (lapmode > maxlap)
      lapmode = 1;
  } else if (NyanTimer::stat == "S") {
    lapcount++;
    if (lapcount > lapmode) {
      lapcount = 1;
    }
  }
}

void lapDOWN() {
  if (NyanTimer::stat == "I") {
    lapmode--;
    if (lapmode < 1)
      lapmode = maxlap;
  } else if (NyanTimer::stat == "S") {
    lapcount--;
    if (lapcount < 1)
      lapcount = lapmode;
  }
}

void setLCDclear(int m) {
  if (m == 0 || m == 2)
    NyanTimer::printLCD(0, 0, "                ");
  if (m == 1 || m == 2)
    NyanTimer::printLCD(0, 1, "                ");
}

void button() {
  if (digitalRead(BUTTON1) == HIGH) {//reset
    int a = 0;
    int t = 500;
    while (digitalRead(BUTTON1) == HIGH) {
      a++;
      delay(1);
      if (a >= t)
        break;
    }
    if (a >= t) {
      NyanTimer::stopTimer();
      batterycount = 0;
      NyanTimer::stat = "I";
      inspresult = "";
      NyanTimer::printLCD(3, 0, "    ");
    }
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
  } else if (NyanTimer::stat == "I")
    batterycount++;
}



void timer() {
  if (NyanTimer::touch(1) != 0) {
    if (NyanTimer::stat == " ") {
      bool tmp = false;
      if (lapcount == lapmode - 1 && NyanTimer::touch(0) == 1) { //when timer stops
        NyanTimer::stat = "S";
        NyanTimer::stopTimer();
        ledr = 0;
        ledg = 0;
        tmp = true;
      }

      if (lapcount < lapmode - 1 || tmp) { //lap++
        lapcount++;
        lap[lapcount][0] = NyanTimer::minute;
        lap[lapcount][1] = NyanTimer::second;
        lap[lapcount][2] = NyanTimer::msecond;
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
        int cnt = 0;
        int touchthreshold = 10;
        while (touchflag) {
          if (NyanTimer::touch(1) == 0)
            cnt++;
          else
            cnt = 0;
          if (cnt > touchthreshold)
            touchflag = false;
        }
      }


    } else if (NyanTimer::stat == "I" && NyanTimer::touch(0) == 1) { //timer ready to start
      if (inspmode == 0 || (inspmode == 1 && inspstat == 2) || (inspmode == 2 && inspstat == 2)) { //not inspstatection mode
        ledr = 1;
        ledg = 0;
        convertLED();
        int waitingthreshold = 20;
        int i = 0;
        while (NyanTimer::touch(0) == 1 && i < waitingthreshold) { //wait about 0.55sec
          i++;
          delay(1);
          if (inspmode == 2) {
            if (inspstatcount > 0 && inspstatcount < 16) {
              String inspstatcountstr = String(int(inspstatcount / 10)) + String(inspstatcount - 10 * int(inspstatcount / 10));
              NyanTimer::printLCD(3, 0, inspstatcountstr);
            } else if (inspstatcount > -2 && inspstatcount <= 0) {
              inspresult = "+2";
            } else if  (inspstatcount <= -2) {
              inspresult = "DNF";
              NyanTimer::printLCD(3, 0, "DNF");
              NyanTimer::stopTimer();
            }
            if (inspmode == 2) {
              if (inspstatcount == 7 || inspstatcount == 3)
                buz = 1;
              else
                buz = 0;
            } else
              buz = 0;
            digitalWrite(BUZZER, buz);
          }
        }
        if (i >= waitingthreshold)  //timer is able to start
          NyanTimer::stat = "A";
      } else if ((inspmode == 1 && inspstat == 0) || (inspmode == 2 && inspstat == 0)) { //inspstatection mode
        int i = 0;
        int waitingthreshold = 15;
        while (NyanTimer::touch(0) == 1 && i < waitingthreshold) { //wait about 0.55sec
          i++;
          delay(1);
        }
        if (i >= waitingthreshold) { //timer is able to start
          inspstat = 1;
          ledr = 1;
          ledg = 0;
        } else {
          ledr = 0;
          ledg = 0;
        }
        convertLED();
        while (NyanTimer::touch(0) == 1);
      }
    }
  }




  if (NyanTimer::touch(0) == 0) { //when pads are open

    if (NyanTimer::stat == "A") { //start solving
      NyanTimer::stat = " ";
      inspstat = 0;
      NyanTimer::stopTimer();
      NyanTimer::startTimer(1, count);

      setLCDclear(1);
      bool touchflag = true;
      int cnt = 0;
      int touchthreshold = 10;
      while (touchflag) {
        if (NyanTimer::touch(1) == 0)
          cnt++;
        else
          cnt = 0;
        if (cnt > touchthreshold)
          touchflag = false;
      }
    }

    else if (NyanTimer::stat == "I" && inspstat == 1) { //inspection time starts
      ledr = 1;
      ledg = 0;
      convertLED();
      inspstat = 2;
      NyanTimer::stopTimer();
      inspstatcount = 15;
      convertLCD();
      NyanTimer::startTimer(1000, inspection);
    }
  }


  if ((NyanTimer::stat == "I" && inspstat == 2) || (NyanTimer::stat == "A" && inspstat == 2)) {
    if (inspstatcount > 0 && inspstatcount < 16) {
      String inspstatcountstr = String(int(inspstatcount / 10)) + String(inspstatcount - 10 * int(inspstatcount / 10));
      NyanTimer::printLCD(3, 0, inspstatcountstr);
    } else if (inspstatcount > -2 && inspstatcount <= 0)
      inspresult = "+2";
    else if  (inspstatcount <= -2) {
      inspresult = "DNF";
      NyanTimer::stopTimer();
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
  if (NyanTimer::stat == "I" || NyanTimer::stat == "A") {
    resettime();
  }

  timer();

  if (NyanTimer::stat != "I") //autopower off unit
    batterycount = 0;
  if (batterycount >= batterythreshold) {
    setLCDclear(2);
    for (;;);
  }

  if (NyanTimer::stat == "S") {
    ledr = 0;
    ledg = 1;
  } else if (NyanTimer::stat == "A") {
    ledr = 1;
    ledg = 1;
  } else if (NyanTimer::stat == "I") {
    ledr = 0;
    ledg = 0;
  }

  if (NyanTimer::stat == "I" && NyanTimer::touch(1) == 2)
    NyanTimer::statout = "R";
  else if (NyanTimer::stat == "I" && NyanTimer::touch(1) == 3)
    NyanTimer::statout = "L";
  else
    NyanTimer::statout = String(NyanTimer::stat);

  convertLCD();
  convertLED();
  NyanTimer::printLCD(3, 0, inspresult);
  Serial.println(NyanTimer::stat);
}
