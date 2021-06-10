// https://programmers.co.kr/learn/courses/30/lessons/60058
// 괄호 변환
function check(s) {
	let p = []
	for (let c of s) {
		if (c === '(')
			p.push(1);
		else if (c === ')' && p.length > 0)
			p.pop();
		else
			return false
	}
	if (p.length === 0)
		return true;
	else
		return false;
}

function solution(p) {
	if (p === '')
		return ''

	let count = 0;
	let i = 0;
	while (p[i]) {
		if (p[i] === '(')
			count++;
		else
			count--;
		if (count === 0)
			break;
		i++;
	}
	let u = p.slice(0, i + 1);
	let v = p.slice(i + 1, p.length);
	if (check(u)) {
		return u + solution(v);
	} else {
		return '(' + solution(v) + ')' +
			u.slice(1, -1).replace(/\(|\)/g, c => (c === "(") ? ")" : "(");
	}
}

// console.log(solution("(()())()"))
// console.log(solution(")("))
console.log(solution("())))((()()"))
