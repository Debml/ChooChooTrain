// counts number of alerts written
var alert_counter = 0;
var runtime_description = "Your program runtime is calculated in seconds. Time taken while waiting for input is not included in total runtime calculation.";

var addedCount = 0;
var code = "Code not loaded";
var DEFAULT_DATASET_SIZE = 7;
var finished_running = false;
var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var view_code = -1;

var randomScalingFactor = function() {
        return Math.round(Math.random() * 100);
    };

chartColors = {
	red: 'rgb(255, 99, 132)',
    red_alpha: "rgba(255, 99, 132, 0.5)",
    red_alpha_high: "rgba(255, 99, 132, 0.7)",
	orange: 'rgb(255, 159, 64)',
    orange_alpha: "rgba(255, 159, 64,0.5)",
    orange_alpha_high: "rgba(255, 159, 64,0.7)",
	yellow: 'rgb(255, 205, 86)',
    yellow_alpha: "rgba(255, 205, 86,0.5)",
    yellow_alpha_high: "rgba(255, 205, 86,0.7)",
	green: 'rgb(75, 192, 192)',
    green_alpha: "rgba(75, 192, 192,0.5)",
    green_alpha_high: "rgba(75, 192, 192,0.7)",
	blue: 'rgb(54, 162, 235)',
    blue_alpha:"rgba(54, 162, 235,0.5)",
    blue_alpha_high:"rgba(54, 162, 235,0.7)",
	purple: 'rgb(153, 102, 255)',
    purple_alpha: "rgba(153, 102, 255,0.5)",
    purple_alpha_high: "rgba(153, 102, 255,0.7)",
	grey: 'rgb(231,233,237)',
    grey_alpha: "rgba(231,233,237,0.5)",
    grey_alpha_high: "rgba(231,233,237,0.7)",
};

//config for time chart
window.time_config = { type: 'doughnut',
                    data: {
                        datasets: [{
                            data: [
                                32,
                            ],
                            backgroundColor: [
                                chartColors.red,
                            ],
                        }],
                        labels: [
                            "Total Runtime",
                        ]
                    },
                    options: {
                        responsive: true,
                        legend:{
                        display: false
                        },
                        layout: {
                        padding: 23
                        },
                        
                        animation: {
                            animateScale: true,
                            animateRotate: true
                        }
                    }
                };

var line_config =  {
        type: 'line',
        data: {
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
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                    }
                }
    };

var bubbleChartData = {
    animation: {
        duration: 10000
    },
    datasets: [{
        label: "Block1",
        backgroundColor: window.chartColors.red_alpha,
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
        backgroundColor: window.chartColors.blue_alpha,
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
        backgroundColor: window.chartColors.green_alpha,
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

var bubble_config = { type: 'bubble',
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
                };
var polar_config = {
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
                    window.chartColors.red_alpha_high,
                    window.chartColors.orange_alpha_high,
                    window.chartColors.yellow_alpha_high,
                    window.chartColors.green_alpha_high,
                    window.chartColors.blue_alpha_high,
                    window.chartColors.red_alpha_high,
                    window.chartColors.orange_alpha_high,
                    window.chartColors.yellow_alpha_high,
                    window.chartColors.green_alpha_high,
                    window.chartColors.blue_alpha_high
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

var stacked_config = {
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

var doughnut_config = {
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
};

$(document).ready(function(){ 
    $("#recompile").click(function(){
        $(".alert").alert("close");
        load_code();
    }); 

    $('#timeChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_time_chart(0);
        }
    });

    $('#myLineChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_line_chart(0);
        }
    });
    $('#myDoughnutChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_doughnut_chart(0);
        }
    });

    $('#myStackedChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_stacked_chart(0);
        }
    });

    $('#myPolarChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_polar_chart(0);
        }
    });

    $('#myBubbleChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_bubble_chart(0);
        }
    });

    $('#pills-tab a').hover(function (e) {
          e.preventDefault()
          if(finished_running){
            $(this).tab('show')
          }
       });

    $('#review-tab').tooltip({trigger: 'manual'});

    $('#review-tab').mouseover(function() {
        var tt = $(this);
        if (!finished_running){
            tt.tooltip("show");
        }
    }).mouseout(function() {
        var tt = $(this);
        tt.tooltip( 'hide' );
    });
  
});

function restart(){
    window.location.href = "index.html";
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
    var a = document.getElementById('recompile');
    a.disabled = true;
    //get code from python
    var compilerURI = "http://127.0.0.1:5000/compile";
    get_request_ajax(compilerURI);
}

function send_input(){
    //compiler receives input
    disable_input();
    show_output(text);
    //runtime_end();
}

function show_output(text){
    //compiler sent output
    var a = document.getElementById('output-text');
    a.focus();
    a.value = text;
}

function runtime_end(){
    //alert user, enable review button
    finished_running = true;
    //time interval to let user see alert appearing
    create_bootstrap_success_alert("Code finished running. ","You can now review your code");
}

function runtime_fail(){
    //alert user, enable review button
    finished_running = false;
    //time interval to let user see alert appearing
    create_bootstrap_danger_alert("Code compilation/runtime error. ","Check output section for error detail");
}

/*function create_review_button(){
    var node_p = document.createElement("P"); 
    var node_button = document.createElement("BUTTON");

    node_button.setAttribute("class","btn btn-success btn-lg btn-block");
    node_button.setAttribute("id","review_button");
    node_button.setAttribute("href","#");
    node_button.setAttribute("role","button");
    node_button.setAttribute("onclick","review_code()");

    var text = document.createTextNode("Review");
    node_button.appendChild(text);

    node_p.appendChild(node_button);

    document.getElementById("code-column").prepend(node_p);
}*/

function enable_input(){
    var a = document.getElementById('input-text');
    var b = document.getElementById('send-input-button');

    a.disabled = false;
    b.disabled = false;
}

function disable_input(){
    var a = document.getElementById('input-text');
    var b = document.getElementById('send-input-button');

    a.value = "";

    a.disabled = true;
    b.disabled = true;
}

// code shown
function show_code(code_returned) {
    var a = document.getElementById("code-running");
    a.textContent = code_returned;

    //after code shown, compile
    compile_code();
}

function compile_code(){
    //compiler needs input
    //enable_input();
}

function get_request_ajax(uri){
    $.ajax({
            url: uri,
            type: "GET",
            contentType: "application/json",
            success: function (jsonResponse) {
                //code retreived, call method to append to html
                //index 0 - code
                //index 1 runtime
                //index 2 compilation time
                //index 3 output
                //index 4 compilation status
                code_returned = jsonResponse.result[0]
                show_code(code_returned);
                //update time chart config info with runtime and compilation time
                update_time_config(jsonResponse.result[1],jsonResponse.result[2]);
                //wait for user to see runtime
                var t = setTimeout(function() {
                    show_output(jsonResponse.result[3])
                    //no error in compilation or runtime
                    if (jsonResponse.result[4] == 1){
                        runtime_end();
                    }
                    //error in compilation or runtime
                    else {
                        runtime_fail();
                    }
                }, 700);
            },
            error: function (errorMessage) {
                alert(errorMessage);
            }
        });
}

function update_time_config(runtime, compilation){
    var a = document.getElementById("label-seconds");
    a.textContent = runtime + " seconds";

    var b = document.getElementById("runtime-info");
    b.textContent = runtime_description + " Total compilation time was only "+ compilation + " seconds, this time is included in the total runtime.";

    window.time_config = { type: 'doughnut',
                    data: {
                        datasets: [{
                            data: [
                                runtime,
                            ],
                            backgroundColor: [
                                chartColors.red,
                            ],
                        }],
                        labels: [
                            "Total Runtime",
                        ]
                    },
                    options: {
                        responsive: true,
                        legend:{
                        display: false
                        },
                        layout: {
                        padding: 23
                        },
                        
                        animation: {
                            animateScale: true,
                            animateRotate: true
                        }
                    }
                };
}

//custom alert
function create_bootstrap_success_alert(strong_t, normal_t){
  alert_counter = alert_counter + 1;

  var node_alert = document.createElement("DIV"); 
  var node_dismiss_alert = document.createElement("A");
  var node_strong_text = document.createElement("STRONG"); 
  var node_span = document.createElement("SPAN");
  
  //has two children: dismiss and text
  node_alert.setAttribute("class","alert alert-success alert-dismissable fade in");
  node_alert.setAttribute("style","margin-bottom:10px");
  node_alert.setAttribute("id","alert" + alert_counter);

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

  document.getElementById("code-container").prepend(node_alert);
}

//custom danger alert
function create_bootstrap_danger_alert(strong_t, normal_t){
  alert_counter = alert_counter + 1;

  var node_alert = document.createElement("DIV"); 
  var node_dismiss_alert = document.createElement("A");
  var node_strong_text = document.createElement("STRONG"); 
  var node_span = document.createElement("SPAN");
  
  //has two children: dismiss and text
  node_alert.setAttribute("class","alert alert-danger alert-dismissable fade in");
  node_alert.setAttribute("style","margin-bottom:10px");
  node_alert.setAttribute("id","alert" + alert_counter);

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

  document.getElementById("code-container").prepend(node_alert);
}


function create_time_chart(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("timeChart").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.timeChart = new Chart(ctx, window.time_config);
    }, offset);
}

function create_line_chart(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("myLineChart").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.myLineChart = new Chart(ctx, line_config);
    }, offset);
}

function create_bubble_chart(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myBubbleChart").getContext("2d");
        window.myBubbleChart = new Chart(ctx, bubble_config);   
    }, offset);
}

function create_polar_chart(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myPolarChart");
        window.myPolarChart = Chart.PolarArea(ctx, polar_config); 
    }, offset);
}

function create_doughnut_chart(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myDoughnutChart").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myDoughnutChart = new Chart(ctx, doughnut_config);
    }, offset);
}

function create_stacked_chart(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myStackedChart").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myStackedChart = new Chart(ctx, stacked_config);
    }, offset);
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