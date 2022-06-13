google.charts.load("current", { packages: ["timeline"] });
google.charts.setOnLoadCallback(drawChart);

function getDigit(number, n) {
  return Math.floor((number / Math.pow(10, n - 1)) % 10);
}

function getTime(time) {
  digitCnt = Math.max(Math.floor(Math.log10(Math.abs(time))), 0) + 1;

  minutes = getDigit(time, 2) * 10 + getDigit(time, 1);

  hours = getDigit(time, 3);

  if (digitCnt == 4) {
    hours += getDigit(time, 4) * 10;
  }

  return [hours, minutes];
}
function drawChart() {
  var container = document.getElementById("example5.3");
  var chart = new google.visualization.Timeline(container);
  var dataTable = new google.visualization.DataTable();

  dataTable.addColumn({ type: "string", id: "Room" });
  dataTable.addColumn({ type: "string", id: "Name" });
  dataTable.addColumn({ type: "date", id: "Start" });
  dataTable.addColumn({ type: "date", id: "End" });

  var AllCourses = [];
  var OneCourseData = [];
  for (let i = 0; i < Object.keys(data).length; i++) {
    var course = data[i].fields;
    var starttime = getTime(course.starttime);
    var endtime = getTime(course.endtime);

    if (course.days == "W") {
      OneCourseData = [
        course.location,
        String(course.code),
        new Date(0, 0, 0, starttime[0], starttime[1], 0),
        new Date(0, 0, 0, endtime[0], endtime[1], 0),
      ];

      AllCourses.push(OneCourseData);
    }
  }

  dataTable.addRows(AllCourses);

  var options = {
    timeline: { colorByRowLabel: true },
    backgroundColor: "",
  };

  chart.draw(dataTable, options);
}

/*
  dataTable.addColumn({ type: "string", id: "Room" });
  dataTable.addColumn({ type: "string", id: "Name" });
  dataTable.addColumn({ type: "date", id: "Start" });
  dataTable.addColumn({ type: "date", id: "End" });
  dataTable.addRows([
    [
      "Magnolia Room",
      "CSS Fundamentals",
      new Date(0, 0, 0, 12, 0, 0),
      new Date(0, 0, 0, 14, 0, 0),
    ],
    [
      "Magnolia Room",
      "Intro JavaScript",
      new Date(0, 0, 0, 14, 30, 0),
      new Date(0, 0, 0, 16, 0, 0),
    ],
    [
      "Magnolia Room",
      "Advanced JavaScript",
      new Date(0, 0, 0, 16, 30, 0),
      new Date(0, 0, 0, 19, 0, 0),
    ],
    [
      "Gladiolus Room",
      "Intermediate Perl",
      new Date(0, 0, 0, 12, 30, 0),
      new Date(0, 0, 0, 14, 0, 0),
    ],
    [
      "Gladiolus Room",
      "Advanced Perl",
      new Date(0, 0, 0, 14, 30, 0),
      new Date(0, 0, 0, 16, 0, 0),
    ],
    [
      "Gladiolus Room",
      "Applied Perl",
      new Date(0, 0, 0, 16, 30, 0),
      new Date(0, 0, 0, 18, 0, 0),
    ],
    [
      "Petunia Room",
      "Google Charts",
      new Date(0, 0, 0, 12, 30, 0),
      new Date(0, 0, 0, 14, 0, 0),
    ],
    [
      "Petunia Room",
      "Closure",
      new Date(0, 0, 0, 14, 30, 0),
      new Date(0, 0, 0, 16, 0, 0),
    ],
    [
      "Petunia Room",
      "App Engine",
      new Date(0, 0, 0, 16, 30, 0),
      new Date(0, 0, 0, 18, 30, 0),
    ],
    [
      "Petunia Room",
      "Wub",
      new Date(0, 0, 0, 18, 30, 0),
      new Date(0, 0, 0, 20, 30, 0),
    ],
  ]);

  var options = {
    timeline: { colorByRowLabel: true },
    backgroundColor: "#ffd",
  };

  chart.draw(dataTable, options);
}
*/
