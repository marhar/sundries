// Learning Processing
// Daniel Shiffman
// http://www.learningprocessing.com

// Example: a graph of perlin noise values

// "Time"
float t = 0.0;

import processing.opengl.*;
void setup() {
  size(400,200,OPENGL);
  smooth();
}

void draw() {
  background(255);
  // Starting point for graph
  float xoff = t;
  for (int i = 0; i < width; i++) {
    stroke(0);
    strokeWeight(2);
    // Get current and "next" noise value
    float y1 = noise(xoff)*height;
    float y2 = noise(xoff+0.01)*height;
    // Draw line
    line(i,y1,i+1,y2);
    // Increment xoff
    xoff += 0.01;

  }
  // Increment "time" for whole graph
  t+= 0.01;
}
