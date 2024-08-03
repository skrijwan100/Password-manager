let visibale = document.getElementsByClassName("visibale")
console.log(visibale)
function showpassword() {
    let storepass = document.getElementById("storepass")
    visibale.style.display = "none"
    if (storepass.type == "password") {
        storepass.type = "text"
    }
    else {
        storepass.type = "password"

    }
}

