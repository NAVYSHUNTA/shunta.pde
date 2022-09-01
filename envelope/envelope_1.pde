int x, y, t;

void setup(){
  size(800, 800);
  frameRate(40);
  x = 9;
  y = 11;
}

void draw(){
  t++;
  line(pow(x * cos(t), 3) + width / 2.0, x + width / 2.0, width / 2.0, pow(y * sin(t), 3) + width / 2.0);
}
