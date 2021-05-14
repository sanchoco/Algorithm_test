// https://programmers.co.kr/learn/courses/30/lessons/42748
// K번째수

function solution(array, commands) {
	let answer = [];
	for (let command of commands) {
		let [i, j, k] = command;
		let temp_arr = array.slice(i - 1, j);
		answer.push(temp_arr.sort((a,b)=>a-b)[k - 1]);
	}
	return answer;
}

const array = [1, 5, 2, 6, 3, 7, 4]
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
console.log(solution(array, commands))
