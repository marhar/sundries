float time = 0;

void setup() {
  size(300,300); // width and height of screen
  background(0,61,66);
  

// int x =0;
  
}


//outside the curly bracket - inside doesn't allow this for sharing

void draw() {
  fill (0,0,0,10);
  rect(0,0,width,height);
  float speed = 1;
  time = time + 1; 
  int howManyDots = 10;
  for (int i=0; i<howManyDots; i++) {
    float y = sin(i + time * 0.05) * 100;
    float x = cos(i + time * 0.05) * 100;
  x = x + width/2;
  y = y + height/2; //offset
  fill(255,0,0);
  ellipse(x,y,30,40);
    
  }
}

