var data = [];
var xArray = x_y_data['x'];
var yArray = x_y_data['y'];
var temp = {
    x: xArray,
    y: yArray,
    mode: "lines",
};
data.push(temp);


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