// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var test_pie = document.getElementById("myPieChart").getContext('2d');
var testPieChart = new Chart(test_pie, {
  type: 'pie',
  data: {
    labels: ['Bold', 'Progay', 'Programmer', 'Smoker'],
    datasets: [{
      data: pie_chart_test,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745']
    }]
  }
});
