#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};
for (const k in dict) {
  if (newDict[dict[k]] === undefined) {
    newDict[dict[k]] = [k];
  } else {
    newDict[dict[k]].push(k);
  }
}
console.log(newDict);
