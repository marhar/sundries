void setup() {
  size (400,400);
  background(86,220,244);
}

float time = 0;

//here is a pretty picture
void draw() {
  fill (25, 78, 200, 10);
  stroke (0, 0, 0, 95);
  float speed = .5;
  time = time + speed;
  float x = time*sin(time*.5);
  float y = 50*sin(time*.005);
  y = (y+200);
  ellipse(x,y-50,30,40);
  fill (25, 255, 200, 10);
  stroke (0, 0, 0, 90);
  ellipse(x-100,y+50,60,40);
  fill (200, 220, 255, 20);
  stroke (200, 220, 255, 20);
  rect(0, 0, 400, 40);
  //rect(360, 10, 30, 40);
  rect(0, 360, 400, 40);
  //rect(360, 350, 30, 40);
}








