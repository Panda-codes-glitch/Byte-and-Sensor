# Byte-and-Sensor
AI-Powered Threat Detection with securing IoT Devices

#define RED_LED 13
#define WHITE_LED 12
#define BUZZER 10

void setup() {
  Serial.begin(9600);    // Initialize serial communication
  pinMode(RED_LED, OUTPUT);
  pinMode(WHITE_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');  // Read data from PC
    data.trim();  // Remove extra spaces and newlines
    
    Serial.println("Received: " + data);  // Debug print

    if (data == "phishing") {         // If phishing detected
      digitalWrite(RED_LED, HIGH);
      digitalWrite(WHITE_LED, LOW);
      digitalWrite(BUZZER, HIGH);
      Serial.println("Compromised!");
      delay(1000);
      digitalWrite(BUZZER, LOW);
      delay(500);   // Extra delay for buzzer clarity

    } else if (data == "safe") {        // If safe signal
      digitalWrite(RED_LED, LOW);
      digitalWrite(WHITE_LED, HIGH);
      digitalWrite(BUZZER, LOW);  // Ensure buzzer is off
      Serial.println("Safe!");
      
    } else {
      Serial.println("Unknown command!");
    }
  }
}
