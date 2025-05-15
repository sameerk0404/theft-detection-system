int pirPin = 13;
int ledPin = 7;  
int buzzerPin = 12;  

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);  
}

void loop() {
  int motion = digitalRead(pirPin);
  
  if (motion == HIGH) { 
    digitalWrite(ledPin, HIGH);  
    digitalWrite(buzzerPin, HIGH);
    Serial.println("Motion Detected! Capturing Image...");
    delay(2000); 
    digitalWrite(ledPin, LOW);
    digitalWrite(buzzerPin, LOW);
  }
}