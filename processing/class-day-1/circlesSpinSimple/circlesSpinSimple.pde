void draw(){
  //smooth();
  //noStroke();
  int numC = 10;
  float space = TWO_PI / numC;

  background(200);
  float cX = width/2;
  float cY = height/2;
  float speed = -frameCount * .05;
  float rad = 40;
  float curS = 0;
  for (int i = 0; i < numC; i++) {
    //rad += (sin(curS + speed * 10) * 5) ;
    float x = mouseX;
    float y = mouseY;
    x = cX + (sin(speed + curS) * rad);
    y = cY + (cos(speed + curS) * rad);
    ellipse(x,y,10,10);
    curS += space;
  }
}

