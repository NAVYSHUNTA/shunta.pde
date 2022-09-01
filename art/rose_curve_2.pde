void setup(){
  size(800, 800);
  colorMode(HSB, 359, 99, 99);
  background(0, 0, 99);
  noStroke();
}

void draw(){
  translate(400, 400);
  background(0, 0, 99);
  float a = (int)mouseX / 50.0;
  for(float x = 0;x <= 2 * PI;x += 0.001){
    fill(1000 * x % 360, 300, 200);
    ellipse(300 * sin(a * x) * sin(x), 300 * sin(a * x) * cos(x), 1, 80);
  }
}
