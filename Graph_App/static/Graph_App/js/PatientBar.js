var nameArray = ['Amide-1', 'Min-1-2', 'Side-chains', 'Min-sch-3', 'Amide-2'];
var data = [];
var count = 0;
for (let elem = 0; elem < x_y_data['donor'][1][0].length; elem++) {
    let oneDataset = [];
    let nameDataset = [];
    for (let who in x_y_data) {
        for (let pat in x_y_data[who][1]) {
            oneDataset.push(x_y_data[who][1][pat][elem]);
        }
        nameDataset.push.apply(nameDataset, x_y_data[who][2])
    }
    count++
    let fullDataset = {
        x: nameDataset,
        y: oneDataset,
        type: "bar",
        xaxis: 'x' + count.toString(),
        yaxis: 'y' + count.toString(),
        name: nameArray[count-1]
    }
    data.push(fullDataset);
}

var layout = {
    grid: {rows: 1, columns: 5, pattern: 'independent'},
    xaxis: {domain: [0, 0.1]},
    xaxis2: {domain: [0.2, 0.3]},
    xaxis3: {domain: [0.4, 0.5]},
    xaxis4: {domain: [0.6, 0.7]},
    xaxis5: {domain: [0.8, 0.9]},
    yaxis1: {range: [1643, 1646]},
    yaxis2: {range: [1578, 1582]},
    yaxis3: {range: [1571, 1575]},
    yaxis4: {range: [1503, 1510]},
    yaxis5: {range: [1451, 1455]},
    width: 1250,
    height: 470,
};
console.log(data)
//document.getElementById('myPlot').innerHTML = data;
Plotly.newPlot("myPlot", data, layout);