import { apiRequest } from "./api.js";

const loginForm = document.getElementById("loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        try {
            const data = await apiRequest("/auth/login", "POST", {
                email,
                password
            });

            localStorage.setItem("access_token", data.access_token);
            localStorage.setItem("refresh_token", data.refresh_token);

            window.location.href = "dashboard.html";

        } catch (error) {
            alert("Login failed");
        }
    });
}


const registerForm = document.getElementById("registerForm");

if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const email = document.getElementById("register-email").value;
        const password = document.getElementById("register-password").value;

        try {
            await apiRequest("/users/register", "POST", {
                email,
                password
            });

            alert("Registered successfully!");
            window.location.href = "login.html";

        } catch (error) {
            alert("Registration failed");
        }
    });
}