//dualvl531x.ino
#include <Wire.h>
#include <VL53L1X.h>
#include<Servo.h>

VL53L1X gVL531X;

VL53L1X sensor;
VL53L1X sensor2;

Servo servo0ne;
Servo servoTwo;
int servoPin = 9;
int servoPos = 135; // initial servo1 position
int servo2Pin = 8;
int servo2Pos = 135; // initial servo2 position

void setup()
{
  servo0ne.attach(servoPin);
  servoTwo.attach(servo2Pin);
  
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);

  delay(500);
  Wire.begin();


  Serial.begin (9600);

  pinMode(2, INPUT);
  delay(150);
  sensor.init(true);
  delay(100);
  sensor.setAddress((uint8_t)22);
  sensor.setTimeout(500);

  pinMode(3, INPUT);
    delay(150);
  sensor2.init(true);
  delay(100);
  sensor2.setAddress((uint8_t)25);
  sensor2.setTimeout(500);
  
  Serial.println("addresses set");
  sensor.startContinuous(30);
  sensor2.startContinuous(30);
  Serial.println("start read range");
   
  gVL531X.setTimeout(1000);


}

void loop()
{
  int dist1;
  int dist2;
  servo0ne.write(90); // sets position back to original position
  servoTwo.write(90); // sets position back to original position

  // records distance of each lidar in mm
  dist1 = sensor.readRangeContinuousMillimeters(); 
  dist2 = sensor2.readRangeContinuousMillimeters(); 

  // Prints data onto Serial monitor for visualization
  Serial.print("LEFT SENSOR: ");
  Serial.print(dist1);
  Serial.print(" [mm]   ");
  Serial.print("RIGHT SENSOR: ");
  Serial.print(dist2);
  Serial.println(" [mm]   ");
  delay(30);

  // if hand is detected within 50mm of left 
  // lidar, left swipe is executed
  if (dist2 < 50)  {
      Serial.print("LEFT");
      servo0ne.write(180);
      delay(1000);
      servoTwo.write(180);
      delay(1001);
      servo0ne.write(90);
      delay(1000);
      servoTwo.write(0);
      delay(1001);
      servo0ne.write(180);
      delay(1000);
      servoTwo.write(90);
      delay(1001);
      servo0ne.write(135);
    }
    
  // if hand is detected within 50mm of right 
  // lidar, right swipe is executed
  if (dist1 < 50)  { 
      Serial.print("RIGHT");
      servo0ne.write(180);
      delay(1000);
      servoTwo.write(0);
      delay(1001);
      servo0ne.write(90);
      delay(1000);
      servoTwo.write(180);
      delay(1001);
      servo0ne.write(180);
      delay(1000);
      servoTwo.write(90);
      delay(1001);
      servo0ne.write(135);
    }

  if (sensor.timeoutOccurred()){
    Serial.print("sensor1timeout\n");
  }
  if (sensor2.timeoutOccurred()){
    Serial.print("sensor2timeout\n");
  }
}
