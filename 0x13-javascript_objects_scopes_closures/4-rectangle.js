#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
  // Method that initialize a instance
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print ()
  {
    for(let count = 0; count < this.height; count++)
    {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
