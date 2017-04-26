// counts number of blocks written
var block_counter = 0;
var code = "Code not loaded";

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
    var compilerURI = "http://127.0.0.1:5000/compile";
    get_request_ajax(compilerURI);
}

function send_input(){
    //compiler receives input
    disable_input();
    show_output();
    runtime_end();
}

function show_output(){
    //compiler sent output
    var a = document.getElementById('output-text');
    a.value = "Output shown";
}

function runtime_end(){
    //alert user, enable review button
    create_review_button();
    create_bootstrap_success_alert("Code finished running. ","You can now review your code")
}

function create_review_button(){
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
}

function review_code(){
    window.location.href = "review.html";
}

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
    enable_input();
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