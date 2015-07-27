float time = 0;

void setup() {
  size(300,300); // width and height of screen
  background(0,61,66);
  

// int x =0;
  
}


//outside the curly bracket - inside doesn't allow this for sharing

void draw() {
  fill (200,200,0,200);
  rect(0,0,width,heights);
  float speed = 1;
  time = time + 1; 
  int howManyDots = 5;
  for (int i=0; i<howManyDots; i++) {
    float y = sin(i + time * 0.05) * 100;
    float x = cos(i + time * 0.05) * 100;
  x = x + width/2;
  x = x + width/2; //offset
  fill(255,0,0);
  ellipse(x,y,30,40);
    
  }
}

