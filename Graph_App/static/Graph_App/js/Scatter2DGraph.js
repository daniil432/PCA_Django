var data = [];
for (let x in x_y_data) {
    let xArray = x_y_data[x][0];
    let yArray = x_y_data[x][1];
    let temp = {
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
document.getElementById('myPlot').innerHTML = xArray;
Plotly.newPlot("myPlot", data, layout);
