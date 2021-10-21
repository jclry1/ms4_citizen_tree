// https://www.chartjs.org/docs/latest/getting-started/usage.html
// https://www.chartjs.org/docs/latest/configuration/legend.html
// https://stackoverflow.com/questions/37292423/chart-js-label-color


function chart(){
var ctx = document.getElementById('co2_doughnut');
let total_donor_sink = JSON.parse(document.getElementById('d_sink_chart').textContent);
let chart_sink_kg = total_donor_sink.donor_sink;
let chart_sink_tonne = parseInt(chart_sink_kg / 1000);
  var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [
          'Ireland Emissions - Annual (Tonnes)',
          'Citizen Tree Sink - Annual (Tonnes)',
        ],
        datasets: [{
          label: 'Citizen Tree Sequestration',
          data: [60000000, chart_sink_tonne],
          backgroundColor: [
            'rgb(250, 250, 250)',
            'rgb(100, 0, 0)',
          ],
          hoverOffset: 4,
          cutout: '75%',
        }]
    },
    options: {
      plugins: {
        legend: {
          display: true,
          labels: {
            color: "white",
            font: {
              size: 20,
            }
          }
        }
      }
    }
  });

}
setTimeout(() => chart(), 1500); //Test - Give time for page content to load so that the function can get the value from template
