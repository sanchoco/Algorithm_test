// https://programmers.co.kr/learn/courses/30/lessons/1845
// 폰켓몬

function solution(nums) {
	let arr = [...(new Set(nums))];
	let max = Math.floor(nums.length / 2);
	return max >= arr.length ? arr.length : max;
}

console.log(solution([3,1,2,3]))
console.log(solution([3,3,3,2,2,4]))
console.log(solution([3,3,3,2,2,2]))
