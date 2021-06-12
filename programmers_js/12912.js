//https://programmers.co.kr/learn/courses/30/lessons/12912
// 두 정수 사이의 합

function solution(a, b) {
	let result = 0;
	if (a < b) {
		while (a <= b)
			result = result + a++;
	} else {
		while (b <= a)
			result = result + b++;
	}
	return result;
}

console.log(sum(3,5))
