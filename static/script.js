
function togglePassword(id) {
    const passwordInput = document.getElementById(id);
    if(passwordInput.type=="password"){
        passwordInput.type="text"
    }
    else{
        passwordInput.type="password"
        
    }
}

