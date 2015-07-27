
MRect[] r = new MRect[201];
int count = 100;

void setup(){
  size(640,360);
  //fill(255, 204);
  //noStroke();
  for(int i=0; i<count; i++){
    r[i] = new MRect(0,0,20,20);
  }
}

void draw(){

  background(255);
  for(int i=0; i<count; i++){
    //r[i] = new MRect(0,0,20,20);
    r[i].setSize(count-i,count-i);
    
    r[i].move(mouseX, mouseY, (count-i)*2);
    r[i].display();
    
  }
  

  
  //float frame = frameCount;
  
  //float w = sin(frame/100)*100;//random(0,25+frameCount);
  //float h = sin(frame/100)*100;//random(0,25+frameCount);
  
  //translate (mouseX,mouseY);
  //rotate (frame/100);
  //translate (-w/2,-h/2);
  //rect(0,0,w,w);
  //rotate (-frame/100);
  
  //float[] col = new float[4];
  //col[0] = random(0,random(150,random(150,250)));
  //col[1] = random(150,200);
  //col[2] = random(100,255);
  //col[3] = 100-sin(frame/100)*50;
  
  //fill(col[0],col[1],col[2],col[3]);
  //stroke(255,255,255,255);
}
