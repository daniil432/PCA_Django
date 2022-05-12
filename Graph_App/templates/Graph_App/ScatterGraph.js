var x_y_data = JSON.parse('{{x_y_data|escapejs}}');
var data = [];
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
    xaxis: {title: "PC{{ data.0 }}"},
    yaxis: {title: "PC{{ data.1 }}"},
    title: "Graph in PC{{ data.0 }}-PC{{ data.1 }} coordinates",
    width: 1200,
    height: 370,
};

// Display using Plotly
Plotly.newPlot("myPlot", data, layout);