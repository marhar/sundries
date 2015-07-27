// Learning Processing
// Daniel Shiffman
// http://www.learningprocessing.com

// Example: a graph of perlin noise values

import processing.opengl.*;
import processing.net.*;

// "Time"
float t = 0.0;

Client c;
float[] vals;
int valix=0;

void setup() {
  size(400,200,OPENGL);
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
  // Starting point for graph
  float xoff = t;
  for (int i = 0; i < width-1; i++) {
    stroke(0);
    strokeWeight(2);
    // Get current and "next" noise value
    float y1 = noise(xoff)*height;
    float y2 = noise(xoff+0.01)*height;
    // Draw line

    line(i,vals[i]+height-10,i+1,vals[i+1]+height-10);
    // Increment xoff
    xoff += 0.01;

  }
  // Increment "time" for whole graph
  t+= 0.01;
}
