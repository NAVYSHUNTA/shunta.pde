float n, k, t1, t2, skip, translation;

void setup(){
  size(800, 800);
  frameRate(100);
  n = 31;
  k = 0;
  translation = width / 2.0;
  skip = 0;
}

void draw(){
  function();
  k++;
  if(k == n){
    k = 0;
    skip++;
    function();
  }
}

void function(){
  t1 = 2 * PI * k / n;
  t2 = 2 * PI * (k + skip) / n;
  line(400 * cos(t1) + translation, 400 * sin(t1) + translation, 400 * cos(t2) + translation, 400 * sin(t2) + translation);
}
