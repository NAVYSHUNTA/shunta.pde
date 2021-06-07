final int sec = 10;
boolean waiting = true;

void setup(){
  //初期条件
}

void draw(){  
  if(waiting && millis() < sec * 1000){
    return;
  }
  waiting = false;
  //処理
}
