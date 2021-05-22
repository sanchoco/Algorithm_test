// https://programmers.co.kr/learn/courses/30/lessons/43238
// 입국심사

function solution(n, times) {
	let answer = 0;
	let left = 0;
	let right = n * Math.max.apply(null, times);
	while (left <= right) {
		let mid = Math.floor((left + right) / 2);
		let checkNum = times.reduce((prev, curr) => prev + Math.floor(mid / curr), 0);
		if (n <= checkNum) {
			answer = mid;
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	return answer;
}

console.log(solution(6,[7,10]))
