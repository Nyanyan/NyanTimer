#include <NyanTimer2.h>

#define maxlap 99
#define batterythreshold 2700 //1000 per 30s

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
String inspresult = "";
int formertouch = 0;

void setup() {
  NyanTimer::begin();
  resettime();
  if (NyanTimer::msecond != 0 || NyanTimer::second != 0 || NyanTimer::minute != 0)
    NyanTimer::stat = 'S';
}


void count() { //every 1 msec
  NyanTimer::msecond++;
  if (NyanTimer::msecond % 100 == 0) {
    ledg = ledr;
    ledr = !ledr;
  }
}




void resettime() {
  NyanTimer::minute = 0;
  NyanTimer::second = 0;
  NyanTimer::msecond = 0;
  for (int i = 0; i < 7; i++)
    NyanTimer::output[i] = 0;
  digitalWrite(A4, LOW);
}



void timer() {
  int touchnow = NyanTimer::touch();
  if (touchnow != 0 && touchnow != formertouch) {
    bool flag = false;
    if (NyanTimer::stat == ' ') {
      if (lapcount == lapmode - 1 && touchnow == 1) { //when timer stops
        NyanTimer::stat = 'S';
        NyanTimer::stopTimer();
        NyanTimer::timing();
        //String lcdoutb = NyanTimer::strTime(NyanTimer::output);
        flag = true;
      }
    } else if (NyanTimer::stat == 'I' && touchnow == 1) { //timer ready to start
      if (inspmode == 0 || (inspmode == 1 && inspstat == 2) || (inspmode == 2 && inspstat == 2)) { //not inspstatection mode
        ledr = 1;
        ledg = 0;
        unsigned long strt = millis();
        unsigned long stp = strt;
        while (NyanTimer::touch() == 1 && stp - strt <= 550) { //wait about 0.55sec
          stp = millis();
        }
        if (strt - stp >= 550)  //timer is able to start
          NyanTimer::stat = 'A';
      }
    }
  }


  if (NyanTimer::touch() != 1) { //when pads are open
    if (NyanTimer::stat == 'A') { //start solving
      NyanTimer::stat = ' ';
      inspstat = 0;
      NyanTimer::stopTimer();
      NyanTimer::startTimer(1, count);

      formertouch = 1;
    }
  }
  formertouch = touchnow;
}



void loop() {
  //timing unit
  NyanTimer::timing();

  //timer unit
  timer();

  if (NyanTimer::stat == 'S' && Serial.available() > 0 && Serial.read() == 'y') {
    resettime();
    NyanTimer::stat = 'I';
  }
  if (analogRead(A5) < 200)
    digitalWrite(A4, HIGH);
}
