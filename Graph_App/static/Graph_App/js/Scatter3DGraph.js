var data = [];
for (let x in x_y_data) {
    let xArray = x_y_data[x][0];
    let yArray = x_y_data[x][1];
    let zArray = x_y_data[x][2];
    let temp = {
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
    autosize: false,
    width: 1000,
    height: 1000,
    xaxis: xtitle,
    yaxis: ytitle,
    zaxis: ztitle,
    title: maintitle,
    margin: {
        l: 0,
        r: 0,
        b: 0,
        t: 0
    }
};

// Display using Plotly
Plotly.newPlot("myPlot", data, layout);