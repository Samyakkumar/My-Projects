function WordString(stringLength, stringLocation){
    this.stringLength = stringLength;
    this.stringLocation = stringLocation;
    this.words = []
    this.randNum = random(97, 122 - this.stringLength)
    this.velocity = random(1, 4)
    this.fontSize = map(this.velocity, 1, 4, 20, 11)
    this.startY = stringLocation.y
    for(var i = randNum; i < randNum + this.stringLength;i++){
      this.words.push(String.fromCharCode(i))
    }
    this.show = function(){
      for(var i = 0; i < this.words.length; i++){
        text(this.words[i], this.stringLocation.x, this.startY)
      }
    }
    this.move = function(){
      this.startY += this.velocity
    }

}

myWords = [];

function setup() {
  createCanvas(600, 600);
  myWords.push(WordString(15, createVector(random(width), random(-300, -100))))
  console.log(myWords)
}

function draw() {
  background(51);
  for(var i = 0; i < myWords.length; i++){
    word = myWords[i];
    word.show()
    word.move()
  }
}
