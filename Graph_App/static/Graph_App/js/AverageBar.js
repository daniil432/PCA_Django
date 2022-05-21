var nameArray = ['Amide-1', 'Min-1-2', 'Side-chains', 'Min-sch-3', 'Amide-2'];
var data = [];
var count = 0;
for (let i = 0; i < x_y_data['donor'][1].length; i++) {
    let tempinner = Array(x_y_data['donor'][1].length).fill([]);
    for (let x in x_y_data) {
        let one = x_y_data[x][1][i]
        if (one) {
            tempinner[i].push(one);
        }
    }
    count++
    let temp = {
        x: ['donor', 'myeloma', 'non-secreting'],
        y: tempinner[i],
        type: "bar",
        xaxis: 'x' + count.toString(),
        yaxis: 'y' + count.toString(),
        name: nameArray[count-1]
    };
    data.push(temp)
}

var layout = {
    grid: {rows: 1, columns: 5, pattern: 'independent'},
    xaxis: {domain: [0, 0.1]},
    xaxis2: {domain: [0.2, 0.3]},
    xaxis3: {domain: [0.4, 0.5]},
    xaxis4: {domain: [0.6, 0.7]},
    xaxis5: {domain: [0.8, 0.9]},
    yaxis1: {range: [1644, 1645]},
    yaxis2: {range: [1579, 1581]},
    yaxis3: {range: [1572, 1574]},
    yaxis4: {range: [1504, 1509]},
    yaxis5: {range: [1452, 1454]},
    width: 1250,
    height: 470,
};

Plotly.newPlot("myPlot", data, layout);
