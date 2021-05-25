float time;

void setup(){
  size(800, 800);
  frameRate(20);
}

void draw(){
  time += 0.01 * (mouseX + mouseY);
  line(0, time, time, width);
  line(time, width, width, width - time);
  line(0, time, width - time, 0);
  line(width, width - time, width - time, 0);
}
