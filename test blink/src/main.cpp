#include <Arduino.h>

char receivedChar;
char* recievedChars;
boolean newData = false;
String receiveString;
boolean isConnected = false;
boolean startData = false;

void setup() {

  Serial.begin(9600);

  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);
  
}

void recvInfo() {

  if (Serial.available() > 0) {
    digitalWrite(3, HIGH);
    receiveString = Serial.readString();
    if (receiveString == "DeviceCheck")
    {
        Serial.write("1234 asdlfkj temperature front");
        digitalWrite(5, HIGH);
        isConnected = true;
    }
    else if (receiveString == "StartData")
    {
      startData = true;
      digitalWrite(6, HIGH);
    }
    else if (receiveString == "X" || receiveString == "x")
    {
      digitalWrite(3, HIGH);
    }
    else
    {
      Serial.write("other string...");
      digitalWrite(10, HIGH);
    }
    
    newData = true;
  }
  
}
void lightLED() {
/*
  int led = (receivedChar - '0');
  while(newData == true) {
    digitalWrite(led, HIGH);
    delay(2000);
    digitalWrite(led, LOW);

    newData = false;
  }*/
  
}

void loop() {

  recvInfo();
  lightLED();
  if (startData)
    Serial.write('1');
  
}
