function checkPassword() {
    const password = document.getElementById("password").value;
    if (password === "mypassword123") { 
        document.getElementById("diary-content").style.display = "block";
    } else {
        alert("Incorrect password!");
    }
}
