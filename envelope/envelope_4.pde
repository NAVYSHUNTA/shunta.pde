float x, y;

void setup(){
  size(800, 800);
  frameRate(30);
  x = 0;
  y = 0;
}

void draw() {
  x += 10;
  function1();
  if(x >= width){
    y += 10;
    function2();
  }
}

void function1(){
  line(x, width, width - x, x);
  line(0, width - x, width - x, x);
  line(width - x, 0, x, width - x);
  line(width, x, x, width - x);
}
void function2(){
  line(0, y, y, width);
  line(y, width, width, width - y);
  line(0, y, width - y, 0);
  line(width, width - y, width - y, 0);
}
