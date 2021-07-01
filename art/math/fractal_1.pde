float radian, size;

void setup(){
  size(800, 800);
  radian = 2 * PI / 3.0;
  size = 400;
  background(250);
}

void draw(){
  background(250);
  translate(400, 450);
  rotate(-PI / 2.0);
  fill(0);
  triangle(size * cos(0 * radian), size * sin(0 * radian), size * cos(1 * radian), size * sin(1 * radian), size * cos(2 * radian), size * sin(2 * radian));
  rotate(PI);
  size /= 2.0;
  function0();
  size /= 2.0;
  function1();
  size /= 2.0;
  function2();
  size /= 2.0;
  function3();
  size /= 2.0;
  function4();
  size /= 2.0;
  function5();
  size /= 2.0;
  function6();
  noLoop();
}

void function0(){
  fill(250);
  triangle(pow(2, 0) * size * cos(0 * radian), size * sin(0 * radian), pow(2, 0) * size * cos(1 * radian), size * sin(1 * radian), size * cos(2 * radian), size * sin(2 * radian));
}


void function1(){
  for (int count = 0; count < 3; count++){
    pushMatrix();
    translate(pow(2, 1) * size * cos(count * radian - PI / 3.0), pow(2, 1) * size * sin(count * radian - PI /3.0));
    function0();
    popMatrix();
  }
}

void function2(){
  for (int count = 0; count < 3; count++){
    pushMatrix();
    translate(pow(2, 2) * size * cos(count * radian - PI / 3.0), pow(2, 2) * size * sin(count * radian - PI /3.0));
    function1();
    popMatrix();
  }
}

void function3(){
  for (int count = 0; count < 3; count++){
    pushMatrix();
    translate(pow(2, 3) * size * cos(count * radian - PI / 3.0), pow(2, 3) * size * sin(count * radian - PI /3.0));
    function2();
    popMatrix();
  }
}

void function4(){
  for (int count = 0; count < 3; count++){
    pushMatrix();
    translate(pow(2, 4) * size * cos(count * radian - PI / 3.0), pow(2, 4) * size * sin(count * radian - PI /3.0));
    function3();
    popMatrix();
  }
}

void function5(){
  for (int count = 0; count < 3; count++){
    pushMatrix();
    translate(pow(2, 5) * size * cos(count * radian - PI / 3.0), pow(2, 5) * size * sin(count * radian - PI /3.0));
    function4();
    popMatrix();
  }
}

void function6(){
  for (int count = 0; count < 3; count++){
    pushMatrix();
    translate(pow(2, 6) * size * cos(count * radian - PI / 3.0), pow(2, 6) * size * sin(count * radian - PI /3.0));
    function5();
    popMatrix();
  }
}
