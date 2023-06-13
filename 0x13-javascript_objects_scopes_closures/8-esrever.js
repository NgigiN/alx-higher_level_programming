#!/usr/bin/node

exports.esrever = function (list) {
  const i = [];
  let count = 0;
  let limit = list.length;
  while (count < list.length) {
    i[count] = list[limit - 1];
    count++;
    limit--;
  }
  return i;
};
