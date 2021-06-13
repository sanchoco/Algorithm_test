// https://programmers.co.kr/learn/courses/30/lessons/42579
// 베스트 앨범

function solution(genres, plays) {
	let songs = {}
	let genres_total = {}
	// 장르별 음악 묶기
	for (let i in genres) {
		if (songs[genres[i]]) {
			songs[genres[i]].push([i, plays[i]]);
			genres_total[genres[i]] += plays[i];
		}
		else {
			songs[genres[i]] = [[i, plays[i]]];
			genres_total[genres[i]] = plays[i];
		}
	}
	// 장르별 총 재생수 배열로 가공
	let genres_sort = []
	for (let key in genres_total) {
		songs[key].sort((a, b) => (a[1] == b[1]) ? (+a[0]) - (+b[0]) : b[1] - a[1]);
		genres_sort.push([key, genres_total[key]])
	}
	genres_sort.sort((a, b) => b[1] - a[1]); // 우선 장르
	let result = [];
	for (let value of genres_sort) {
		songs[value[0]].slice(0,2).map((element)=>{result.push(+element[0])})
	}

	return result;
}

let genres = ["classic", "pop", "classic", "classic", "pop"];
let plays = [500, 600, 150, 800, 2500];
console.log(solution(genres, plays))
