function solution(array, commands) {
  var answer = [];
  for (let i = 0; i < commands.length; i++) {
    let start = commands[i][0];
    let end = commands[i][1];
    let pick = commands[i][2] - 1;
    let tmp = array.slice(start - 1, end);
    tmp.sort((a, b) => a - b);
    console.log(tmp);
    answer.push(tmp[pick]);
  }

  return answer;
}
