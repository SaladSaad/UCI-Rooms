google.charts.load("current", { packages: ["timeline"] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var container = document.getElementById("example5.3");
  var chart = new google.visualization.Timeline(container);
  var dataTable = new google.visualization.DataTable();

  dataTable.addColumn({ type: "string", id: "Room" });
  dataTable.addColumn({ type: "string", id: "Name" });
  dataTable.addColumn({ type: "date", id: "Start" });
  dataTable.addColumn({ type: "date", id: "End" });
  dataTable.addRows([
    [
      "PCB 1300",
      "16425",
      new Date(0, 0, 0, 8, 0, 0),
      new Date(0, 0, 0, 9, 50, 0),
    ],
    [
      "ELH 110",
      "16438",
      new Date(0, 0, 0, 21, 0, 0),
      new Date(0, 0, 0, 21, 50, 0),
    ],
  ]);

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
