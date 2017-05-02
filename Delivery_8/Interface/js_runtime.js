// counts number of alerts written
var alert_counter = 0;
var runtime_description = "Your program runtime is calculated in seconds. Time taken while waiting for input is not included in total runtime calculation.";
var memory_use_ar = "Some blocks can take up a lot of memory if they are called numerous times within each other or recursively. If there are many calls within blocks before finishing execution, memory usage can stack up. See how well your code performs with increasing amount of block calls.";
var memory_use_no_ar = "There were no calls to other blocks except the starting block. Choo Choo Train makes a hidden block call to the starting block in order to start execution of the program.";
var vars_description = "Each block has a total amount of variables including simple data types, parameters, and lists. Some blocks contain more variables than we expect, these variables take up memory space and can sometimes saturate the available memory.";
var no_vars_description = "There are no variables declared in your code. Try including variable declarations in order to store values and constants.";
var total_vars_description = "Each block has its own weight on the program's memory. Comparing how many variables each block has compared to others can help visualize just how much memory space each block is taking.";
var branch_description = "Branches are sections of code where a conditional statement is used and the program must choose what to execute according to the evaluated condition.These branches define the direction the program execution takes,just as train tracks branch out and direct trains.";
var no_branch_description = "There are no branches used in your code. Write some conditional statements in your code to see how this makes your program behaves.";
var no_loop_description = "There are no loops used in your code. Write some loop statements (do - until) in your code to see how this makes your program behaves.";;
var no_elements_description = "There are no elements in your entire code. Try writing variables, conditional statements, or loop statements to see how this makes your program behaves.";
var elements_description = "Total elements in a block include variables, loops, and branches. These are some of the elements Choo Choo Train provides.";
var cycles_description = "Loop statements allow us to execute a statement or group of statements multiple times. Check how many times the statement inside the loop is executed for each loop. Loops are sequentially numbered for each block.";
var loop_description = "Choo Choo Train provides a simple loop statement, called a do until loop. These are defined inside block code and can execute a statement multiple times. Check how many loops each block has.";
var summary_description = "Total elements of program.";
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
    red_alpha_low: "rgba(255, 99, 132, 0.2)",
    red_alpha_high: "rgba(255, 99, 132, 0.7)",
	orange: 'rgb(255, 159, 64)',
    orange_alpha: "rgba(255, 159, 64,0.5)",
    orange_alpha_low: "rgba(255, 159, 64,0.2)",
    orange_alpha_high: "rgba(255, 159, 64,0.7)",
	yellow: 'rgb(255, 205, 86)',
    yellow_alpha: "rgba(255, 205, 86,0.5)",
    yellow_alpha_low: "rgba(255, 205, 86,0.2)",
    yellow_alpha_high: "rgba(255, 205, 86,0.7)",
	green: 'rgb(75, 192, 192)',
    green_alpha: "rgba(75, 192, 192,0.5)",
    green_alpha_low: "rgba(75, 192, 192,0.2)",
    green_alpha_high: "rgba(75, 192, 192,0.7)",
	blue: 'rgb(54, 162, 235)',
    blue_alpha:"rgba(54, 162, 235,0.5)",
    blue_alpha_low:"rgba(54, 162, 235,0.2)",
    blue_alpha_high:"rgba(54, 162, 235,0.7)",
	purple: 'rgb(153, 102, 255)',
    purple_alpha: "rgba(153, 102, 255,0.5)",
    purple_alpha_low: "rgba(153, 102, 255,0.2)",
    purple_alpha_high: "rgba(153, 102, 255,0.7)",
	grey: 'rgb(231,233,237)',
    grey_alpha: "rgba(231,233,237,0.5)",
    grey_alpha_low: "rgba(231,233,237,0.2)",
    grey_alpha_high: "rgba(231,233,237,0.7)",
    transparent: "rgba(231,233,237,0.0)"
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

window.system_chart_config = {
    type: 'line',
    data: {
        labels: ["0", "1", "2", "3", "4", "5", "6","7","8","9","10", "11", "12", "13","14", "15", "15", "17",],
        datasets: [ {
        label: "System Usage",
        borderColor: window.chartColors.purple,
        backgroundColor: window.chartColors.purple_alpha,
        data: [
                        10, 
                        66, 
                        122, 
                        100, 
                        11, 
                        11, 
                        39,
                        8,
                        12,
                        2,1,3,4,5,5,3,5,4
                    ],
        }]
    },
    options: {
        responsive: true,
        title:{
        display: false,
        text:"System Usage Stacked Area"
        },
        legend: {
            display: false,
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
                afterTickToLabelConversion: function(data){
                    var xLabels = data.ticks;

                    xLabels.forEach(function (labels, i, xLabels) {
                        var size_data = xLabels.length;
                        var fixed = Math.floor(size_data/5);

                        if (i % fixed != 0){
                            xLabels[i] = '';
                        }
                    });
                } 
            }],
            yAxes: [{
                stacked: true,
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
            label: 'Operations'
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
    type: 'pie',
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
            label: 'Operations'
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
    type: 'pie',
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

window.doughnut_config_ifs = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [
                1,
                2,
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


window.doughnut_config_loops = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: [
                1,
                2,
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

window.polar_config = {
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

window.bar_elements_config =  {
        type: 'bar',
        data: {
            labels: ["Block1", "Block2"],
            datasets: [
            {
                label: "Variables",
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
                label: "Branches",
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
            },
            {
                label: "Loops",
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

window.polar_calls_config = {
    type: 'pie',
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

window.line_runs_config = {
    type: 'line',
    data: {
        labels: ["0", "1", "2", "3", "4", "5", "6","7","8","9","10", "11", "12", "13","14", "15", "15", "17",],
        datasets: [ {
        label: "System Usage",
        borderColor: window.chartColors.purple,
        backgroundColor: window.chartColors.purple_alpha,
        data: [
                        10, 
                        66, 
                        122, 
                        100, 
                        11, 
                        11, 
                        39,
                        8,
                        12,
                        2,1,3,4,5,5,3,5,4
                    ],
        }]
    },
    options: {
        responsive: true,
        title:{
        display: false,
        text:"Runtime per block Stacked Area"
        },
        legend: {
            display: false,
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
            yAxes: [{
                stacked: true,
            }]
        }
    }
};

window.bar_summary_config =  {
        type: 'horizontalBar',
        data: {
            labels: ["Summary"],
            datasets: [
            {
                label: "Variables",
                backgroundColor: [
                    window.chartColors.red_alpha,
                    window.chartColors.orange_alpha,
                ],
                borderColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderWidth: 1,
                data: [10],
            },
            {
                label: "Branches",
                backgroundColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderWidth: 1,
                data: [20],
            },
            {
                label: "Loops",
                backgroundColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderColor: [
                    window.chartColors.red,
                    window.chartColors.orange,
                ],
                borderWidth: 1,
                data: [22],
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

$(document).ready(function(){ 
    $('[data-toggle="popover"]').popover();  

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

    $('#mySystemChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_system_chart(0);
        }
    });

    $('#myBarChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_bar_elements_chart(0);
        }
    });

    $('#mySummary').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_bar_summary(0);
        }
    });

    $('#myCallsChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_polar_calls_chart(0);
        }
    });

    $('#myRuntimeChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_line_runs_chart(0);
        }
    });
    
    $('#myLineChart_vars').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_line_chart_vars(0);
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

    $('#myDoughnutChart_ifs').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_doughnut_chart_ifs(0);
        }
    });

    $('#myDoughnutChart_loops').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_doughnut_chart_loops(0);
        }
    });

    $('#myPolarChart').viewportChecker({
        offset: 200,                 
        callbackFunction: function(elem){
           create_polar_chart(0);
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
    //get input value
    var a = document.getElementById('input-text');
    var user_input = a.value;

    //build json from code
    var data_js = JSON.stringify({"user_input":user_input});

    //post input to API
    var postUserInputURI = "http://127.0.0.1:5000/post_input";
    post_request_ajax_input(postUserInputURI, data_js);
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

function show_output_input(text){
    //compiler sent output
    var a = document.getElementById('output-text');
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

function ask_input(message){
    
    $(".alert").alert("close");
    //alert user, enable review button
    finished_running = false;
    //time interval to let user see alert appearing
    create_bootstrap_input_alert(message+ ". ","Click send after writing input");
    enable_input();
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
    a.focus();
}

function disable_input(){
    $(".alert").alert("close");
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

//ajax post request
function post_request_ajax_input(uri,data_js){
  $.ajax({
            url: uri,
            type: "POST",
            data: data_js,
            dataType: "json",
            contentType: "application/json",
            success: function (jsonResponse) {
                response_post_ajax(jsonResponse);
            },
            error: function (errorMessage) {
                //alert user
                create_bootstrap_alert("ERROR",": Not connected to compiler");
            }
            
        });
}

//ajax response callback
function response_post_ajax(jsonResponse){
    result_code = jsonResponse.result;
    if(result_code == 1) {
        //input was posted
        disable_input();
    }
    else {
        //bootstrap alert
        create_bootstrap_alert("ERROR " + result_code,": User input not sent");
    }
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
                //index 5 is block names
                //index 6 is compilation steps
                //index 7 is runtime steps
                //index 8 is number of vars
                //index 9 is last output generated
                //index 10 is number of activation records
                //index 11 is the record for the ar's
                //index 12 is for number of ifs
                $(".alert").alert("close");

                code_returned = jsonResponse.result[0]
                //show_code(code_returned);
                //update time chart config info with runtime and compilation time
                update_time_config(jsonResponse.result[1],jsonResponse.result[2]);
                //update bar graph
                update_line_config(jsonResponse.result[5], jsonResponse.result[6], jsonResponse.result[7]);
                //update vars bar graph
                update_line_config_vars(jsonResponse.result[5], jsonResponse.result[8]);
                //update activation records line graph
                update_system_chart_config(jsonResponse.result[10], jsonResponse.result[11]);
                //update num ifs
                update_doughnut_chart_ifs(jsonResponse.result[5], jsonResponse.result[12]);
                //update num loops
                update_doughnut_chart_loops(jsonResponse.result[5], jsonResponse.result[13]);
                //update cycles
                update_polar_chart(jsonResponse.result[14], jsonResponse.result[15]);
                //update elements
                update_bar_elements_chart(jsonResponse.result[5], jsonResponse.result[8],jsonResponse.result[12],jsonResponse.result[13]);
                //update calls to blocks
                update_polar_calls_chart(jsonResponse.result[5], jsonResponse.result[19]);
                //update calls to blocks
                update_line_runs_config(jsonResponse.result[5], jsonResponse.result[20]);
                //update summary
                update_bar_summary(jsonResponse.result[8], jsonResponse.result[13], jsonResponse.result[12]);
                //wait for user to see runtime
                var t = setTimeout(function() {
                    $(".alert").alert("close");
                    //no error in compilation or runtime
                    if (jsonResponse.result[4] == 1){
                        runtime_end();
                        show_output(jsonResponse.result[3])
                    }
                    //error in compilation or runtime, or input
                    else {
                        //asks for input
                        if(jsonResponse.result[4] == 3){
                            ask_input("User input needed to continue running");
                            //show all previous output
                            show_output_input(jsonResponse.result[3])
                        }
                        //compilation error
                        else if(jsonResponse.result[4] == 2){
                            runtime_fail(jsonResponse.result[9]);
                            show_output(jsonResponse.result[9])
                        }
                        //runtime error
                        else {
                            runtime_fail(jsonResponse.result[9]);
                            show_output(jsonResponse.result[3])
                        }
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

function generate_colors_alpha_low(amount_blocks){
    colors = [];

    for(var i = 0; i < amount_blocks; i++){
        var indexer = i%7;
        if(indexer == 0){
           colors[i]=window.chartColors.red_alpha_low; 
        }
        else if(indexer == 1){
           colors[i]=window.chartColors.orange_alpha_low; 
        }
        else if(indexer == 2){
           colors[i]=window.chartColors.yellow_alpha_low; 
        }
        else if(indexer == 3){
           colors[i]=window.chartColors.blue_alpha_low; 
        }
        else if(indexer == 4){
           colors[i]=window.chartColors.green_alpha_low; 
        }
        else if(indexer == 5){
           colors[i]=window.chartColors.purple_alpha_low; 
        }
        else{
           colors[i]=window.chartColors.grey_alpha_low; 
        }
    }
    return colors;
}

function generate_colors_transparent(amount_blocks){
    colors = [];

    for(var i = 0; i < amount_blocks; i++){
        colors[i]=window.chartColors.transparent; 
    }
    return colors;
}

function generate_colors_alpha_high(amount_blocks){
    colors = [];

    for(var i = 0; i < amount_blocks; i++){
        var indexer = i%7;
        if(indexer == 0){
           colors[i]=window.chartColors.red_alpha_high; 
        }
        else if(indexer == 1){
           colors[i]=window.chartColors.orange_alpha_high; 
        }
        else if(indexer == 2){
           colors[i]=window.chartColors.yellow_alpha_high; 
        }
        else if(indexer == 3){
           colors[i]=window.chartColors.blue_alpha_high; 
        }
        else if(indexer == 4){
           colors[i]=window.chartColors.green_alpha_high; 
        }
        else if(indexer == 5){
           colors[i]=window.chartColors.purple_alpha_high; 
        }
        else{
           colors[i]=window.chartColors.grey_alpha_high; 
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
                label: "Operations",
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

    //update_doughnut_chart(blocks, compilation_steps, runtime_colors);
    update_doughnut_chart_runtime(blocks, runtime_steps, runtime_colors);
}

function generate_label_system(size){
    labels = [];
    for (var i=1; i<=size;i++){
        labels[i-1] = i.toString();
    }
    return labels;
}

function update_system_chart_config(num_ar, num_ar_records){
    //main
    var aux = ["0.2"];
    var records = aux.concat(num_ar_records);
    var show_points, borderColor, label_data, fixed;
    max_ar = (num_ar/500*100)+0.2;
    fixed = Math.floor(num_ar_records.length/6);

    if(num_ar == 1){
        max_ar = 1;
        label_data = ["0","1"];
        records = [0.2,0.2];
        var a = document.getElementById("memory-use-description");
        a.textContent = memory_use_no_ar;
    }

    else {
        var aux_label = ["0"];
        var label_data = aux_label;
        label_data = aux_label.concat(generate_label_system(num_ar_records.length));
        var a = document.getElementById("memory-use-description");
        a.textContent = memory_use_ar;
    }

    if(num_ar_records.length > 40){
        show_points = 0;
        borderColor = window.chartColors.transparent;
    }

    else {
        show_points = 3;
        borderColor = window.chartColors.purple;
    }

    window.system_chart_config =  {
        type: 'line',
    data: {
        labels: label_data,
        datasets: [ {
        label: "System Usage",
        borderColor: borderColor,
        backgroundColor: window.chartColors.purple_alpha,
        data: records,
        pointBorderColor: window.chartColors.purple,
        pointBackgroundColor: window.chartColors.purple,
        }
    ]
    },
    options: {
        elements: {
                    point:{
                        radius: show_points
                    },
                    line:{
                        borderWidth: 2
                    }
        },
        responsive: true,
        title:{
        display: false,
        text:"System Usage Stacked Area"
        },
        legend: {
            display: false,
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
                autoSkip: true,
                ticks: {
                    maxTicksLimit: 15,
                    suggestedMax: num_ar_records.length,
                    min: 0,
                    stepSize: fixed
                }
            }],
            yAxes: [{
                afterTickToLabelConversion: function(data){
                    var ylabels = data.ticks;

                    ylabels.forEach(function (labels, i, ylabels) {
                        ylabels[i] = ylabels[i]+'%';
                    });
                },
                ticks: {
                        suggestedMax: max_ar
                       },
                stacked: true,
            }]
        }
    }
};
}

function are_all_zero(array){
    var flag = true;

    for(var i=0;i < array.length; i++){
        if(array[i]!= 0){
            flag = false;
        }
    }

    return flag;
}

function update_line_config_vars(blocks, num_vars){
    if(are_all_zero(num_vars)){
        var a = document.getElementById("vars-description");
        a.textContent = no_vars_description;
    }
    else {
        var b = document.getElementById("vars-description");
        b.textContent = vars_description;
    }

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
                        stacked: true,
                        ticks: {
                            beginAtZero:true
                        }
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
            label: 'Operations'
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
    var visible_legend;

    if(are_all_zero(num_vars)){
        var a = document.getElementById("total-vars-description");
        a.textContent = no_vars_description;
        visible_legend = false;
    }
    else {
        var b = document.getElementById("total-vars-description");
        b.textContent = total_vars_description;
        visible_legend = true;
    }

    window.doughnut_config_vars = {
    type: 'pie',
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
            display: visible_legend,
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

function update_doughnut_chart_ifs(blocks, num_ifs){
    var visible_legend;
    amount_blocks = blocks.length;
    var colors = generate_colors(amount_blocks);

    if(are_all_zero(num_ifs)){
        var a = document.getElementById("branch-description");
        a.textContent = no_branch_description;
        visible_legend = false;
    }
    else {
        var b = document.getElementById("branch-description");
        b.textContent = branch_description;
        visible_legend = true;
    }

    window.doughnut_config_ifs = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: num_ifs,
            backgroundColor: colors,
            label: 'Variables'
        }],
        labels: blocks
    },
    options: {
        responsive: true,
        legend: {
            display: visible_legend,
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

function update_polar_chart(blocks_loops, num_cycles){
    amount_blocks = blocks_loops.length;
    var colors = generate_colors_alpha_high(amount_blocks);
    var borders = generate_colors_alpha_low(amount_blocks);

    if(are_all_zero(num_cycles)){
        var a = document.getElementById("cycles-description");
        a.textContent = no_loop_description;
    }
    else {
        var b = document.getElementById("cycles-description");
        b.textContent = cycles_description;
    }

    window.polar_config = {
        data: {
            datasets: [{
                data: num_cycles,
                backgroundColor: colors,
                borderColor: borders,
                borderWidth: 1
            }],
            labels: blocks_loops
        },
        options: {
            layout: {
                padding: 20
            },
            responsive: true,
            title:{
            display: true,
            padding: 15,
            position: "bottom",
            text:"Hover over areas to see details",
            fontSize:10,
            fontStyle: "normal"
            },
            legend: {
                position: 'right',
                display:false,
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
}

function update_doughnut_chart_loops(blocks, num_loops){
    var visible_legend;
    amount_blocks = blocks.length;
    var colors = generate_colors(amount_blocks);

    if(are_all_zero(num_loops)){
        var a = document.getElementById("loop-description");
        a.textContent = no_loop_description;
        visible_legend = false;
    }
    else {
        var b = document.getElementById("loop-description");
        b.textContent = loop_description;
        visible_legend = true;
    }
    
    window.doughnut_config_loops = {
    type: 'doughnut',
    data: {
        datasets: [{
            data: num_loops,
            backgroundColor: colors,
            label: 'Variables'
        }],
        labels: blocks
    },
    options: {
        responsive: true,
        legend: {
            display: visible_legend,
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
    type: 'pie',
    data: {
        datasets: [{
            data: runtime_steps,
            backgroundColor: colors,
            label: 'Operations'
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

function update_bar_elements_chart(blocks, num_vars, num_ifs, num_loops){
    if(are_all_zero(num_vars) && are_all_zero(num_ifs) && are_all_zero(num_loops)){
        var a = document.getElementById("elements-description");
        a.textContent = no_elements_description;
    }
    else {
        var b = document.getElementById("elements-description");
        b.textContent = elements_description;
    }
    
    amount_blocks = blocks.length;
    var colors = generate_colors(amount_blocks);
    var colors_alpha_low = generate_colors_alpha_low(amount_blocks);
    var colors_alpha_high = generate_colors_alpha_high(amount_blocks);

    window.bar_elements_config =  {
        type: 'bar',
        data: {
            labels: blocks,
            datasets: [
            {
                label: "Variables",
                backgroundColor: colors,
                borderColor: colors,
                borderWidth: 1,
                data: num_vars,
            },
            {
                label: "Branches",
                backgroundColor: colors_alpha_high,
                borderColor: colors,
                borderWidth: 1,
                data: num_ifs,
            },
            {
                label: "Loops",
                backgroundColor: colors_alpha_low,
                borderColor: colors,
                borderWidth: 1,
                data: num_loops,
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
                        stacked: true,
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                    }
                }
    };

}

function update_polar_calls_chart(blocks, num_calls){
     amount_blocks = blocks.length;
    var colors = generate_colors(amount_blocks);

    window.polar_calls_config = {
    type: 'pie',
    data: {
        datasets: [{
            data: num_calls,
            backgroundColor: colors,
            label: 'Calls to Block'
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

function accumulate_runtimes(runtimes){
    var counter = 0;
    var accums = [];

    for(var i = 0; i < runtimes.length; i++){
        counter = counter + runtimes[i];
        accums[i]= counter;
    }
    return accums;
}

function calc(array){
    var newarray = [];
    var counter = 0;

    for(var i=0;i < array.length;i++){
        counter = counter + array[i];
    }

    newarray[0] = counter;

    return newarray;
}

function update_bar_summary(num_vars,num_loops, num_ifs){
    var legend_show;
    if(are_all_zero(num_vars) && are_all_zero(num_ifs) && are_all_zero(num_loops)){
        var a = document.getElementById("summary-description");
        a.textContent = no_elements_description;
        legend_show = false;
    }
    else {
        var b = document.getElementById("summary-description");
        b.textContent = summary_description;
        legend_show = true;
    }
    
    var nvars = calc(num_vars);
    var nloops = calc(num_loops);
    var nifs = calc(num_ifs);

    window.bar_summary_config =  {
        type: 'bar',
        data: {
            labels: ["Summary"],
            datasets: [
            {
                label: "Variables",
                backgroundColor: [
                    window.chartColors.red,
                ],
                borderColor: [
                    window.chartColors.red,
                ],
                borderWidth: 1,
                data: nvars,
            },
            {
                label: "Branches",
                backgroundColor: [
                    window.chartColors.green,
                ],
                borderColor: [
                    window.chartColors.green,
                ],
                borderWidth: 1,
                data: nifs,
            },
            {
                label: "Loops",
                backgroundColor: [
                    window.chartColors.yellow,
                ],
                borderColor: [
                    window.chartColors.yellow,
                ],
                borderWidth: 1,
                data: nloops,
            }
        ]
        },
        options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each horizontal bar to be 2px wide
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                        }
                    },
                    responsive: true,
                    legend: {
                        display:legend_show,
                        fontSize:10,
                        position: 'right',
                    },
                    title: {
                        display: false,
                        text: 'Chart.js Horizontal Bar Chart'
                    },

                    scales: {
                    xAxes: [{
                        stacked: true
                    }],
                    yAxes: [{
                        stacked: true,
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                    }
                    
                }
    };
}

function update_line_runs_config (blocks, runtimes){
    var newlabels, newruntimes;

    if(runtimes.length == 1){
        newlabels = ["Start Execution",blocks[0]];
        newruntimes = [0,runtimes[0]];
    }

    else {
        newlabels = blocks;
        newruntimes = runtimes;
    }

    var max = Math.max(runtimes);
    //accumulate runtimes
    accum = accumulate_runtimes(newruntimes);

    window.line_runs_config =  {
        type: 'line',
    data: {
        labels: newlabels,
        datasets: [ 
        {
        pointRadius: 8,
        pointHoverRadius:10,
        pointHitRadius:10,
        showLine: false,
        label: "Runtime per Block",
        borderColor: window.chartColors.red,
        backgroundColor: window.chartColors.red_alpha,
        data: newruntimes,
        pointBorderColor: window.chartColors.red,
        pointBackgroundColor: window.chartColors.red,
        },
        {
        fill: true,
        label: "Accumulated Runtime",
        borderColor: window.chartColors.yellow,
        backgroundColor: window.chartColors.yellow_alpha,
        data: accum,
        pointBorderColor: window.chartColors.yellow,
        pointBackgroundColor: window.chartColors.yellow,
        },
    ]
    },
    options: {
        elements: {
                    point:{
                        radius: 3
                    },
                    line:{
                        borderWidth: 2
                    }
        },
        responsive: true,
        title:{
        display: false,
        text:"Runtimes"
        },
        legend: {
            display: false,
            position: 'right',
            fullWidth: false,
            labels: {
                boxWidth: 15
            }
        },
        tooltips: {
                callbacks: {
                    label: function (tooltipItems, data) {
                        return tooltipItems.yLabel.toFixed(8)
                    }
                },
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Month'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Value'
                }
            }]
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
function create_bootstrap_alert(strong_t, normal_t){
  var node_alert = document.createElement("DIV"); 
  var node_dismiss_alert = document.createElement("A");
  var node_strong_text = document.createElement("STRONG"); 
  var node_span = document.createElement("SPAN");
  
  //has two children: dismiss and text
  node_alert.setAttribute("class","alert alert-danger alert-dismissable fade in");

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

//input alert
function create_bootstrap_input_alert(strong_t, normal_t){
  alert_counter = alert_counter + 1;

  var node_alert = document.createElement("DIV"); 
  var node_dismiss_alert = document.createElement("A");
  var node_strong_text = document.createElement("STRONG"); 
  var node_span = document.createElement("SPAN");
  
  //has two children: dismiss and text
  node_alert.setAttribute("class","alert alert-warning alert-dismissable fade in");
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
            window.myLineChart = new Chart(ctx, window.line_config);
    }, offset);
}

function create_system_chart(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("mySystemChart").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.mySystemChart = new Chart(ctx, window.system_chart_config);
    }, offset);
}

function create_bar_elements_chart(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("myBarChart").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.myBarChart = new Chart(ctx, window.bar_elements_config);
    }, offset);
}

function create_bar_summary(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("mySummary").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.mySummary = new Chart(ctx, window.bar_summary_config);
    }, offset);
}

function create_polar_calls_chart(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("myCallsChart").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.myCallsChart = new Chart(ctx, window.polar_calls_config);
    }, offset);
}

function create_line_runs_chart(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("myRuntimeChart").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.myRuntimeChart = new Chart(ctx, window.line_runs_config);
    }, offset);
}

function create_line_chart_vars(offset){
    var t = setTimeout(function() {
            var ctx = document.getElementById("myLineChart_vars").getContext("2d");
            ctx.canvas.width = 20;
            ctx.canvas.height = 20;
            window.myLineChart_vars = new Chart(ctx, window.line_config_vars);
    }, offset);
}

function create_polar_chart(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myPolarChart");
        window.myPolarChart = Chart.PolarArea(ctx, window.polar_config); 
    }, offset);
}

function create_doughnut_chart_vars(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myDoughnutChart_vars").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myDoughnutChart_vars = new Chart(ctx, window.doughnut_config_vars);
    }, offset);
}

function create_doughnut_chart_ifs(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myDoughnutChart_ifs").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myDoughnutChart_ifs = new Chart(ctx, window.doughnut_config_ifs);
    }, offset);
}

function create_doughnut_chart_runtime(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myDoughnutChart_runtime").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myDoughnutChart_runtime = new Chart(ctx, window.doughnut_config_runtime);
    }, offset);
}

function create_doughnut_chart_loops(offset){
    var t = setTimeout(function() {   
        var ctx = document.getElementById("myDoughnutChart_loops").getContext("2d");
        ctx.canvas.width = 20;
        ctx.canvas.height = 20;
        window.myDoughnutChart_loops = new Chart(ctx, window.doughnut_config_loops);
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
