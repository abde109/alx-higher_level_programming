#!/usr/bin/node
const { dict } = require('./101-data.js');
const sortedDict = {};
for (const key in dict) {
  if (!sortedDict[dict[key]]) {
    sortedDict[dict[key]] = [];
  }
  sortedDict[dict[key]].push(key);
}
console.log(sortedDict);
