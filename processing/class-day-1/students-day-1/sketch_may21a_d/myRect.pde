/**
 * Objects
 * by hbarragan. 
 * 
 * Move the cursor across the image to change the speed and positions
 * of the geometry. The class MRect defines a group of lines.
 */
 
class MRect 
{
  float w; // single bar width
  float xpos; // rect xposition
  float h; // rect height
  float ypos ; // rect yposition
 
  MRect(float ixpos, float iypos, float iw, float ih) {
    w = iw;
    xpos = ixpos;
    h = ih;
    ypos = iypos;
  }
 
  void move (float posX, float posY, float damping) {
    float dif = ypos - posY;
    if (abs(dif) > 1) {
      ypos -= dif/damping;
    }
    dif = xpos - posX;
    if (abs(dif) > 1) {
      xpos -= dif/damping;
    }
  }

  void setSize (float iw, float ih) {
    w = iw;
    h = ih;
  }
 
  void display() {
    ellipse(xpos,ypos,w,h);
  }
}
