// https://programmers.co.kr/learn/courses/30/lessons/43165?language=javascript
// 타겟 넘버

function recurive(numbers, target, depth, total) {
	if (numbers.length === depth)
		return (target === total) ? 1 : 0;
	return recurive(numbers, target, depth + 1, total + numbers[depth])
		+ recurive(numbers, target, depth + 1, total - numbers[depth])
}

function solution(numbers, target) {
	return recurive(numbers, target, 0, 0);
}

console.log (solution([1, 1, 1, 1, 1], 3))
