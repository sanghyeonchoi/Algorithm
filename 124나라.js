function solution(n) {
  let answer = "";
  let arr = ["4", "1", "2"];
  let tmp = 0;
  while (n > 0) {
    tmp = n % 3;
    n = parseInt(n / 3);
    if (tmp === 0) n = n - 1;
    answer = arr[tmp] + answer;
  }
  return answer;
}
console.log(solution(3));
