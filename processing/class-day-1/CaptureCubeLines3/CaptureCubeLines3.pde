import processing.opengl.*;

PGraphics pg;
PImage tex;
float rotx = PI/4;
float roty = PI/4;
int maxCubes = 80;
//int maxCubes = 10;
int maxLines = 10;
float atten = .93;
float amtAlpha = 1;//atten*.5; 
float saturate = .1;
float randXX;
float randYY;
float randLength;
int tone;
float thick;
color bgColor = color(0,0,0);
color satColor;
color [] colors = {
  color(230,220,255,255),
  color(230,100,255,255),
  color(167,150,255,255),
  color(124,250,255,255),
  color(100,50,255,255),
  color(200,250,255,255),
  color(255,250,255,255)};
float time = 0;
float margin = 400;
int odd = 0;
int blurOn = 1;
int colorOn = 1;
int pgOn = 0;
void setup() 
{
  colorMode(HSB,1.0);
  pg = createGraphics(100,100,P2D);
  pg.colorMode(HSB,1.0);
  tex = createImage(100,100,ARGB);
  size(screen.width,screen.height,OPENGL);
  //size(500,300,P3D);
  textureMode(NORMALIZED);
}

float accel = mouseX - pmouseX;

void draw() 
{
    noCursor();
  if (keyPressed) {
    if (key == 'b') {
      blurOn = 1 - blurOn;
    }
  }
  if (keyPressed) {
    if (key == 'v') {
      colorOn = 1 - colorOn;
    }
  }
  //colorOn = round(noise(frameCount * 0));
  pg.beginDraw(); 
  if (blurOn == 1) {
    pg.filter(BLUR,1);
    amtAlpha = 1;
  } 
  else {
    amtAlpha = atten;
  }

  if (keyPressed == true) {
    if (key == 'c') {
      pg.loadPixels();  
      for (int i = 0; i < (pg.pixels.length); i++) {
        pg.pixels[i] = color(0,0,0,0);
      }
    }
  }
  float randShape;
  float frameSpeed = noise(frameCount) * .01;
  for (int i = 0;i < maxLines;i++) {
    odd = 1 - odd;
    randShape = noise(i * 100) ;//* noise(frameCount * .001);
    randLength = (randShape) * 60;
    randXX = noise(i * 357 + frameCount * .01) * 100; //random(20,100);
    randYY = noise(i * 123 + frameCount * .01) * 100; //random(10,100);
    thick = (randShape * 0) + 1;
    pg.strokeWeight(thick);
    tone = int((noise(i + frameCount * 0.01)*colors.length));
    if (colorOn == 1) {
      pg.stroke(colors[tone]);
    } 
    else {
      pg.stroke(color(.3,0,1,1));
    }
    //odd = round(noise(mouseX));
    if (odd == 1) {
      pg.line(randXX,randYY,randXX+randLength,randYY);
    } 
    else {
      pg.line(randXX,randYY,randXX,randYY+randLength);
    }
  }
  pg.loadPixels(); 
  for (int i = 0; i < (pg.pixels.length); i++) {
    pg.pixels[i] = color(hue(pg.pixels[i]),
    constrain(saturation(pg.pixels[i]) + saturate,0,1),
    brightness(pg.pixels[i]),      
    alpha(pg.pixels[i]) * amtAlpha);
  }

  pg.endDraw();

  tex = pg;
  background(bgColor);
  noStroke();
  if ((keyPressed && key == 'p') || (pgOn == 1)) {
    pgOn = 1 - pgOn;
    pushMatrix();
    translate(width*.5,height*.5);
    imageMode(CENTER);
    rectMode(CENTER);
    scale(8,8);    
    fill(0,0,.1);
    stroke(0,0,1,1);
    rect(0,0,100,100);
    image(pg,0,0);
    noStroke();
    popMatrix();
  } 
  else {
    for (int i =0;i<maxCubes;i++) {  
      pushMatrix();  
      float randX = (noise(i+4)* (width + (margin * 2))) - margin;
      float randY = (noise(i-37)* (height + (margin * 2))) - margin; 
      float randZ = noise(i+43) * 200;
      randZ -= 50;   
      float randScale = noise(i+37) + 400; 
      randScale -= 250;
      translate(randX,randY,randZ);
      //rotx += .00001 * frameCount;
      rotx = time*.01;
      rotateX(rotx);
      rotateY(roty);
      scale(randScale);    
      TexturedCube(pg);
      popMatrix();
    }
  }
  time++;

}

void TexturedCube(PImage tex) {
  beginShape(QUADS);
  texture(tex);
  // +Z "front" face
  vertex(-1, -1,  1, 0, 0);
  vertex( 1, -1,  1, 1, 0);
  vertex( 1,  1,  1, 1, 1);
  vertex(-1,  1,  1, 0, 1);
  // -Z "back" face
  vertex( 1, -1, -1, 0, 0);
  vertex(-1, -1, -1, 1, 0);     
  vertex(-1,  1, -1, 1, 1);
  vertex( 1,  1, -1, 0, 1);
  // +Y "bottom" face
  vertex(-1,  1,  1, 0, 0);
  vertex( 1,  1,  1, 1, 0);
  vertex( 1,  1, -1, 1, 1);
  vertex(-1,  1, -1, 0, 1);
  // -Y "top" face
  vertex(-1, -1, -1, 0, 0);
  vertex( 1, -1, -1, 1, 0);
  vertex( 1, -1,  1, 1, 1);
  vertex(-1, -1,  1, 0, 1);
  // +X "right" face
  vertex( 1, -1,  1, 0, 0);
  vertex( 1, -1, -1, 1, 0);
  vertex( 1,  1, -1, 1, 1);
  vertex( 1,  1,  1, 0, 1);
  // -X "left" face
  vertex(-1, -1, -1, 0, 0);
  vertex(-1, -1,  1, 1, 0);
  vertex(-1,  1,  1, 1, 1);
  vertex(-1,  1, -1, 0, 1);
  endShape();
}

void mouseDragged() {
  float rate = 0.01;
  rotx += (pmouseY-mouseY) * rate;
  roty += (mouseX-pmouseX) * rate;
}
/*
void Xaos() {
  print("Screen x is:" + screenX(mouseX,mouseY) + "\n");
  print("Screen y is:" + screenY(mouseX,mouseY) + "\n\n");
}
*/


void keyPressed(){
  exit();
}
void mouseMoved(){
  exit(); 
} 










