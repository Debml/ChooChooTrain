var DEFAULT_DATASET_SIZE = 7;
var myLineChart, myDoughnutChart, myStackedChart, myPolarChart, myBubbleChart;

var randomScalingFactor = function() {
        return Math.round(Math.random() * 100);
    };

$(document).ready(function(){    
    $('#carousel-example-generic').on('slide.bs.carousel', function (e) {
        var currentIndex = $('div.active').index();
        var slideTo = $(e.relatedTarget).index();
        updateChart(currentIndex, slideTo);
    })
});

function updateChart(currentIndex, slideTo){
    create_chart(slideTo,currentIndex);
}

function create_chart(slideTo, currentIndex){
    if(slideTo == 1){
        create_line_chart(currentIndex);
    }
    else if (slideTo == 2){
        create_doughnut_chart(currentIndex);
    }
    else if (slideTo == 3){
        create_stacked_chart(currentIndex);
    }
    else if (slideTo == 4){
        create_polar_chart(currentIndex);
    }
    else if (slideTo == 5){
        create_bubble_chart(currentIndex);
    }
    else{
        
    }
}

function destroy_chart(currentIndex){
    if(currentIndex == 1){
        //destroy line chart
        myLineChart.clear();
    }
    else if (currentIndex == 2){
        //destroy chart
        myDoughnutChart.clear();
    }
    else if (currentIndex == 3){
        myStackedChart.clear();
    }
    else if (currentIndex == 4){
        myPolarChart.clear();
    }
    else if (currentIndex == 5){
        myBubbleChart.clear();
    }
    else{
        
    }
}

function create_line_chart(currentIndex){
    var data1 = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "Time",
                fill: false,
                lineTension: 0.2,
                backgroundColor: "rgba(255,99,132,0.4)",
                borderColor: window.chartColors.red,
                borderCapStyle: 'butt',
                borderDash: [5, 5],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(255,99,132,0.4)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: window.chartColors.red,
                pointHoverBorderColor: window.chartColors.red,
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [5, 19, 30, 31, 23, 25, 15],
                spanGaps: false,
            }
        ]
    };
    var ctx = document.getElementById("myLineChart").getContext("2d");
    ctx.canvas.width = 20;
    ctx.canvas.height = 20;
    myLineChart = new Chart(ctx, {
        type: 'line',
        data: data1,
        options: {
                responsive: true,
                legend: {
                    position: 'right',
                    fullWidth: false,
                    labels: {
                        boxWidth: 15
                    }
                },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                    }
                }
    });
    destroy_chart(currentIndex);
}

function create_bubble_chart(currentIndex){
    var addedCount = 0;
    var color = Chart.helpers.color;
    var bubbleChartData = {
        animation: {
            duration: 10000
        },
        datasets: [{
            label: "Block1",
            backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
            borderColor: window.chartColors.red,
            borderWidth: 2,
            data: [{
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }]
        }, {
            label: "Block2",
            backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
            borderColor: window.chartColors.blue,
            borderWidth: 2,
            data: [{
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }]
        }, {
            label: "Block3",
            backgroundColor: color(window.chartColors.green).alpha(0.5).rgbString(),
            borderColor: window.chartColors.green,
            borderWidth: 2,
            data: [{
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }, {
                x: randomScalingFactor(),
                y: randomScalingFactor(),
                r: Math.abs(randomScalingFactor()) / 5,
            }]
        }]
    };
    var ctx = document.getElementById("myBubbleChart").getContext("2d");
    myBubbleChart = new Chart(ctx, {
        type: 'bubble',
        data: bubbleChartData,
        options: {
            layout: {
            padding: 10,
            },
            responsive: true,
            legend: {
            position: 'right',
            fullWidth: false,
            labels: {
                boxWidth: 15
            }
            },
            tooltips: {
                mode: 'point'
            }
        }
    });
    destroy_chart(currentIndex);
}

function create_polar_chart(currentIndex){
    var color = Chart.helpers.color;
    var config4 = {
        data: {
            datasets: [{
                data: [
                    60,
                    22,
                    56,
                    70,
                    30,
                    50,
                    12,
                    63,
                    45,
                    50,
                ],
                backgroundColor: [
                    color(chartColors.red).alpha(0.7).rgbString(),
                    color(chartColors.orange).alpha(0.7).rgbString(),
                    color(chartColors.yellow).alpha(0.7).rgbString(),
                    color(chartColors.green).alpha(0.7).rgbString(),
                    color(chartColors.blue).alpha(0.7).rgbString(),
                    color(chartColors.red).alpha(0.7).rgbString(),
                    color(chartColors.orange).alpha(0.7).rgbString(),
                    color(chartColors.yellow).alpha(0.7).rgbString(),
                    color(chartColors.green).alpha(0.7).rgbString(),
                    color(chartColors.blue).alpha(0.7).rgbString()
                ],
            }],
            labels: [
                "var1",
                "var2",
                "var3",
                "var4",
                "var5",
                "list1",
                "list2",
                "list3",
                "list4",
                "list5"
            ]
        },
        options: {
            responsive: true,
            legend: {
                position: 'right',
                fullWidth: false,
                labels: {
                    boxWidth: 15
                }
            },
            scale: {
            ticks: {
                beginAtZero: true
            },
            reverse: false
            },
            animation: {
                animateRotate: false,
                animateScale: true
            }
        }
    };
    var ctx = document.getElementById("myPolarChart");
    myPolarChart = Chart.PolarArea(ctx, config4);
    destroy_chart(currentIndex);
}

function create_doughnut_chart(currentIndex){
    var ctx = document.getElementById("myDoughnutChart").getContext("2d");
    ctx.canvas.width = 20;
    ctx.canvas.height = 20;
    myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [
                10,
                20,
                70,
            ],
            backgroundColor: [
                window.chartColors.red,
                window.chartColors.orange,
                window.chartColors.yellow,
            ],
            label: 'Dataset 1'
        }],
        labels: [
            "Block1",
            "Block2",
            "Block3",
        ]
    },
    options: {
        responsive: true,
        legend: {
            position: 'right',
            fullWidth: false,
            labels: {
                        boxWidth: 15
                    }
        },
        animation: {
            animateScale: true,
            animateRotate: true
        }
    }
});
    destroy_chart(currentIndex);
}

function create_stacked_chart(currentIndex){
    var ctx = document.getElementById("myStackedChart").getContext("2d");
    ctx.canvas.width = 20;
    ctx.canvas.height = 20;
    var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var config1 = {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
        label: "Block1",
        borderColor: window.chartColors.red,
        backgroundColor: window.chartColors.red,
        data: [
                        20, 
                        120, 
                        0, 
                        -30, 
                        -90, 
                        33, 
                        149
                    ],
        }, {
        label: "Block2",
        borderColor: window.chartColors.blue,
        backgroundColor: window.chartColors.blue,
        data: [
                        -20, 
                        20, 
                        10, 
                        0, 
                        90, 
                        133, 
                        9
                    ],
        }, {
        label: "Block3",
        borderColor: window.chartColors.green,
        backgroundColor: window.chartColors.green,
        data: [
                        -110, 
                        -66, 
                        -122, 
                        100, 
                        0, 
                        11, 
                        39
                    ],
        }]
    },
    options: {
        responsive: true,
        title:{
        display:false,
        text:"Chart.js Line Chart - Stacked Area"
        },
        legend: {
            position: 'right',
            fullWidth: false,
            labels: {
                boxWidth: 15
            }
        },
        tooltips: {
        mode: 'index',
        },
        hover: {
        mode: 'index'
        },
        scales: {
        xAxes: [{
        }],
        yAxes: [{
            stacked: true,
        }]
        }
    }
    };
    myStackedChart = new Chart(ctx, config1);
    destroy_chart(currentIndex);
}

// resize block code
function resizeTextarea (id) {
  var a = document.getElementById(id);
  a.style.height = a.scrollHeight+'px';
}

//resize block code
function init() {
  var a = document.getElementsByTagName('textarea');
  for(var i=0,inb=a.length;i<inb;i++) {
     if(a[i].getAttribute('data-resizable')=='true')
      resizeTextarea(a[i].id);
  }
}

// html loads, print code on html, compile python
function load_code() {
    //get code from python
}

function get_request_ajax(uri){
    $.ajax({
            url: uri,
            type: "GET",
            contentType: "application/json",
            success: function (jsonResponse) {
                //code retreived, call method to append to html
                code_returned = jsonResponse.code;
                show_code(code_returned);
            },
            error: function (errorMessage) {
                alert(errorMessage);
            }
        });
}

function post_request_ajax(uri,data_js){
  $.ajax({
            url: uri,
            type: "POST",
            data: data_js,
            dataType: "json",
            contentType: "application/json",
            success: function (jsonResponse) {
                result_code = jsonResponse.result;
                if(result_code == 1) {
                    alert("Code sent");
                    location.replace("runtime.html");
                }
                else {
                    alert("ERROR: Code not sent");
                }
            },
            error: function (errorMessage) {
                alert(errorMessage);
            }
        });
}

//custom alert
function create_bootstrap_success_alert(strong_t, normal_t){
  var node_alert = document.createElement("DIV"); 
  var node_dismiss_alert = document.createElement("A");
  var node_strong_text = document.createElement("STRONG"); 
  var node_span = document.createElement("SPAN");
  
  //has two children: dismiss and text
  node_alert.setAttribute("class","alert alert-success alert-dismissable fade in");

  node_dismiss_alert.setAttribute("href","#");
  node_dismiss_alert.setAttribute("class","close");
  node_dismiss_alert.setAttribute("data-dismiss","alert");
  node_dismiss_alert.setAttribute("aria-label","close");

  var span_text = document.createTextNode("x");
  node_span.appendChild(span_text);

  node_dismiss_alert.appendChild(node_span);
  node_alert.appendChild(node_dismiss_alert);

  var strong_text = document.createTextNode(strong_t);

  var other_text = document.createTextNode(normal_t);

  node_strong_text.appendChild(strong_text);

  node_alert.appendChild(node_strong_text);
  node_alert.appendChild(other_text);

  document.getElementById("code-column").prepend(node_alert);
}

//resize block code
addEventListener('DOMContentLoaded', init);

/*
function registerToDatabase() {
            var jsonData = {
                "action": "REGISTER",
                "firstName": $("#firstName").val(),
                "lastName": $("#lastName").val(),
                "username": $("#username").val(),
                "password": $("#password").val(),
                "email": $("#email").val()
            };

            $.ajax({
                url: "data/applicationLayer.php",
                type: "POST",
                data: jsonData,
                dataType: "json",
                contentType: "application/x-www-form-urlencoded",
                success: function (jsonResponse) {
                    window.location.replace("index.php");
                },
                error: function (errorMessage) {
                    alert(errorMessage.responseText);
                }
            });
        }

        function loadCountries() {
        $.ajax({
            url: "data/countries.php",
            type: "GET",
            dataType: "json",
            contentType: "application/x-www-form-urlencoded",
            success: function (jsonResponse) {
                $("#country").append(jsonResponse);
            },
            error: function (errorMessage) {
                alert(errorMessage);
            }
        });
    }
*/