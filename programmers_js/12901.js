// https://programmers.co.kr/learn/courses/30/lessons/12901
// 2016년

function solution(a, b) {
	const week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
	const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	let day = 5 + b - 1; // 금요일부터 시작
	for (let i = 0; i < a-1; i++)
		day += month[i];
	let answer = week[day % 7];
	return answer;
}

const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

for (let i = 0; i < 12; i++){
	for (let j = 0; j < month[i]; j++) {
		console.log(`${i+1}월 ${j+1}일은`,solution(i+1,j+1))
	}
}
