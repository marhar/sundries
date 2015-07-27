import processing.opengl.*;
import processing.net.*;


Client c;
float time=0;
float time2=0;
float depth= -800;
float x,y,z;


void setup() {
  size(600,600,OPENGL);
  noStroke();
  smooth();
  c = new Client(this, "ohm", 9008);
}


void draw() {
  // Center and spin grid
  translate(width/2, height/2, depth);
  rotateY(frameCount * 0.01);
  rotateX(frameCount * 0.01);
  
  background(cos(time*0.03)*200,150,150);
  float speed = 1;
  time = time + 1;
  time2 = time2 + 1;
  int howManyDots = 15;
  String input;
  if (c.available() > 0) {
    input = c.readStringUntil(10);
    println(":"+input+":");
    if (input != null && input.length() > 0) {
      howManyDots=int(Float.parseFloat(input));
    }
  }  



  lights();
  pushMatrix();
  for (int i=0; i<howManyDots; i++) {
    x = sin(i+time*0.15) * 200;
    y = cos(i+time*0.13) * 200;
    z = sin(i+time*0.11) * 200;
    x = x + (width/8);
    y = y + (height/8);
    if(z < 400) {
      fill(random(200,255),random(0,255),random(0,255),100);
      translate(x,y,z);
      sphereDetail(8);
      sphere(30);
    }
  }
  for (int i=0; i<howManyDots; i++) {
    x = sin(i+time2*0.15) * 200;
    y = cos(i+time2*0.13) * 200;
    z = sin(i+time2*0.11) * 200;
    x = x + (width/8);
    y = y + (height/8);
    if(z < 400) {
      fill(random(200,255),random(0,255),random(0,255),100);
      translate(x,y,z);
      sphereDetail(8);
      sphere(30);
    }
  }
  popMatrix();

}
