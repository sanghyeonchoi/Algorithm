function solution(numbers, target) {
  var answer = 0;
  function DFS(L, sum) {
    if (L === numbers.length) {
      if (sum === target) {
        answer++;
      }
    } else {
      DFS(L + 1, sum + numbers[L]);
      DFS(L + 1, sum - numbers[L]);
    }
  }
  DFS(0, 0);
  return answer;
}

let numbers = [1, 1, 1, 1, 1];
console.log(solution(numbers, 3));
