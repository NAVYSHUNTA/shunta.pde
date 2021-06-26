int x, y, vx, vy, c;
int score, gameover;

import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;

Minim minim;
AudioPlayer music;
String s;

void setup() {
  colorMode(HSB, 359, 99, 99);
  noStroke();
  frameRate(30);
  ini();
  score = 0;
  gameover = 0;
  textSize(48);
  size(360, 360);
  minim = new Minim(this);
  s = "http://www.is.kyusan-u.ac.jp/~goshi/d/irish.mp3";
  music = minim.loadFile(s, 2048);
  music.play();
}
void draw() {
  fill(0, 0, 0);
  text("SCORE: "+score, 0, 50);
  if (gameover == 1) {
    fill(0, 99, 99);
    text("GAME OVER", 70, 180);
    return;
  }
  fade();
  x += vx;
  y += vy;
  vy++;
  fill(c, 99, 99);
  ellipse(x, y, 40, 40);
  if (y > 360) {
    ini();
  }
  if (y > 340 && abs(x-mouseX)< 30) {
    if (c > 0) {
      score++;
    }
    if (c == 0) {
      gameover = 0;
    }
  }
  fill(0, 0, 0);
  rect(mouseX - 15, 340, 30, 30);
}

void fade() {
  fill(0, 0, 99, 30);
  rect(0, 0, 360, 360);
}

void ini() {
  x = 360;
  y = 100;
  vy = -10;
  vx = -1*(int)random(10);
  c = (int)random(300);
  if (c < 100) {
    c = 0;
  }
}
