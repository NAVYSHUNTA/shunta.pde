int x, y;
int scale = 5;

void setup(){
  size(600, 600);
  frameRate(1000 / scale);
  x = width / 2;
  y = height / 2;
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
