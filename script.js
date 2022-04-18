console.log("Hello There and Welcome to my title page");
var id = null;
var imageUpload = false;
function businessCard() {
    var elem = document.getElementById("card");
    var pos = -10;
    clearInterval(id);
    id = setInterval(frame, 1);
    function frame() {
      if (pos == 300) {
        clearInterval(id);
      } else {
        pos++;
        elem.style.top = pos + 'px';
      }
    }
  }


function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        imageUpload = true;
        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
            $('#imageResult')
                .attr('width', 400);
            $('#imageResult')
                .attr('height', 500);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById( 'upload' );
var infoArea = document.getElementById( 'upload-label' );

input.addEventListener( 'change', showFileName );
function showFileName( event ) {
  var input = event.srcElement;
}

function sendImage(){
  if (imageUpload){
    var output = document.getElementById("imageResult").src;
    let text = output;
    console.log(text);
    console.log("Starting AJAX");
    $.ajax({
        url: "http://localhost:8989/test",
        type: "POST",
        data: text,
        dataType:"json",
        success: function(data){
            var myData = data["Names"];
            document.getElementById('output').value = myData;
            console.log(myData);
        }
    });
  }
  else{
    alert("Image must be uploaded prior to processing.")
  }
}
