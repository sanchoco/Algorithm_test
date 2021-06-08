// https://programmers.co.kr/learn/courses/30/lessons/12899
// 124 나라의 숫자

function solution(n) {
	let num = ['4', '1', '2']
	let result = ''
	while (true) {
		result = num[n % 3] + result;
		n = Math.floor(n / 3) + (n % 3 == 0 ? -1 : 0);
		if (n == 0)
			break;
	}
	return result;
}

console.log(solution(5))
console.log(solution(8))
