float time = 0;

void setup() { //this happens once
  size(400,400);
  background (100,100,100);
}


void draw() { //this happens over and over
 
 float speed = 1;
 time = time + 1;
  float x =time;
  if (x> width) {
     time = 0;
  }
  float y = 100 * sin(time * 0.05);
 y = y +100; //offset
 fill (200,0,0,20);
 stroke(0,0,100);
 rect (0,0, width, height);
  ellipse(x,y,55,40);
 stroke(0,100,100);
  rect(x,y,40,20);
}

