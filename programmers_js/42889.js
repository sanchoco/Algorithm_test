// https://programmers.co.kr/learn/courses/30/lessons/42889
// 실패율

function solution(N, stages) {
	let fail = {}; // 스테이지별 실패한 인원을 저장
	stages.forEach((stage) => {
		fail[stage] = (fail[stage] || 0) + 1; // 실패인원 누적
	})
	let len = stages.length;
	let temp = []
	for (let stage = 1; stage <= N; stage++){
		let success = 0;
		if (!fail[stage]) {
			fail[stage] = 0; // 실패한 인원이 없으면 0
		}
		else (fail[stage])
			success = fail[stage] / len; // 실패율 계산
		temp.push([stage, success])
		len -= fail[stage]
	}
	temp.sort((a, b) => b[1] - a[1]); // 실패율 정렬

	return temp.map((value) => value[0]);
}

let N = 5;
let stages = [2, 1, 2, 6, 2, 4, 3, 3]
console.log(solution(N, stages))

// let N = 4;
// let stages = [4,4,4,4,4]
// console.log(solution(N, stages))
