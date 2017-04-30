// counts number of alerts written
var alert_counter = 0;
var runtime_description = "Your program runtime is calculated in seconds. Time taken while waiting for input is not included in total runtime calculation.";
var quote_counter = 0;
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
                                1,
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


window.line_config =  {
        type: 'bar',
        data: {
            labels: ["Block1", "Block2"],
            datasets: [
            {
                label: "Compilation steps",
                backgroundColor: [
                    window.chartColors.red_alpha,
                    window.chartColors.orange_alpha,
                ],
                borderColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderWidth: 1,
                data: [10, 15],
            },
            {
                label: "Runtime steps",
                backgroundColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderWidth: 1,
                data: [20, 25],
            }
        ]
        },
        options: {
                responsive: true,
                legend:{
                    display: false,
                },
                scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: true
                    }]
                    }
                }
    };


window.line_config_vars =  {
        type: 'bar',
        data: {
            labels: ["Block1", "Block2"],
            datasets: [
            {
                label: "Number of variables",
                backgroundColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderWidth: 1,
                data: [20, 25],
            }
        ]
        },
        options: {
                responsive: true,
                legend:{
                    display: false,
                },
                scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: true
                    }]
                    }
                }
    };
    
window.doughnut_config = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [
                10,
                20,
            ],
            backgroundColor: [
                window.chartColors.red,
                window.chartColors.orange,
            ],
            label: 'Steps'
        }],
        labels: [
            "Block1",
            "Block2",
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

window.doughnut_config_runtime = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [
                10,
                20,
            ],
            backgroundColor: [
                window.chartColors.red,
                window.chartColors.orange,
            ],
            label: 'Steps'
        }],
        labels: [
            "Block1",
            "Block2",
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

window.doughnut_config_vars = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [
                10,
                20,
            ],
            backgroundColor: [
                window.chartColors.red,
                window.chartColors.orange,
            ],
            label: 'Variables'
        }],
        labels: [
            "Block1",
            "Block2",
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

$(document).ready(function(){ 
    $("#recompile").click(function(){
        $(".alert").alert("close");
        //clear output
        var a = document.getElementById('output-text');
        a.value = "";
        disable_input();
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
    
    $('#myLineChart_vars').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_line_chart_vars(0);
        }
    });

    $('#myDoughnutChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_doughnut_chart(0);
        }
    });

    $('#myDoughnutChart_runtime').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_doughnut_chart_runtime(0);
        }
    });

    $('#myDoughnutChart_vars').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_doughnut_chart_vars(0);
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

function random_patience_quote(){
    current_quote = quote_counter%7;

    quote_counter = quote_counter + 1;

    if (current_quote == 0) {
        return "Patience is a virtue.";
    }

    else if (current_quote == 1) {
        return "Love is patient. Love is kind.";
    }

    else if (current_quote == 2) {
        return "With love and patience, nothing is impossible.";
    }

    else if (current_quote == 3) {
        return  "Patience is bitter, but its fruit is sweet.";
    }

    else if (current_quote == 4) {
        return "He that can have patience can have what he will.";
    }

    else if (current_quote == 5){
        return "The greatest power is often simple patience.";
    }

    else {
        return "The two most powerful warriors are patience and time.";
    }
}

// html loads, print code on html, compile python
function load_code() {
    //desiable recompile button
    var but = document.getElementById('recompile');
    but.style.visibility = 'hidden';

    var but1 = document.getElementById('restart-button');
    but1.style.visibility = 'hidden';

    var t = setTimeout(function() {
                //show loading
                //get random patience quote
                patience_quote = random_patience_quote();
                create_bootstrap_info_alert("Choo Cho Train is hard at work. ", patience_quote);
            }, 300);

    //get code from python
    var getCodeURI = "http://127.0.0.1:5000/get_code";
    get_request_ajax_code(getCodeURI);
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
    a.value = "";
    a.value = text;
    //in case not in scroll view
    if(a.scrollHeight>0){
        a.style.height = a.scrollHeight+'px';
    }
    else {
        a.style.height = 72+'px';
    }
}

function runtime_end(){
    $(".alert").alert("close");
    //alert user, enable review button
    finished_running = true;
    //time interval to let user see alert appearing
    create_bootstrap_success_alert("Code finished running. ","You can now review your code");
}

function runtime_fail(message){
    $(".alert").alert("close");
    //alert user, enable review button
    finished_running = false;
    //time interval to let user see alert appearing
    create_bootstrap_danger_alert(message+ ". ","Try editing code or recompiling");
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
function get_request_ajax_code(uri){
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
                code_returned = jsonResponse.code
                show_code(code_returned);
                //start compiling
                var compilerURI = "http://127.0.0.1:5000/compile";
                get_request_ajax(compilerURI);
            },
            error: function (errorMessage) {
                alert(errorMessage);
            }
        });
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
                $(".alert").alert("close");

                code_returned = jsonResponse.result[0]
                //show_code(code_returned);
                //update time chart config info with runtime and compilation time
                update_time_config(jsonResponse.result[1],jsonResponse.result[2]);
                //update bar graph
                update_line_config(jsonResponse.result[5], jsonResponse.result[6], jsonResponse.result[7]);
                //update vars bar graph
                update_line_config_vars(jsonResponse.result[5], jsonResponse.result[8]);
                //wait for user to see runtime
                var t = setTimeout(function() {
                    $(".alert").alert("close");
                    show_output(jsonResponse.result[3])
                    //no error in compilation or runtime
                    if (jsonResponse.result[4] == 1){
                        runtime_end();
                    }
                    //error in compilation or runtime
                    else {
                        runtime_fail(jsonResponse.result[9]);
                    }

                    var but = document.getElementById('recompile');
                    but.style.visibility = 'visible';
                    var but1 = document.getElementById('restart-button');
                    but1.style.visibility = 'visible';
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
    if (compilation != 0) {
        b.textContent = runtime_description + " Total compilation time was only "+ compilation + " seconds, this time is included in the total runtime.";
    }

    else {
        b.textContent = runtime_description + " Total compilation time was extremely small to be able count it in seconds.";
    }

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

function generate_colors(amount_blocks){
    colors = [];

    for(var i = 0; i < amount_blocks; i++){
        var indexer = i%7;
        if(indexer == 0){
           colors[i]=window.chartColors.red; 
        }
        else if(indexer == 1){
           colors[i]=window.chartColors.orange; 
        }
        else if(indexer == 2){
           colors[i]=window.chartColors.yellow; 
        }
        else if(indexer == 3){
           colors[i]=window.chartColors.blue; 
        }
        else if(indexer == 4){
           colors[i]=window.chartColors.green; 
        }
        else if(indexer == 5){
           colors[i]=window.chartColors.purple; 
        }
        else{
           colors[i]=window.chartColors.grey; 
        }
    }
    return colors;
}

function generate_colors_alpha(amount_blocks){
    colors = [];

    for(var i = 0; i < amount_blocks; i++){
        var indexer = i%7;
        if(indexer == 0){
           colors[i]=window.chartColors.red_alpha; 
        }
        else if(indexer == 1){
           colors[i]=window.chartColors.orange_alpha; 
        }
        else if(indexer == 2){
           colors[i]=window.chartColors.yellow_alpha; 
        }
        else if(indexer == 3){
           colors[i]=window.chartColors.blue_alpha; 
        }
        else if(indexer == 4){
           colors[i]=window.chartColors.green_alpha; 
        }
        else if(indexer == 5){
           colors[i]=window.chartColors.purple_alpha; 
        }
        else{
           colors[i]=window.chartColors.grey_alpha; 
        }
    }
    return colors;
}

function update_line_config(blocks, compilation_steps, runtime_steps){
    amount_blocks = blocks.length;

    var runtime_colors = generate_colors(amount_blocks);
    var compilation_colors = generate_colors_alpha(amount_blocks);

    window.line_config =  {
        type: 'bar',
        data: {
            labels: blocks,
            datasets: [
            {
                label: "Compilation steps",
                backgroundColor: compilation_colors,
                borderColor: compilation_colors,
                borderWidth: 1,
                data: compilation_steps,
            },
            {
                label: "Runtime steps",
                backgroundColor: runtime_colors,
                borderColor: runtime_colors,
                borderWidth: 1,
                data: runtime_steps,
            }
        ]
        },
        options: {
                responsive: true,
                legend:{
                    display: false,
                },
                scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: true
                    }]
                    }
                }
    };

    update_doughnut_chart(blocks, compilation_steps, runtime_colors);
    update_doughnut_chart_runtime(blocks, runtime_steps, runtime_colors);
}

function update_line_config_vars(blocks, num_vars){
    amount_blocks = blocks.length;

    var colors = generate_colors(amount_blocks);

    window.line_config_vars =  {
        type: 'bar',
        data: {
            labels: blocks,
            datasets: [
            {
                label: "Number of variables",
                backgroundColor: colors,
                borderColor: colors,
                borderWidth: 1,
                data: num_vars,
            }
        ]
        },
        options: {
                responsive: true,
                legend:{
                    display: false,
                },
                scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: true
                    }]
                    }
                }
    };

    update_doughnut_chart_vars(blocks, num_vars, colors);
}


function update_doughnut_chart(blocks, compilation_steps, colors){
    window.doughnut_config = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: compilation_steps,
            backgroundColor: colors,
            label: 'Steps'
        }],
        labels: blocks
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
}

function update_doughnut_chart_vars(blocks, num_vars, colors){
    window.doughnut_config_vars = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: num_vars,
            backgroundColor: colors,
            label: 'Variables'
        }],
        labels: blocks
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
}

function update_doughnut_chart_runtime(blocks, runtime_steps, colors){
    window.doughnut_config_runtime = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: runtime_steps,
            backgroundColor: colors,
            label: 'Steps'
        }],
        labels: blocks
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

//custom alert
function create_bootstrap_info_alert(strong_t, normal_t){
  alert_counter = alert_counter + 1;

  var node_alert = document.createElement("DIV"); 
  var node_dismiss_alert = document.createElement("A");
  var node_strong_text = document.createElement("STRONG"); 
  var node_span = document.createElement("SPAN");
  var node_img = document.createElement("IMG");

  node_img.setAttribute("src","img/loading-sm.gif");
  node_img.setAttribute("alt","loading");
  node_img.setAttribute("width","12");
  node_img.setAttribute("height","12");
  
  //has two children: dismiss and text
  node_alert.setAttribute("class","alert alert-info alert-dismissable fade in");
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

  var other_text = document.createTextNode(normal_t + "  ");

  node_strong_text.appendChild(strong_text);

  node_alert.appendChild(node_strong_text);
  node_alert.appendChild(other_text);
  node_alert.appendChild(node_img);

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

function create_line_chart_vars(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("myLineChart_vars").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.myLineChart_vars = new Chart(ctx, line_config_vars);
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

function create_doughnut_chart_vars(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myDoughnutChart_vars").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myDoughnutChart_vars = new Chart(ctx, doughnut_config_vars);
    }, offset);
}

function create_doughnut_chart_runtime(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myDoughnutChart_runtime").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myDoughnutChart_runtime = new Chart(ctx, doughnut_config_runtime);
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
