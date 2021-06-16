function solution(s) {
  let answer = 0;
  let sum = 0;
  function DFS(L, sum) {
    if (sum > s) return false;
    if (sum === s) return true;
    else return DFS(L + 1, sum + L);
  }
  for (let i = 1; i <= s; i++) {
    if (DFS(i, sum)) answer++;
  }
  return answer;
}
console.log(solution(15));
