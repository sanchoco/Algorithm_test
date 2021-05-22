// https://programmers.co.kr/learn/courses/30/lessons/77484
// 로또의 최고 순위와 최저 순위

function solution(lottos, win_nums) {
	let count = lottos.reduce((acc, curr) => acc + (win_nums.includes(curr)? 1 : 0 ) ,0)
	let zeroCount = lottos.reduce((acc, curr) => acc + (curr === 0 ? 1 : 0), 0)
	return [
		((count + zeroCount) >= 2) ? (7 - (count + zeroCount)) : 6,
		(count >= 2) ? 7 - count : 6
	]
}

let lottos = [44, 1, 0, 0, 31, 25]
let win_nums = [31, 10, 45, 1, 6, 19]
console.log(solution(lottos, win_nums))

