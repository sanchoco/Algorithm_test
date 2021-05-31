// https://programmers.co.kr/learn/courses/30/lessons/42746
// 가장 큰 수

function solution(numbers) {
	if (numbers.length === 0)
		return '';
	let sortNum = numbers.map(number => number + '').sort((a, b) => (b + a) - (a + b)).join('');
	if (sortNum[0] == '0')
		return '0'
	return sortNum;
}
