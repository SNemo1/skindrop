let btn = document.getElementById("spin-btn");
let text = document.getElementById("result-text");

btn.addEventListener("click", function() {fetch('http://127.0.0.1:8000/spin')
    .then(response => response.json())
.then(data => {
    text.innerText = data.massage;
    }
)}