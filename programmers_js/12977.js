// https://programmers.co.kr/learn/courses/30/lessons/12977
// 소수 만들기

function isPrime(number) {
	if (number === 1)
		return false;
	for (let i = 2; i <= Math.sqrt(number); i++)
		if (number % i === 0)
			return false;
	return true;
}

function solution(nums) {
	let count = 0;
	for (let i = 0; i < nums.length - 2; i++)
		for (let j = i + 1; j < nums.length - 1; j++)
			for (let k = j + 1; k < nums.length; k++)
				if (isPrime(nums[i] + nums[j] + nums[k]))
					count++;
	return count;
}

console.log(solution([1, 2, 3, 4]))
console.log(solution([1, 2, 7, 6, 4]))
