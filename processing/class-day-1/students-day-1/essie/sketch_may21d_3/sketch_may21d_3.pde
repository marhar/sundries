// float x = 0; => can be here as well -- when its outside of curly brackets.

void setup() {
  size(400,400);
  

// int x =0;
  
}
float x = 0;

//outside the curly bracket - inside doesn't allow this for sharing

void draw() {
  background(193,66,66);
  float speed = 0.1;
  x = x + speed;
  // thus will not work with int
  float x = frameCount / 10;
  float y = mouseY+30;
  ellipse(x,y,30,40);
}
