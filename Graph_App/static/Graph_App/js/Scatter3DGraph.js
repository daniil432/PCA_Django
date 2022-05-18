for (var x in x_y_data) {
    var xArray = x_y_data[x][0];
    var yArray = x_y_data[x][1];
    var zArray = x_y_data[x][2];
    var temp = {
        x: xArray,
        y: yArray,
        z: zArray,
        mode: "markers",
        marker: {
            size: 9,
            line: {
                width: 0.5
            },
            opacity: 0.8
        },
        type: 'scatter3d',
        name: x
    };
    data.push(temp);
}

// Define Layout
var layout = {
    xaxis: xtitle,
    yaxis: ytitle,
    zaxis: ztitle,
    title: maintitle,
    width: 1200,
    height: 370,
};

// Display using Plotly
Plotly.newPlot("myPlot", data, layout);