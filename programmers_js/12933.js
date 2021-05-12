// https://programmers.co.kr/learn/courses/30/lessons/12933
// 정수 내림차순으로 배치하기

function solution(n) {
	var answer = n.toString().split('').sort().reverse().join('');
    return parseInt(answer);
}

console.log(solution(118372))
