#include <NyanTimer.h>
//#include <MemoryFree.h>

#define maxlap 99
#define batterythreshold 10000 //1000 per 30s

volatile bool ledr = 0; //red led status
volatile bool ledg = 0; //green led status
int inspmode = 0; //0:off 1:sndOFF 2:sndON
int lapmode = 1;
int lapcount = 0;
int lap[maxlap + 1][3];
int inspstat = 0; //1=during inspstatection time
int inspstatcount = 16; //inspstatection time count
bool soundmode = false;
bool buz = 0;
long batterycount = 0;
String inspresult = "";
int formertouch = 0;

void setup() {
  resettime();
  NyanTimer::begin();
  NyanTimer::setLCDclear(2);
  lap[0][0] = 0;
  lap[0][1] = 0;
  lap[0][2] = 0;
}


void inspection() {
  inspstatcount--;
}




void count() { //every 1 msec
  NyanTimer::msecond++;
  if (NyanTimer::msecond % 100 == 0) {
    ledg = ledr;
    ledr = !ledr;
  }
}







void convertLCD() {
  String lcdouta = NyanTimer::strTime(NyanTimer::output);
  NyanTimer::printLCD(7, 0, lcdouta);

  String lcdoutb;
  if (lapcount >= 1) {
    int a[7];
    int t;
    if (NyanTimer::stat == 'I')
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
      NyanTimer::printLCD(0, 0, 'i');
    else if (inspmode == 2)
      NyanTimer::printLCD(0, 0, 'I');
    else if (inspmode == 0)
      NyanTimer::printLCD(0, 0, ' ');
  }
  if (soundmode)
    NyanTimer::printLCD(1, 0, 'S');
  else
    NyanTimer::printLCD(1, 0, ' ');
  NyanTimer::printLCD(0, 1, 'L');
  String lapout = String(int(lapcount / 10)) +  String(lapcount - int(lapcount / 10) * 10) + "/" + String(int(lapmode / 10)) + String(lapmode - int(lapmode / 10) * 10);
  NyanTimer::printLCD(1, 1, lapout);
  //Serial.println(freeMemory());
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
  if (NyanTimer::stat == 'I') {
    lapmode++;
    if (lapmode > maxlap)
      lapmode = 1;
  } else if (NyanTimer::stat == 'S') {
    lapcount++;
    if (lapcount > lapmode) {
      lapcount = 1;
    }
  }
}

void lapDOWN() {
  if (NyanTimer::stat == 'I') {
    lapmode--;
    if (lapmode < 1)
      lapmode = maxlap;
  } else if (NyanTimer::stat == 'S') {
    lapcount--;
    if (lapcount < 1)
      lapcount = lapmode;
  }
}

void button() {
  if (NyanTimer::inputButton(BUTTON1)) {//reset
    batterycount = 0;
    int a = 0;
    int t = 500;
    while (NyanTimer::inputButton(BUTTON1)) {
      a++;
      delay(1);
      if (a >= t)
        break;
    }
    if (a >= t) {
      NyanTimer::stopTimer();
      NyanTimer::stat = 'I';
      inspresult = "";
      NyanTimer::printLCD(3, 0, "    ");
    }
  } else if (NyanTimer::inputButton(BUTTON2)) { //inspstatection mode and sound mode
    batterycount = 0;
    int a = 0;
    int t = 500;
    while (NyanTimer::inputButton(BUTTON2)) {
      a++;
      delay(1);
      if (a >= t)
        break;
    }
    if (a >= t) {
      soundmode = !soundmode;
      if (soundmode)
        NyanTimer::printLCD(1, 0, 'S');
      else
        NyanTimer::printLCD(1, 0, ' ');
      while (NyanTimer::inputButton(BUTTON2));
    } else {
      inspmode += 1;
      if (inspmode > 2)
        inspmode = 0;
      while (NyanTimer::inputButton(BUTTON2));
    }
  } else if (NyanTimer::inputButton(BUTTON3)) { //lap mode up
    batterycount = 0;
    lapUP();
    convertLCD();
    for (int i = 0; i < 1000; i++) {
      if (!NyanTimer::inputButton(BUTTON3))
        break;
      delay(1);
    }
    while (NyanTimer::inputButton(BUTTON3)) {
      lapUP();
      delay(100);
      convertLCD();
    }
  } else if (NyanTimer::inputButton(BUTTON4)) { //lap mode down
    batterycount = 0;
    lapDOWN();
    convertLCD();
    for (int i = 0; i < 1000; i++) {
      if (!NyanTimer::inputButton(BUTTON4))
        break;
      delay(1);
    }
    while (NyanTimer::inputButton(BUTTON4)) {
      lapDOWN();
      delay(100);
      convertLCD();
    }
  } else if (NyanTimer::stat == 'I' || NyanTimer::stat == 'S')
    batterycount++;

}



void timer() {
  const int num = 7;
  int tmp1[num];
  for (int i = 0; i < num; i++)
    tmp1[i] = NyanTimer::touch();
  int tmp2[4] = {0, 0, 0, 0};
  for (int i = 0; i < num; i++)
    tmp2[tmp1[i]]++;
  int m = 0;
  int tmp3 = 0;
  for (int i = 0; i < 4; i++) {
    if (tmp2[i] > m) {
      m = tmp2[i];
      tmp3 = i;
    }
  }
  int touchnow = tmp3;
  if (touchnow != 0 && touchnow != formertouch) {
    batterycount = 0;
    bool flag = false;
    if (NyanTimer::stat == ' ') {
      if (lapcount == lapmode - 1 && touchnow == 1) { //when timer stops
        NyanTimer::stat = 'S';
        NyanTimer::stopTimer();
        String lcdouta = NyanTimer::strTime(NyanTimer::output);
        NyanTimer::printLCD(7, 0, lcdouta);
        if (soundmode) {
          digitalWrite(BUZZER, HIGH);
          delay(1000);
        }
        ledr = 0;
        ledg = 0;
        flag = true;
      }

      if ((lapcount < lapmode - 1 && formertouch != 1) || flag) { //lap++
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
        int a[7];
        NyanTimer::calcTime(lap[lapcount][0], lap[lapcount][1], lap[lapcount][2], a);
        String lcdoutb = NyanTimer::strTime(a);
        NyanTimer::printLCD(7, 1, lcdoutb);
        int threshold = 5;
        int cnt = 0;
        while (cnt <= threshold) {
          if (NyanTimer::touch() == touchnow)
            cnt = 0;
          else
            cnt++;
        }
      }


    } else if (NyanTimer::stat == 'I' && touchnow == 1) { //timer ready to start
      if (inspmode == 0 || (inspmode == 1 && inspstat == 2) || (inspmode == 2 && inspstat == 2)) { //not inspstatection mode
        ledr = 1;
        ledg = 0;
        convertLED();
        int waitingthreshold = 20;
        int i = 0;
        while (NyanTimer::touch() == 1 && i < waitingthreshold) { //wait about 0.55sec
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
              if (inspstatcount == 7 || inspstatcount == 3 || inspstatcount == 0 || inspstatcount == -2)
                buz = 1;
              else
                buz = 0;
            } else
              buz = 0;
            digitalWrite(BUZZER, buz);
          }
        }
        if (i >= waitingthreshold)  //timer is able to start
          NyanTimer::stat = 'A';
      } else if ((inspmode == 1 && inspstat == 0) || (inspmode == 2 && inspstat == 0)) { //inspstatection mode
        int i = 0;
        int waitingthreshold = 15;
        while (NyanTimer::touch() == 1 && i < waitingthreshold) { //wait about 0.55sec
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
        while (NyanTimer::touch() == 1);
      }
    }
  }




  if (NyanTimer::touch() != 1) { //when pads are open

    if (NyanTimer::stat == 'A') { //start solving
      NyanTimer::stat = ' ';
      inspstat = 0;
      NyanTimer::stopTimer();
      NyanTimer::startTimer(1, count);

      NyanTimer::setLCDclear(1);
      formertouch = 1;
    }

    else if (NyanTimer::stat == 'I' && inspstat == 1) { //inspection time starts
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


  if ((NyanTimer::stat == 'I' && inspstat == 2) || (NyanTimer::stat == 'A' && inspstat == 2)) {
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
      if (inspstatcount == 7 || inspstatcount == 3 || inspstatcount == 0 || inspstatcount == -2)
        buz = 1;
      else
        buz = 0;
    } else
      buz = 0;

  } else
    buz = 0;
  digitalWrite(BUZZER, buz);
  formertouch = touchnow;
}



void loop() {
  //timing unit, must be done in loop in order to output signal
  NyanTimer::timing();

  //button unit
  if (NyanTimer::stat != ' ')
    button();

  //reset time unit
  if (NyanTimer::stat == 'I' || NyanTimer::stat == 'A')
    resettime();

  //timer unit
  timer();

  //auto power off unit
  if (batterycount >= batterythreshold) {
    NyanTimer::setLCDclear(2);
    delay(1000);
    SMCR |= (1 << SM1);
    SMCR |= 1;
    ADCSRA &= ~(1 << ADEN);
    MCUCR |= (1 << BODSE) | (1 << BODS);
    MCUCR = (MCUCR & ~(1 << BODSE)) | (1 << BODS);
    asm("sleep");
  }

  //led unit
  if (NyanTimer::stat == 'S') {
    ledr = 0;
    ledg = 1;
  } else if (NyanTimer::stat == 'A') {
    ledr = 1;
    ledg = 1;
  } else if (NyanTimer::stat == 'I') {
    ledr = 0;
    ledg = 0;
  }

  //convert lcd and led unit
  convertLCD();
  convertLED();
  NyanTimer::printLCD(3, 0, inspresult);

}
