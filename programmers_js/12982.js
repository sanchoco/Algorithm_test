// https://programmers.co.kr/learn/courses/30/lessons/12982
// 예산

function solution(d, budget) {
	let answer = 0;
	d.sort((a, b) => a - b)
	let total = 0
	for (let element of d) {
		total += element
		if (total <= budget)
			answer += 1;
		else
			break;
	}
    return answer;
}

const d = [1, 3, 2, 5, 4]
const budget = 9
console.log(solution(d, budget))
