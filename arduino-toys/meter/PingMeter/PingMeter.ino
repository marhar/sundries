//----------------------------------------------------------------------
// PingMeter -- show ping times
//----------------------------------------------------------------------

#define MAXPING 500

int pin = 3;

//----------------------------------------------------------------------
// mapi -- map a value from one range to another
//----------------------------------------------------------------------
int mapi(int x, int in_min, int in_max, int out_min, int out_max)
{
  float t;
  t = (double)(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
  return (int)t;
}


//----------------------------------------------------------------------
void setup() {
  Serial.begin(9600);
}

//----------------------------------------------------------------------
void loop() {
  
  if (Serial.available() > 0) {
    int pingtime;
    int v;
    pingtime = Serial.parseInt();
    
    if (pingtime > MAXPING)
      pingtime = MAXPING;

    v = mapi(pingtime, 0, 500, 0, 255);
    Serial.print(pingtime); Serial.print(" "); Serial.println(v);
    analogWrite(pin, v);
  }
}
