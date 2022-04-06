document.addEventListener("mouseover", function() {
    document.body.style.backgroundColor = "lavender";
});
document.addEventListener("mouseout", function() {
    document.body.style.backgroundColor = "white";
});

var input = document.getElementById("customFile");
var output = document.getElementById("output");

input.addEventListener("change", function () {
  if (this.files && this.files[0]) {
    var myFile = this.files[0];
    var reader = new FileReader();
    
    reader.addEventListener('load', function (e) {
      output.textContent = e.target.result;
    });
    
    reader.readAsBinaryString(myFile);
  }   
});

//var output = document.getElementById("output").value;
function getHello() {
    let myName = "Gery";
    let myPassword = "abcde";
    const url = 'http://localhost:8989/test'
    fetch(url, {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      
        //make sure to serialize your JSON body
        body: JSON.stringify({
          name: myName,
          password: myPassword
        })
      })
      .then( (response) => { 
         //do something awesome that makes the world a better place
      });
}