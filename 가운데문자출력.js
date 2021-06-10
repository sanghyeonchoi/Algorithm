function solution(s) {
  let answer = "",
    mid = Math.floor(s.length / 2);
  for (let x of s) {
    if (s.length % 2 == 1) {
      answer = s.substr(mid, 1);
    } else {
      answer = s.substr(mid - 1, 2);
    }
  }

  return answer;
}
console.log(solution("good"));
