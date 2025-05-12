document.addEventListener("DOMContentLoaded", function () {
    const overlay = document.getElementById("overlay");
    const loginUI = document.getElementById("floatingUI");
    const guestUI = document.getElementById("guestUI");
    const registerUI = document.getElementById("registerUI");
    const forgotUI = document.getElementById("forgotPasswordUI");
    const recoveryUI = document.getElementById("recoveryUI");
    const aboutUsUI = document.getElementById("aboutUsUI");
    const aboutUsContent = document.getElementById("aboutUsContent");

    function showUI(id) {
        overlay.style.display = "block";
        document.querySelectorAll(".floating-ui").forEach(el => el.style.display = "none");
        document.getElementById(id).style.display = "block";
    }

    function hideAllUI() {
        overlay.style.display = "none";
        document.querySelectorAll(".floating-ui").forEach(el => el.style.display = "none");
    }

    function toggleRegisterPassword() {
        const inputs = document.querySelectorAll('input[type="password"]');
        inputs.forEach(input => {
            input.type = input.type === "password" ? "text" : "password";
        });
    }

    document.getElementById("loginLink").addEventListener("click", (e) => {
        e.preventDefault();
        showUI("floatingUI");
    });

    document.getElementById("guestBtn").onclick = () => showUI("guestUI");
    document.getElementById("backToLoginBtn").onclick = () => showUI("floatingUI");
    document.getElementById("switchToRegisterBtn").onclick = () => showUI("registerUI");
    document.getElementById("backToLoginFromRegisterBtn").onclick = () => showUI("floatingUI");
    document.getElementById("forgotPasswordLink").onclick = (e) => {
        e.preventDefault();
        showUI("forgotPasswordUI");
    };
    document.getElementById("backToLoginFromForgotBtn").onclick = () => showUI("floatingUI");
    document.getElementById("sendCodeBtn").onclick = () => showUI("recoveryUI");
    document.getElementById("cancelRecoveryBtn").onclick = hideAllUI;

    document.getElementById("closeBtn").onclick = hideAllUI;
    document.getElementById("guestCloseBtn").onclick = hideAllUI;
    document.getElementById("registerCloseBtn").onclick = hideAllUI;
    document.getElementById("forgotCloseBtn").onclick = hideAllUI;
    document.getElementById("recoveryCloseBtn").onclick = hideAllUI;

    document.querySelectorAll(".toggle-password").forEach(span => {
        span.onclick = toggleRegisterPassword;
    });

    document.getElementById("aboutUsLink").addEventListener("click", function () {
        fetch("assets/aboutus.txt")
            .then(response => response.text())
            .then(data => {
                aboutUsContent.innerHTML = data;
                aboutUsUI.style.display = "block";
            });
    });

    document.getElementById("closeAboutUsBtn").addEventListener("click", () => {
        aboutUsUI.style.display = "none";
    });

    document.getElementById("registerBtn").onclick = async () => {
        const user = document.getElementById("registerUsername").value;
        const email = document.getElementById("registerEmail").value;
        const pass = document.getElementById("registerPassword").value;

        try {
            const response = await fetch("http://localhost:5000/auth/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: user,
                    email: email,
                    password: pass
                })
            });

            const result = await response.json();

            if (response.ok && result.success) {
                alert("Registration successful!");
                hideAllUI();
            } else {
                alert("Registration failed. Please try again.");
                console.error(result.message);
            }
        } catch (error) {
            alert("Registration failed due to a network error.");
            console.error("Error:", error);
        }
    };

    document.getElementById("loginBtn").onclick = async () => {
        const user = document.getElementById("username").value;
        const pass = document.getElementById("password").value;

        try {
            const response = await fetch("http://localhost:5000/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: user,
                    password: pass
                })
            });

            const result = await response.json();

            if (response.ok && result.success) {
                alert("Login successful!");
                hideAllUI();
            } else {
                alert("Login failed. Incorrect credentials.");
                console.error(result.message);
            }
        } catch (error) {
            alert("Login failed due to a network error.");
            console.error("Error:", error);
        }
    };

    document.getElementById("guestLoginBtn").onclick = async () => {
        const guestName = document.getElementById("guestUsername").value;
        const contact = document.getElementById("guestContact").value;

        try {
            const response = await fetch("http://localhost:5000/guest-login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    guestname: guestName,
                    contact: contact
                })
            });

            const result = await response.json();

            if (response.ok && result.success) {
                alert("Guest login successful!");
                hideAllUI();
            } else {
                alert("Guest login failed.");
                console.error(result.message);
            }
        } catch (error) {
            alert("Guest login failed due to a network error.");
            console.error("Error:", error);
        }
    };

    document.getElementById("sendCodeBtn").onclick = async () => {
        const email = document.getElementById("forgotEmail").value;

        try {
            const response = await fetch("http://localhost:5000/forgot-password", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email: email })
            });

            const result = await response.json();

            if (response.ok && result.success) {
                alert("Verification code sent to your email.");
                showUI("recoveryUI");
            } else {
                alert("Failed to send verification code.");
                console.error(result.message);
            }
        } catch (error) {
            alert("Network error during password reset.");
            console.error("Error:", error);
        }
    };
});
