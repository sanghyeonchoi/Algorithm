function solution(people, limit) {
  var answer = 0;
  people.sort((a, b) => b - a);
  for (let i = 0, j = people.length - 1; i <= j; i++) {
    if (people[i] + people[j] <= limit) j--;
    answer++;
  }
  return answer;
}
console.log(solution([70, 50, 80, 50], 100));
