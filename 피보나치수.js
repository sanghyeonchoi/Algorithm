function solution(n) {
  var answer = 0;
  let tmp = [];
  tmp[0] = 0;
  tmp[1] = 1;
  for (let i = 2; i <= n; i++) {
    tmp[i] = (tmp[i - 1] + tmp[i - 2]) % 1234567;
  }
  answer += tmp[n];
  return answer;
}
