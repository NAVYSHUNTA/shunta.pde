int x = width / 2;
int y = height / 2;
int scale = 5;

void setup(){
  size(600, 600);
  frameRate(1000 / scale);
}

void draw(){
  int up = (int)random(3) - 1;
  int right = (int)random(3) - 1;
  up *= scale;
  right *= scale;
  line(x, y, x + up, y + right);
  x += up;
  y += right;
}
