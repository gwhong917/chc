
var test_pie = document.getElementById("testPieChart");
var testPieChart = new Chart(test_pie, {
  type: 'pie',
  data: {
    labels: ['bold', 'progay', 'programmer', 'smoker'],
    datasets: [{
      data: pie_chart_test,
      backgroundColor: [
        "#f7323f",
        "#673ba7",
        "#ffc107",
        "#28a745"
      ],
      borderWidth:0
    }]
  }
});
