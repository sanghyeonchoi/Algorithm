function solution(n) {
  return parseInt([...n.toString(3)].reverse().join(""));
}
console.log(solution(125));
