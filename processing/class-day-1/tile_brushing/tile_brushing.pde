


TileObject tile;

void setup()
{
  size(800, 800);
  //fill(255, 204);
  smooth();
  //noStroke();
  tile = new TileObject();
  background(0);
  frameRate(300);
}
 
void draw()
{  
  //tint(random(0,255)); //,random(0,255),random(0,255));
  tile.clear();
  tile.saveImage();
  tile.bomb();
}
 
void mouseDragged() {
  tile.brushStroke();
  tile.createCurve();
} 

class TileObject 
{
  //PShape tileshape = loadShape("/Users/colin/Documents/test.svg");   
   PImage tileshape = loadImage(
   "/Users/mh/Dropbox/projects/processing/class-day-1/tile_brushing/tile3438.tif");   
   
  
  float coord[];
  float sy[];

  
  TileObject() {
        tileshape.resize(20,20);
    coord = new float[0];
    sy = new float[0];

  }
 
  void createCurve(){
     append(coord, mouseX);
     append(coord, mouseY);
          stroke(255,0,0);
          //noStroke();
     beginShape();
     curveVertex(pmouseX,pmouseY);
          curveVertex(pmouseX,pmouseY);
     curveVertex(mouseX,mouseY);
          curveVertex(mouseX,mouseY);
     endShape();

  }

  void brushStroke() {
    
    imageMode(CENTER);
    
    float distance = dist(pmouseX,pmouseY,mouseX,mouseY);
    float amt = float(ceil(distance)) * 1;

    int i = 1;
    while (i<amt) {
      float x = lerp(pmouseX,mouseX,i/amt);
      float y = lerp(pmouseY,mouseY,i/amt);
      //rotate(random(i));
    image(tileshape, x, y);  
    image(tileshape, (x - width),(y));
    image(tileshape, (x + width),(y));
    image(tileshape, (x),(y + height));
    image(tileshape, (x),(y - height));
    image(tileshape, (x - width),(y - height));
    image(tileshape, (x + width),(y + height));
    image(tileshape, (x + width),(y - height));
    image(tileshape, (x - width),(y + height));
    i++;
    }
  }
  
    void bomb() {
    
    imageMode(CENTER);
  
    if (keyPressed) {  
  
       if (key == 'b') {
         
         float x = random(frameCount);
         float y = random(frameCount);
    rotate(random(frameCount));

    image(tileshape, x, y);  
    image(tileshape, (x - width),(y));
    image(tileshape, (x + width),(y));
    image(tileshape, (x),(y + height));
    image(tileshape, (x),(y - height));
    image(tileshape, (x - width),(y - height));
    image(tileshape, (x + width),(y + height));
    image(tileshape, (x + width),(y - height));
    image(tileshape, (x - width),(y + height));
       }
    }
  }
    //clear    
  void clear() {
    if (keyPressed) {
      if (key == 'c') {        
        background(0);  
      }
    }
  }
  
  void saveImage() {
    //save
    if (keyPressed) {
      if (key == 's') {
        String filename = "tile" + millis() + ".tif";        
        save(filename);
      }
    }
  }
  
  void preview() {
    //preview
    if (keyPressed) {
      if (key == 'p') {
        
      }
    }
    
  }

}
