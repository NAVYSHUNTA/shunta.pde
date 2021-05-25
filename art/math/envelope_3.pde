float time;

void setup(){
  size(800, 800);
  frameRate(20);
}

void draw(){
  time += 10;
  line(time, width, width - time, time);
  line(0, width - time, width - time, time);
  line(width - time, 0, time, width - time);
  line(width, time, time, width - time);
}
