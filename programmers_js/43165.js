// https://programmers.co.kr/learn/courses/30/lessons/43165?language=javascript
// 타겟 넘버

function recurive(numbers, target, depth, total) {
	if (numbers.length === depth) {
		if (target === total)
			return 1;
		else
			return 0;
	}
	let case1 = recurive(numbers, target, depth + 1, total + numbers[depth])
	let case2 = recurive(numbers, target, depth + 1, total - numbers[depth])
	return case1 + case2;
}

function solution(numbers, target) {
	let answer = recurive(numbers, target, 0, 0);
    return answer;
}
