
var currentURL = window.location.href; // Current url 
saveOnServer(currentURL)
function saveOnServer(content) 
{
    var url ="http://127.0.0.1:5000/"; 
    var params = "content="+ content;
    var http = new XMLHttpRequest();  
    http.open("POST",url, true);
    http.setRequestHeader(
        "Content-type",
        "application/x-www-form-urlencoded"
    );
    console.time("Phishing Detection")
    http.onreadystatechange = function() 
    {
        if(http.readyState == 4 && http.status == 200) 
        {
             alter=http.responseText;
             console.log(alter);
             var r=0;
             alert(alter);
             
        }
    }
   console.timeEnd("Phishing Detection")

    http.send(params);
};
