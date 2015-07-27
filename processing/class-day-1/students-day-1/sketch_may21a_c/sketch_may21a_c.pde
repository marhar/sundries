float time = 0;

void setup () {
  
  size(512,512);
  background(112,222,23);
}
void draw (){
    color c1 = color(255,255,255,0) ;
color c2 = color(20,20,20);
color c3 = color(255,255,255,70);
fill(0,0,0,20);
rect(0,0,width,height);
float speed =1;

time = time +1;
for (int i=0; i<100; i++) {

float x = (i*5 +time * speed);
if (x>width) {
  time = 0; 
}
float y = 100 * cos(i +time * 0.05);
y = y + 200;

  stroke (c1) ;
  fill (c3 );
  ellipse(x,y,30,40);
}
}
  



