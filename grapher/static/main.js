google.charts.load('current', { packages: ['timeline'] });
google.charts.setOnLoadCallback(drawChart);
window.addEventListener('DOMContentLoaded', (event) => {
	loadChartCSS();
});

const search = document.getElementById('location');
const matchList = document.getElementById('matchList');

$(window).resize(function () {
	drawChart();
});

//returns individual digits of large numbers
function getDigit(number, n) {
	return Math.floor((number / Math.pow(10, n - 1)) % 10);
}

//breaks up datetime formats into mins and secs for Google charts
function getTime(time) {
	digitCnt = Math.max(Math.floor(Math.log10(Math.abs(time))), 0) + 1;

	minutes = getDigit(time, 2) * 10 + getDigit(time, 1);

	hours = getDigit(time, 3);

	if (digitCnt == 4) {
		hours += getDigit(time, 4) * 10;
	}

	return [hours, minutes];
}

var rowFontFamily = '';
var rowFontSize = 16;
var barFontFamily = '';
var barFontSize = 16;

function loadChartCSS() {
	rowFontFamily = getFontFamily('rows');
	rowFontSize = getFontSize('rows');
	barFontFamily = getFontFamily('bars');
	barFontSize = getFontSize('bars');
}

function getFontSize(id) {
	var el = document.getElementById(id);
	var style = window.getComputedStyle(el, null).getPropertyValue('font-size');
	var fontSize = parseFloat(style);
	return fontSize;
}

function getFontFamily(id) {
	var el = document.getElementById(id);
	var style = window
		.getComputedStyle(el, null)
		.getPropertyValue('font-family');
	style = style.replace(/['"]+/g, '');
	return style;
}

AllLocations = [];
function drawChart() {
	var container = document.getElementById('timeline');
	var chart = new google.visualization.Timeline(container);
	var dataTable = new google.visualization.DataTable();

	dataTable.addColumn({ type: 'string', id: 'Room' });
	dataTable.addColumn({ type: 'string', id: 'Name' });
	dataTable.addColumn({ type: 'date', id: 'Start' });
	dataTable.addColumn({ type: 'date', id: 'End' });

	var AllCourses = [];
	var OneCourseData = [];
	for (var i = 0; i < Object.keys(data).length; i++) {
		var course = data[i].fields;
		var starttime = getTime(course.starttime);
		var endtime = getTime(course.endtime);

		OneCourseData = [
			course.location,
			String(course.code),
			new Date(0, 0, 0, starttime[0], starttime[1], 0),
			new Date(0, 0, 0, endtime[0], endtime[1], 0),
		];

		AllLocations.push(course.location);
		AllCourses.push(OneCourseData);
	}
	
	dataTable.addRows(AllCourses);
	dataTable.addRows([
		['~DEV~', String(00000), new Date(0, 0, 0, 7, 0, 0), new Date(0, 0, 0, 23, 0, 0)]
	]);
	//hardcoded start and end courses to keep charts even
	chart.draw(dataTable);

	var options = {
		colors: ['#f35d45', '#089aff', '#facd58'],
		timeline: {
			showBarLabels: true,
			colorByRowLabel: true,
			rowLabelStyle: {
				fontName: rowFontFamily,
				fontSize: rowFontSize,
			},
			barLabelStyle: {
				fontName: barFontFamily,
				fontSize: barFontSize,
			},
		},
		backgroundColor: '',
		alternatingRowStyle: false,
	};

	chart.draw(dataTable, options);
}

//search allcourses list and filter it
function searchLocations(searchText) {
	console.log(searchText);
	let matches = AllLocations.filter((room) => {
		const regex = new RegExp(`^${searchText}`, 'gi');
		return room.match(regex);
	});

	if (searchText.length === 0) {
		matches = [];
		matchList.innerHTML = '';
	}
	console.log(matches);
	outputHtml(matches);
}

//show results in html
const outputHtml = (matches) => {
	if (matches.length > 0) {
		const html = matches
			.map(
				(match) => `
		<div class="card card-body mb-1">
			<h4>${match} <span class="text-primary"></span></h4>
		</div>`
			)
			.join('');
		//matchList.innerHTML = html;
	}
};

if (search) {
	search.addEventListener('input', () => searchLocations(search.value));
}
