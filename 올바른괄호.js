function solution(s) {
  let answer = "YES";
  let arr = [];
  for (let x of s) {
    if (x == "(") arr.push();
    else {
      if (arr.length === 0) return "NO";
      arr.pop();
    }
  }
  if (arr.length > 0) return "NO";

  return answer;
}

let a = "(()(()))(()";
console.log(solution(a));
