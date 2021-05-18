// https://programmers.co.kr/learn/courses/30/lessons/42576?language=javascript
// 완주하지 못한 선수

function solution(participant, completion) {
	participant.sort()
	completion.sort()
	while (participant.length) {
		let p = participant.pop()
		let c = completion.pop()
		if (p != c) {
			return p
		}
	}
}

let participant = ["leo", "kiki", "eden"]
let completion = ["eden", "kiki"]
console.log(solution(participant, completion))
