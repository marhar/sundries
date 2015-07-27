void setup() {
  size(400,400);
  
  
}

void draw() {
  background(193,66,66);
  float x = frameCount / 10;
  float y = mouseY+30;
  ellipse(x,y,30,40);
}
