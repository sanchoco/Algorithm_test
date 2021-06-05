// https://programmers.co.kr/learn/courses/30/lessons/12930
// 이상한 문자 만들기

function solution(s) {
	let even = 0
	return s.split('').map((c) => {
		if (c == ' ') {
			even = 0;
			return c;
		}
		else {
			even += 1;
			return (even % 2 == 1) ? c.toUpperCase() : c.toLowerCase()
		}
	}).join('')
}
