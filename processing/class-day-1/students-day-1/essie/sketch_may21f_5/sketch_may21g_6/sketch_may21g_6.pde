float time = 0;

void setup() {
  size(1000,1000); // width and height of screen
  background(100,61,66);
  

// int x =0;
  
}


//outside the curly bracket - inside doesn't allow this for sharing

void draw() {
  fill (0,0,0,200);
  stroke (204, 102, 0);
  // noStroke();
  float speed = 1; // Bend of curve?
  time = time + 3; // speed of float 
  float x = time * speed; // x is referring to time
  if (x > width) {
    time = 0;
    
  }
  // y is where on the rect. does it begin
  float y = 100 * sin(time * 0.05);
  y = y + 200; //offset
  ellipse(x,y,30,40);
}
