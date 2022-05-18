for (var x in x_y_data) {
    var xArray = x_y_data[x][0];
    var yArray = x_y_data[x][1];
    var temp = {
        x: xArray,
        y: yArray,
        mode: "markers",
        type: 'scatter',
        name: x
    };
    data.push(temp);
}

// Define Layout
var layout = {
    xaxis: xtitle,
    yaxis: ytitle,
    title: maintitle,
    width: 1200,
    height: 370,
};

// Display using Plotly
Plotly.newPlot("myPlot", data, layout);