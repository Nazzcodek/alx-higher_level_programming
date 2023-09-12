#!/usr/bin/node

exports.function = function (x, theFunction) {
  for (let i = 0; i < x; i++)
    console.log(theFunction);
}
