function solution(answers) {
	const select_one = [1, 2, 3, 4, 5];
	const select_two = [2, 1, 2, 3, 2, 4, 2, 5]
	const select_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	let score = [0, 0, 0];
	for (let i = 0; i < answers.length; i++) {
		if (answers[i] === select_one[i % select_one.length])
			score[0] += 1;
		if (answers[i] === select_two[i % select_two.length])
			score[1] += 1;
		if (answers[i] === select_three[i % select_three.length])
			score[2] += 1;
	}
	let max = Math.max(...score)
	let answer = [];
	for (let i = 0; i < score.length; i++){
		if (score[i] == max)
			answer.push(i+1)
	}
	return answer;
}


console.log(solution([1,2,3,4,5]))
