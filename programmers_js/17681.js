// https://programmers.co.kr/learn/courses/30/lessons/17681
// 비밀지도

function solution(n, arr1, arr2) {
	return arr1.map((num, i) => {
		num = num | arr2[i];
		let bin = num.toString(2).padStart(n, '0');
		return bin.replace(/0/g, ' ').replace(/1/g, '#')
	});
}

let n = 5;
let arr1 = [9, 20, 28, 18, 11]
let arr2 = [30, 1, 21, 17, 28]
console.log(solution(n, arr1, arr2))
