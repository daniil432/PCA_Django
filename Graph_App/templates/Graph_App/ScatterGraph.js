var xArray = x_y_data;
var yArray = x_y_data;

// Define Data
var data1 = {
    x: xArray['donor'][0],
    y: yArray['donor'][1],
    mode: "markers",
    type: 'scatter',
    name: '1'
};

var data2 = {
    x: xArray['myeloma'][0],
    y: yArray['myeloma'][1],
    mode: "markers",
    type: 'scatter',
    name: '2'
};

var data = [data1, data2];

// Define Layout
var layout = {
    xaxis: {title: "PC1"},
    yaxis: {title: "PC2"},
    title: "Graph in PC1-PC2 coordinates"
};

// Display using Plotly
Plotly.newPlot("myPlot", data, layout);