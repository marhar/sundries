void setup(){
  size(400,400);
  background(77,111,20);
  }
float time = 0; 

void draw(){
  float speed = 1;
  time = time + 1;
  float x = time * speed;
  if (time>500) time = 0;
  float y = 100* sin(time*0.9);
  y = y+200; //offset
  ellipse(x,y,35,70);

}

