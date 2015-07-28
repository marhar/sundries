//----------------------------------------------------------------------
// TickTock -- make the analog meter sound like a clock
//----------------------------------------------------------------------

int pin = 3;

void setup() {
}

void loop() {
  analogWrite(pin, 0);    // tock
  delay(1000);
  analogWrite(pin, 255);  // tick
  delay(1000);
}
