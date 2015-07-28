//----------------------------------------------------------------------
// SimpleSweep -- sweep the analog dial indicator up and down
//----------------------------------------------------------------------

int pin = 3;  // arduino pin.  make sure it's PWM compatible
int x = 0;    // current value
int d = 1;    // direction

#define XLO 0       // range of arduino analog out
#define XHI 255

//----------------------------------------------------------------------
void setup() {
  Serial.begin(9600);
}

//----------------------------------------------------------------------
void loop() {
  x += d;
  if (x >=XHI || x <= XLO)
    d = -d;
  
  Serial.println(x);
  analogWrite(pin, x);
  delay(10);
}
