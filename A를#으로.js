function solution(s) {
  let answer = "";
  for (let x of s) {
    if (x == "A") {
      answer += "#";
    } else {
      answer += x;
    }
  }
  return answer;
}
//정규식 표현
function solution2(s) {
  s = s.replace(/A/g, "#");
  return s;
}

let str = "BANANA";
console.log(solution(str));
console.log(solution2(str));
