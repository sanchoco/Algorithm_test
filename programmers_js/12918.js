//https://programmers.co.kr/learn/courses/30/lessons/12918
// 문자열 다루기 기본

function solution(s) {
	if (!(s.length == 4 || s.length == 6) || s.includes('e'))
		return false;
	return Number.isInteger(+s) ? true : false;
}

console.log(solution('1e22'))
