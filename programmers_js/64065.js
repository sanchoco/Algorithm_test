// https://programmers.co.kr/learn/courses/30/lessons/64065
// 튜플

function solution(s) {
	s = s.slice(1, -1).replace(/\},/gi, '}|');
	let arr = s.split('|').map((value) => value.slice(1, -1).split(','))
	arr = arr.sort((a, b) => a.length - b.length)
		.map((lst) => lst.map((value) => +value).sort((a, b) => a - b))
	let result = [];
	let before_arr = [];
	arr.forEach(element => {
		result.push(element.filter((x) => !before_arr.includes(x))[0]);
		before_arr = element;
	})
	return result;
}


console.log(solution("{{2,1},{2},{2,1,3},{2,1,3,4}}"))
console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
