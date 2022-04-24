var chart;

JSC.fetch(
  './resources/fertilityRateAndLifeExpectancy.csv'
)
  .then(function(response) {
    return response.text();
  })
  .then(function(text) {
    var data = JSC.csv2Json(text);
    chart = renderChart(data);
  });
function renderChart(data) {
  var series = [
    {
      name: '""""""""""""""Category name 1""""""""""""""',
      type: 'marker',
      points: data.map(function(item) {
        return {
          x: item.fertility_rate1960,
          y: item.life_expectancy1960,
          name: item.country
        };
      })
    },
    {
      name: '""""""""""""""Category name 2""""""""""""""',
      type: 'marker',
      points: data.map(function(item) {
        return {
          x: item.fertility_rate1990,
          y: item.life_expectancy1990,
          name: item.country
        };
      })
    },
    {
      name: '""""""""""""""Category name 3""""""""""""""',
      type: 'marker',
      points: data.map(function(item) {
        return {
          x: item.___dataforxaxes___,
          y: item.___dataforxaxes___,
          name: item.___name___
        };
      })
    }
  ];
  return JSC.chart('chartDiv', {
    axisToZoom: 'xy',
    defaultPoint: {
      tooltip:
        '<b>%"""name of category"""</b><br>%"""x value label""": <b>%xValue</b><br>%"""y value label"""": <b>%yValue</b>',
      opacity: 0.8,
      marker: {
        type: 'circle',
        outline_width: 0,
        size: 12
      }
    },
    legend_template: '%icon %name',
    yAxis: {
      label_text: '"""""""""""label text y"""""""""""',
      alternateGridFill: 'none'
    },
    xAxis: {
      scale_range: [0, 10],
      label_text: '""""""""""label text x""""""""""'
    },
    series: series
  });
}