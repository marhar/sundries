// stripchart

import processing.opengl.*;
import processing.net.*;

int dimX=1024;
int dimY=768;
int portno=4444;      // udp port to monitor

DatagramSocket datagramSocket;
byte[] buffer = new byte[10];
DatagramPacket packet = new DatagramPacket(buffer, buffer.length);

// "Time"
float t = 0.0;

Client c;
float[] vals;
int valix=0;

void setup() {
  try {
  datagramSocket = new DatagramSocket(4445);
  } catch (SocketException e) {
    println(e.getMessage());
  }
  size(dimX,dimY,OPENGL);
  smooth();
  vals=new float[width];
  for (int i = 0; i < width; ++i)
      vals[i]=0.0;
  c = new Client(this, "ohm", 9008);

}

void draw() {
  String input;
  if (c.available() > 0) {
    input = c.readStringUntil(10);
    println(":"+input+":");
    if (input != null && input.length() > 0) {
      float vv=Float.parseFloat(input);
      println(vv);
      if (valix==width) {
        valix=0;
      }
      vals[valix] = vv;
      valix+=1;
    }
  }  
  background(255);

  float vscale=2.2;

  float xoff = t;
  
  stroke(0);
  strokeWeight(1);
  line(valix,0,valix,height);
  for (int i = 0; i < 40; i += 10) {
    line(0,height-10-i*vscale,width,height-10-i*vscale);
  }
  for (int i = 0; i < width-1; i++) {
    stroke(0);
    strokeWeight(2);
    line(i,height-10-vals[i]*vscale,i+1,height-10-vals[i+1]*vscale);
    // Increment xoff
    xoff += 0.01;

  }
  // Increment "time" for whole graph
  t+= 0.01;
}
