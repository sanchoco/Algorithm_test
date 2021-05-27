// https://programmers.co.kr/learn/courses/30/lessons/1845
// 폰켓몬

function solution(nums) {
	return Math.min(nums.length / 2, [...new Set(nums)].length);
}

console.log(solution([3,1,2,3]))
console.log(solution([3,3,3,2,2,4]))
console.log(solution([3,3,3,2,2,2]))
