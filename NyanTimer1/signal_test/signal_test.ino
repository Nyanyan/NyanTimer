#include <TimerOne.h>

String serout = "I000000@";
int count = 0;

void signalOut() {
  count++;
  if (count % 10 == 0) {
    count = 0;
    Serial.print(serout);
    Serial.print(char(10));
    Serial.print(char(13));
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(1200);
  Timer1.initialize(11140);
  Timer1.attachInterrupt(signalOut);
  Timer1.start();
}

void loop() {
  // put your main code here, to run repeatedly:

}
