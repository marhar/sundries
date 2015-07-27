float time = 0;

void setup() {
  size(400,400);
  background(193,66,66);
  

// int x =0;
  
}


//outside the curly bracket - inside doesn't allow this for sharing

void draw() {
  float speed = 1;
  time = time + 1;
  float x = time * speed;
  if (x > width) x = 0;
  float y = 100 * sin(time * 0.05);
  y = y + 200; //offset
  ellipse(x,y,30,40);
}
