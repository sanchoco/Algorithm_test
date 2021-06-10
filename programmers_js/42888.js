// https://programmers.co.kr/learn/courses/30/lessons/42888
// 오픈 채팅방

function solution(record) {
	let nickname = {};
	let log = [];
	for (let msg of record) {
		let info = msg.split(' ')
		if (info[0] === 'Enter') {
			nickname[info[1]] = info[2];
			log.push(['Enter', info[1]])
		} else if (info[0] === 'Change') {
			nickname[info[1]] = info[2];
		} else {
			log.push(['Leave', info[1]])
		}
	}
	return log.map((msg) => {
		if (msg[0] === 'Enter')
			return `${nickname[msg[1]]}님이 들어왔습니다.`
		else
			return `${nickname[msg[1]]}님이 나갔습니다.`
	});
}

let record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"];
console.log(solution(record))
