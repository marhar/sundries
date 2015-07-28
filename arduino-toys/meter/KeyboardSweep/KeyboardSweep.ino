//----------------------------------------------------------------------
// KeyboardSweep -- control the meter with the keyboard, j,k = down,up
//----------------------------------------------------------------------

#define XLO 0
#define XHI 255

int pin = 3;
int x = 0;

//----------------------------------------------------------------------
void setup() {
  Serial.begin(9600);
}

//----------------------------------------------------------------------
void loop() {
  
  if (Serial.available() > 0) {
    int cmd;
    cmd = Serial.read();
    if      (cmd == 'j' && x > XLO) --x;
    else if (cmd == 'k' && x < XHI) ++x;
    Serial.print(x); Serial.print(" "); Serial.println((double)x/XHI);
    analogWrite(pin, x);
  }
}
