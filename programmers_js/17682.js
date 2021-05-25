// https://programmers.co.kr/learn/courses/30/lessons/17682
// 다트게임

function solution(dartResult) {
	let temp = 0;
	let score = [];
	for (let c of dartResult) {
		if (!isNaN(c))
			temp = 10 * temp + parseInt(c);
		else {
			if (c === 'S') {
				score.push(temp)
			} else if (c === 'D') {
				score.push(Math.pow(temp, 2))
			} else if (c === 'T') {
				score.push(Math.pow(temp, 3))
			} else if (c === '*') {
				score[score.length - 1] *= 2;
				if (score.length >= 2) {
					score[score.length - 2] *= 2;
				}
			} else if (c === '#') {
				score[score.length - 1] *= -1;
			}
			temp = 0;
		}
	}
	let answer = score.reduce((pre, curr) => pre + curr);
	return answer;
}

// console.log(solution('1S2D*3T'))
// console.log(solution('1D2S#10S'))
// console.log(solution('1D2S0T'))
// console.log(solution('1S*2T*3S'))
console.log(solution('1D#2S*3S'))
