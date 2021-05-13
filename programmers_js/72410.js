// https://programmers.co.kr/learn/courses/30/lessons/72410
// 신규 아이디 추천
function solution(new_id) {
	new_id = new_id.toLowerCase() // level 1
	new_id = new_id.replace(/[^0-9a-z-_.]/gi, '') // level 2
	new_id = new_id.replace(/[.]{1,}/gi, '.') // level 3
	if (new_id[0] == '.') new_id = new_id.substr(1, new_id.length); // level 4
	if (new_id[new_id.length - 1] == '.') new_id = new_id.substr(0, new_id.length - 1);
	if (new_id.length == 0) new_id = 'a'; // level 5
	if (new_id.length >= 16) { // level 6
		new_id = new_id.substr(0, 15);
		if (new_id[new_id.length - 1] == '.') new_id = new_id.substr(0, new_id.length - 1);
	}
	if (new_id.length <= 2) { // level 7
		let last_char = new_id[new_id.length - 1];
		while (new_id.length < 3) new_id += last_char;
	}
	return new_id;
}

console.log(solution('...!@BaT#*..y.abcdefghijklm.'))
console.log(solution('z-+.^.'))
console.log(solution('=.='))
console.log(solution('123_.def'))
console.log(solution('abcdefghijklmn.p'))
console.log(solution("-_.~!@#$%^&*()=+[{]}:?,<>/._-"))
