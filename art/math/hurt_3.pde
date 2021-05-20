float x, y1, y2, num1, num2, num3;

void setup(){
  size(800, 800);
  frameRate(1000);
  x = 0;
}

void draw(){
  num1 = pow(x, 2.0 / 3.0);
  num2 = sq(num1) - 4 * (sq(x) - 1);
  num3 = sqrt(num2);
  y1 = (num1 + num3) / 2.0;
  y2 = (num1 - num3) / 2.0;
  ellipse(width - (250 * x + width / 2.0), width - (250 * y1 + width / 2.0), 10, 10);
  ellipse(width - (250 * x + width / 2.0), width - (250 * y2 + width / 2.0), 10, 10);
  ellipse(width - (-250 * x + width / 2.0), width - (250 * y1 + width / 2.0), 10, 10);
  ellipse(width - (-250 * x + width / 2.0), width - (250 * y2 + width / 2.0), 10, 10);
  x += 0.001;
}
