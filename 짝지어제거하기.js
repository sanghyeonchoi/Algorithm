function solution(s) {
  let answer = 0;
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (stack.length === 0 || stack[stack.length - 1] !== s[i]) {
      stack.push(s[i]);
    } else {
      stack.pop();
    }
  }
  if (stack.length === 0) answer = 1;
  return answer;
}

console.log(solution("baabaa"));
