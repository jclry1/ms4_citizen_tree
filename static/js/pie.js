// https://www.chartjs.org/docs/latest/getting-started/usage.html
// https://www.chartjs.org/docs/latest/configuration/legend.html
// https://stackoverflow.com/questions/37292423/chart-js-label-color


function chart(){
var ctx = document.getElementById('co2_doughnut');
let total_donor_sink = JSON.parse(document.getElementById('d_sink_chart').textContent);
let chart_sink_kg = total_donor_sink.donor_sink;
let var_total_sink = document.getElementById("chartVal").value; //JSON option not working after deploying so trying this as temp workaround
//let chart_sink_tonne = parseInt(chart_sink_kg / 1000);
  var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [
          'Irl. Emissions - Annual (T)',
          'CT Sink - Annual (Kg)',
        ],
        datasets: [{
          label: 'Citizen Tree Sequestration',
          data: [60000000, var_total_sink],
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
              size: 16,
            }
          }
        }
      }
    }
  });

}
setTimeout(() => chart(), 1500); //Test - Give time for page content to load so that the function can get the value from template
