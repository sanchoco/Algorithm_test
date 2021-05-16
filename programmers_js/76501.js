// https://programmers.co.kr/learn/courses/30/lessons/76501
// 음양 더하기
function solution(absolutes, signs) {
	let answer = 0;
	for (let i = 0; i < absolutes.length; i++){
		if (signs[i] === true)
			answer += absolutes[i];
		else
			answer -= absolutes[i];
	}
	return answer;
}
