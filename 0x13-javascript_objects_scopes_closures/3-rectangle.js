#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
	    this.width = 0;
	    this.height = 0;
    } else {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let count = 0; count < this.height; count++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
