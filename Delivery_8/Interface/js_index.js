// counts number of blocks written
var block_counter = 0;
var file_upload = false;
var file_text = "-1";

//jquery methods
$(document).ready(function(){
    $('#input-4').on('fileloaded', function(event, file, previewId, index, reader) {
        file_loaded(file);
    });

    $('#input-4').on('fileclear', function(event) {
        file_cancel();
    });
});

function file_loaded(file){
    //successful file upload
    file_upload = true;

    //get text
    read = new FileReader();
    read.readAsText(file);

    read.onloadend = function(){
        file_text = read.result;
    }

    //render blocks useless, button
    document.getElementById("add-block-button").disabled = true;
    
    //disable all blocks
    disable_blocks();
}

function file_cancel(){
    //successful file upload
    file_upload = false;

    //reset text
    file_text = "-1";

    //render blocks useless, button
    document.getElementById("add-block-button").disabled = false;

    //enable all blocks
    enable_blocks();
}

//enable blocks
function enable_blocks(){
    //blocks must exist
    if(block_counter > 0){

        //iterate through blocks
        for(var i = 1; i <= block_counter;i++){
            name_id = "block-name" + i;
            code_id = "block-code" + i;

            name_block = document.getElementById(name_id);
            code_block = document.getElementById(code_id);

            name_block.disabled = false;
            code_block.disabled = false;
        }
    }
}

//disable blocks
function disable_blocks(){
    //blocks must exist
    if(block_counter > 0){

        //iterate through blocks
        for(var i = 1; i <= block_counter;i++){
            name_id = "block-name" + i;
            code_id = "block-code" + i;

            name_block = document.getElementById(name_id);
            code_block = document.getElementById(code_id);

            name_block.disabled = true;
            code_block.disabled = true;
        }
    }
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

// enables block code
function block_name_input(id){
	var b = "block-code" + id.slice(-1);
	var a = document.getElementById(b);
	if (a.disabled) {
		a.disabled = false;
	}
}

// code ready to be compiled
function compile_code() {
  //link for compiler
  var compilerURI = "http://127.0.0.1:5000/post_code";

  //get code from blocks
  if(!file_upload){
    //build code from text
    var finished_code = get_code();

    //user wrote code (blocks were created)
    if(finished_code != "-1") {
        var clean_string = finished_code.replace(/[^a-zA-Z ]/g, "");
        if( clean_string.replace(/\s/g,'') == ""){
            create_bootstrap_alert("Write code to compile! ","You can add a block or upload a file.");
        }

        else{
            //build json from code
            var data_js = JSON.stringify({"code":finished_code});

            //send ajax post request
            post_request_ajax(compilerURI,data_js);
        }
    }
  }
  
  //get code from file
  else {
    if(file_text != "-1"){
        //build json from code
        var data_js = JSON.stringify({"code":file_text});

        //send ajax post request
        post_request_ajax(compilerURI,data_js);
    }

    else {
        create_bootstrap_alert("Write code to compile! ","You can add a block or upload a file.");
    }
  }
}

//gather code form blocks to string
function get_code(){
    var finished_code = "";
    //blocks must exist
    if(block_counter > 0){
        var name_id, code_id, name_block, code_block, name, block, temp;

        //iterate through blocks
        for(var i = 1; i <= block_counter;i++){
            name_id = "block-name" + i;
            code_id = "block-code" + i;

            name_block = document.getElementById(name_id);
            code_block = document.getElementById(code_id);

            name = name_block.value;
            code = code_block.value;

            name = name + "\n";
            temp = name + code;

            //only grabs blocks with code
            var clean_string = temp.replace(/[^a-zA-Z ]/g, "");
            if( clean_string.replace(/\s/g,'') != ""){
                finished_code = finished_code + temp +  "\n\n";
            }
        }
        return finished_code;
    }

    else {
        //call alert function
        if(!file_upload) {
            create_bootstrap_alert("Write code to compile! ","You can add a block or upload a file.");
            return "-1";
        }
    }
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

//ajax post request
function post_request_ajax(uri,data_js){

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
        window.location.href = "runtime.html";
    }
    else {
        //bootstrap alert
        create_bootstrap_alert("ERROR " + result_code,": Compilation not successful");
    }
}

// adds block to block list
function add_block() {
  block_counter = block_counter + 1;
 
  var node = document.createElement("A"); 

  node.setAttribute("href","#");
  node.setAttribute("class","list-group-item");

  var node_block_name_form = document.createElement("INPUT"); 

  node_block_name_form.setAttribute("type","text");
  node_block_name_form.setAttribute("class","form-control");
  node_block_name_form.setAttribute("id","block-name" + block_counter);
  node_block_name_form.setAttribute("placeholder", "Block name here e.g. \"block MyBlock\"");
  node_block_name_form.setAttribute("oninput","block_name_input(this.id)");

  var node_block_code_form = document.createElement("TEXTAREA");

  node_block_code_form.setAttribute("style","overflow:hidden; max-width:100%;");
  node_block_code_form.setAttribute("class","form-control");
  node_block_code_form.setAttribute("rows","1");
  node_block_code_form.setAttribute("class","form-control");
  node_block_code_form.setAttribute("id","block-code" + block_counter);
  node_block_code_form.setAttribute("placeholder", "Block code here");
  node_block_code_form.setAttribute("onkeyup", "resizeTextarea(this.id)");
  node_block_code_form.disabled = true;
  
  node.appendChild(node_block_name_form); 
  node.appendChild(node_block_code_form);  

  document.getElementById("block-list").appendChild(node); 
  document.getElementById("block-name" + block_counter).focus(); 
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