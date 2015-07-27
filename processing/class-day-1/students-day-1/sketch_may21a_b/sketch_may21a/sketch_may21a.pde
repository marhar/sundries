void setup() {
  background(174,216,37);
  size(400,400);
  frameRate(24);
}

int x = 50;
int y = 50;
int n = 20;
int m = 400;
int inc = 100;
float time = 0;
float time2 = 0;

void draw() {
  float speed = 1;
  time = time + speed;
  time2 = time2 + speed;
  
  if (time > 400) {
    time = 0;
  }
  
  if (time2 > 50) {
    fill(174,216,37,100);
    noStroke();
    rect(0,0,m,m);
    time2 = 0;
  }
  
  for (int i=y; i<m-x; i=i+inc) {
    for (int j=x; j<m-y; j=j+inc) {
      fill(125,random(120,255),28,random(1,10));
      stroke(255,random(1,100));
      float r = random(-100,100);
      rect(j+r,i+r,r,r);
    }
  }
  
  
  //fill(152,255,194,random(1,100));
  //stroke(255,random(1,100));
  //float r2 = random(20,20);
  //rect(mouseX,mouseY,r2,r2);
}
