// https://programmers.co.kr/learn/courses/30/lessons/67256
// 키패드 누르기
// 1 2 3
// 4 5 6
// 7 8 9
// * 0 #

function position(number) {
	if (number === 0) {
		return [1, 3]
	} else if (number === '*') {
		return [0, 3]
	} else if (number === '#') {
		return [2, 3]
	}
	let x = (number + 2) % 3;
	let y = parseInt((number - 1) / 3)
	return [x, y];
}

function distance(num1, num2) {
	let [num1_x, num1_y] = position(num1);
	let [num2_x, num2_y] = position(num2);
	let dis = Math.abs(num1_x - num2_x) + Math.abs(num1_y - num2_y)
	return dis
}

function solution(numbers, hand) {
	let answer = '';
	let last_L = '*'
	let last_R = '#'
	numbers.map((num) => {
		if ([1, 4, 7].includes(num)) {
			answer += 'L'
			last_L = num
		} else if ([3, 6, 9].includes(num)) {
			answer += 'R'
			last_R = num
		} else {
			if (distance(num, last_L) < distance(num, last_R)) {
				answer += 'L'
				last_L = num
			} else if (distance(num, last_L) > distance(num, last_R)) {
				answer += 'R'
				last_R = num
			} else {
				if (hand === 'left') {
					answer += 'L'
					last_L = num
				} else {
					answer += 'R'
					last_R = num
				}
			}
		}
	})
	return answer;
}

let numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
let hand = 'right'
console.log(solution(numbers, hand))

