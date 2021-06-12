function solution(s) {
  let answer;
  let arr = [];
  for (let x of s) {
    if (x === ")") {
      while (arr.pop() !== "(");
    } else arr.push(x);
  }
  answer = arr.join("");
  return answer;
}

let str = "(A(BC)D)EF(G(H)(IJ)K)LM(N)";
console.log(solution(str));
