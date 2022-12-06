function show_plot() {
    document.getElementById("loader").style.display="block";
    var ticker = document.getElementById("ticker").value;
    var type = document.getElementById('type').value;
    var dataPoints = [];
    var predPoints = [];
    var stockChart = new CanvasJS.StockChart("chartContainer",{
    exportEnabled: true,
    animationEnabled: true,
    zoomEnabled: true,
    title: {
        text: ticker,
        fontSize : 20,
        fontWeight: "bolder",
        fontColor: "dodgerblue",
        fontFamily: "tahoma",
      },
    axisX:{
        valueFormatString: "yyyy-MM-dd hh:mm:ss",
      },
    axisY:{
        title: "Cryptocurrency in INR",
        lineColor: "#369EAD",
        },
    charts: [{
      data: [
      {
        type: "line",
        name : 'Trend',
        showInLegend: true,
        color: 'dodgerblue',
        xValueFormatString : "DD-MM-YYYY hh:mm:ss",
        dataPoints : dataPoints
      },{
        type: "line", //Change it to "spline", "area", "column"
        name : 'Predicted',
        showInLegend: true,
        color: '#DC143C',
        xValueFormatString : "DD-MM-YYYY hh:mm:ss",
        dataPoints : predPoints
      }]
    }
    ],
  });

  $.get("http://localhost:5000/getJson/"+ticker, function(data) {
    document.getElementById("loader").style.display="none";
    for(var i = 0; i < data[0].length; i++){
      dataPoints.push({x: new Date(data[0][i].date), y: Number(data[0][i].close)});
    }
    for(var i = 0; i < data[1].length; i++){
      predPoints.push({x: new Date(data[1][i].date), y: Number(data[1][i].close)});
    }

    stockChart.render();
  });

};
