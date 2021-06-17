function solution(record) {
  var answer = [];
  let users = {};

  let stateMapping = {
    Enter: "님이 들어왔습니다.",
    Leave: "님이 나갔습니다.",
  };
  record.forEach((v) => {
    let [state, id, name] = v.split(" ");
    if (state !== "Change") {
      answer.push([state, id]);
    }
    if (name) {
      users[id] = name;
    }
  });

  return answer.map(([state, uid]) => {
    return `${users[uid]}${stateMapping[state]}`;
  });
}
let record = [
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
];
console.log(solution(record));
