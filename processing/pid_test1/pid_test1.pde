// Learning Processing
// Daniel Shiffman
// http://www.learningprocessing.com

// Example: a graph of perlin noise values

import processing.opengl.*;

int dimX=1024;
int dimY=768;

// "Time"
float t = 0.0;

float[] mvals;
int mvalix=0;

void setup() {
  size(dimY,dimX,OPENGL);
  smooth();
  mvals=new float[width];
  for (int i = 0; i < width; ++i)
      mvals[i]=0.0;
}

void draw() {
  int vv;
  String input;
    vv=width-mouseY;
    println(vv);
    if (mvalix==width) {
      mvalix=0;
    }
    mvals[mvalix] = vv;
    mvalix+=1;
  background(255);

  float vscale=2.2;

  float xoff = t;
  
  stroke(0);
  strokeWeight(1);
  line(mvalix,0,mvalix,height);
  for (int i = 0; i < 40; i += 10) {
    line(0,height-10-i*vscale,width,height-10-i*vscale);
  }
  for (int i = 0; i < width-1; i++) {
    stroke(0);
    strokeWeight(2);
    line(i,height-10-mvals[i]*vscale,i+1,height-10-mvals[i+1]*vscale);
    // Increment xoff
    xoff += 0.01;

  }
  // Increment "time" for whole graph
  t+= 0.05;
}
