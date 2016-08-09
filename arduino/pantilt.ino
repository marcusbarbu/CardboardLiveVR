#include <Servo.h>
char recByte;
int panPin = 6;
int tiltPin = 3;
int panSteps = 5;
int tiltSteps = 10;
Servo pan;
Servo tilt;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pan.attach(panPin);
  tilt.attach(tiltPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  pan.writeMicroseconds(1530);
  if(Serial.available()>0){
    recByte = Serial.read();
    if(recByte == 'L'){
      pan.write(100);
      delay(100);
      pan.write(95);
    }
    else if(recByte == 'R'){
      pan.write(80);
      delay(100);
      pan.write(95);
    }
    else if(recByte == 'U'){
      tilt.write(tilt.read()+tiltSteps);
    }
   else if(recByte == 'D'){
    tilt.write(tilt.read()-tiltSteps);
   }
   else{
     pan.writeMicroseconds(1530);
     tilt.write(90);
   }
  } 
}
