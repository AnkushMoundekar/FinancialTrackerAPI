const BASE_URL = "http://127.0.0.1:8000";

export async function apiRequest(endpoint, method = "GET", body = null) {

    const token = localStorage.getItem("access_token")
    
    const makeRequest = async (token) => {
        const headers = {
            "Content-Type": "application/json"
        };

        if (token) {
            headers["Authorization"] = `Bearer ${token}`;
        }

        return fetch(`${BASE_URL}${endpoint}`, {
            method: method,
            headers: headers,
            body: body ? JSON.stringify(body) : null
        });
    }
    let response = await makeRequest(token);

    // If token expired → try refresh
    if (response.status === 401) {
        try {
            const newToken = await refreshAccessToken();

            response = await makeRequest(newToken);

        } catch (error) {
            localStorage.clear();
            window.location.href = "login.html";
            return;
        }
    }
    if (!response.ok) {
        throw new Error("API request failed");
    }

    return response.json();
}
async function refreshAccessToken() {
    const refreshToken = localStorage.getItem("refresh_token");

    const response = await fetch(`${BASE_URL}/auth/refresh`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            refresh_token: refreshToken
        })
    });

    if (!response.ok) {
        throw new Error("Refresh failed");
    }

    const data = await response.json();

    localStorage.setItem("access_token", data.access_token);

    return data.access_token;
}