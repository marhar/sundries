void setup() {
  size(400,400);
  
float x = 0;
// int x =0;
  
}

void draw() {
  background(193,66,66);
  x = x + 0.1;
  // thus will not work with int
  float x = frameCount / 10;
  float y = mouseY+30;
  ellipse(x,y,30,40);
}
