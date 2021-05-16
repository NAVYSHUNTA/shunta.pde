float x;

void setup(){
  size(800, 800);
  frameRate(1000);
  x = -0.3;
}

void draw(){
  x+= 0.001;
  float a = pow(x, 2.0 / 3.0);
  float b = sqrt(1 - sq(x));
  ellipse(250 * x + 400, 800-(200 * (a + b) + 300), 10, 10);
  ellipse(250 * x + 400, 800-(200 * (a - b) + 300), 10, 10);
  ellipse(-250 * x + 400, 800-(280 * (a + b) + 350), 10, 10);
  ellipse(-250 * x + 400, 800-(280 * (a - b) + 350), 10, 10);
}
