// https://programmers.co.kr/learn/courses/30/lessons/12903?language=javascript
// 가운데 글자 가져오기

function solution(s) {
	let answer = '';
	let len = s.length;
	let mid = parseInt(len / 2);

	// 길이가 짝수인 경우
	if (len % 2 == 0)
		answer = s.slice(mid-1, mid+1);
	else
		answer = s.slice(mid, mid+1);
	return answer;
}

const s = "asdfasdf"
console.log(solution(s))
