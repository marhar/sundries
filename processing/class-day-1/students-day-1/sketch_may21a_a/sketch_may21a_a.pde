


// this happens once

void setup() {
  size(600,400);
  background(232,166,33);
}

float time = -20;


// this happens over and over

void draw() {
  fill(100,100,200,60);
  stroke(200,0,0);
  rect(0,0,width,height/4);

  fill(50,50,100,2);
  rect(width/2,0,width/4,height);


  float speed = 1;
  time = time + 1;
  int howManyDots = 10;
  for (int i=0; i<howManyDots; i++) {
    float x = i*10 + time * speed;
    if (x > width + 20) {
      time = 0;
    }
    float y = 100 * sin( i + time * 0.03) * 100;
    y = y + i*10 + 200; //offset
    fill(200,100,200);
    ellipse(x,y,40,40);
  }
  
  fill(232,166,33);
  stroke(246,255,124);
  //rect(sin((i + time*0.05)*100),cos((i + time*0.05)*100),20,20);
  
  fill(0,0,100);
  stroke(100,0,0);
  //rect(x + y,y,60,60);
  



}







