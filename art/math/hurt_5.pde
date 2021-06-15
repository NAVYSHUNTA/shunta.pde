final float sec = 1;
float x, y1, y2, num1, num2, num3, time, base_time, radius;

void setup(){
  size(800, 800);
  colorMode(HSB, 359, 99, 99);
  background(0, 0, 99);
  noStroke();
  radius = 5;
}

void draw(){
  float time = millis() - base_time;
  translate(400, 400);
  rotate(radians(180));
  for(x = 0;x < 1.14;x += 0.0001){
    num1 = pow(x, 2.0 / 3.0);
    num2 = sq(num1) - 4 * (sq(x) - 1);
    num3 = sqrt(num2);
    y1 = (num1 + num3) / 2.0;
    y2 = (num1 - num3) / 2.0;
    rotate(radians(10 * (int)(mouseX * 0.01)));
    fill(300, 100, 100);
    circle(250 * x, 250 * y1, radius);
    circle(250 * x, 250 * y2, radius);
    circle(-250 * x, 250 * y1, radius);
    circle(-250 * x, 250 * y2, radius);
  }
  if(time < sec * 1000){
    return;
  }
  base_time = millis();
  background(0, 0, 99);
}
