// GESTURE CONTROL USING ULTRASONIC SENSORS
// Arduino sends distance values of Right & Left
// ultrasonic sensors to the computer via Serial.
// Python reads these values and performs actions.


// RIGHT SENSOR PINS
#define trigR 9     // Trigger pin for RIGHT sensor at pin 9
#define echoR 8     // Echo pin for RIGHT sensor


// LEFT SENSOR PINS
#define trigL 7     // Trigger pin for LEFT sensor at pin 7
#define echoL 6     // Echo pin for LEFT sensor

long durationR, distanceR;
long durationL, distanceL;

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud rate

  // Set RIGHT sensor pins
  pinMode(trigR, OUTPUT);
  pinMode(echoR, INPUT);

  // Set LEFT sensor pins
  pinMode(trigL, OUTPUT);
  pinMode(echoL, INPUT);
}

// Function to measure distance using ultrasonic sensor
long getDistance(int trigPin, int echoPin) {

  // LOW -> HIGH -> LOW = Send ultrasonic sound wave
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure time for sound to return by 
  long duration = pulseIn(echoPin, HIGH);

  // Convert time -> distance (in cm), .034 cm/us is speed of sound
  long distance = duration * 0.034 / 2;

  return distance;
}

void loop() {

  // Read RIGHT & LEFT sensor distances
  distanceR = getDistance(trigR, echoR);
  distanceL = getDistance(trigL, echoL);

  // Send both distances to Python in this format:
  // Example: 25,40
  Serial.print(distanceR);
  Serial.print(",");
  Serial.println(distanceL);

  delay(100);  // 0.1 second delay for stability
}
