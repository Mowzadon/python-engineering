const int LIGHT_PIN = A0;

const int RED_LED = 8;
const int YELLOW_LED = 9;
const int GREEN_LED = 10;


int readLightLevel() {
  /*
    Reads the photoresistor value from analog pin A0.

    Returns:
      Light reading from 0 to 1023.
  */
  return analogRead(LIGHT_PIN);
}


String classifyLight(int lightLevel) {
  /*
    Classifies the light reading into a lighting condition.
  */
  if (lightLevel <= 200) {
    return "Very Dark";
  } else if (lightLevel <= 600) {
    return "Indoor";
  } else if (lightLevel <= 850) {
    return "Bright";
  } else {
    return "Very Bright";
  }
}


void turnOffAllLEDs() {
  digitalWrite(RED_LED, LOW);
  digitalWrite(YELLOW_LED, LOW);
  digitalWrite(GREEN_LED, LOW);
}


void updateLEDs(int lightLevel) {
  /*
    Turns on the LED that matches the current light level.
  */
  turnOffAllLEDs();

  if (lightLevel <= 200) {
    digitalWrite(RED_LED, HIGH);
  } else if (lightLevel <= 600) {
    digitalWrite(YELLOW_LED, HIGH);
  } else {
    digitalWrite(GREEN_LED, HIGH);
  }
}


void sendSerialData(int lightLevel, String condition) {
  /*
    Sends structured serial data in this format:

    lightLevel,condition

    Example:
    450,Indoor
  */
  Serial.print(lightLevel);
  Serial.print(",");
  Serial.println(condition);
}


void setup() {
  Serial.begin(9600);

  pinMode(RED_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);

  turnOffAllLEDs();
}


void loop() {
  int lightLevel = readLightLevel();
  String condition = classifyLight(lightLevel);

  updateLEDs(lightLevel);
  sendSerialData(lightLevel, condition);

  delay(1000);
}