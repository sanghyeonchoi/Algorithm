function solution(s) {
  var answer = "";
  let arr = s.split("");
  if (s.length % 2 === 1) answer += arr[Math.floor(s.length / 2)];
  else if (s.length % 2 === 0)
    answer += arr[Math.floor(s.length / 2 - 1)] + arr[Math.floor(s.length / 2)];
  return answer;
}
