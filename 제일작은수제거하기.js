function solution(arr) {
  let min = Math.min(...arr);
  if (arr.length <= 1) return [-1];
  let i = arr.findIndex((val) => val === min);
  arr.splice(i, 1);

  return arr;
}
