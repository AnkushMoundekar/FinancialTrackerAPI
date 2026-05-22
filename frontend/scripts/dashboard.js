import { apiRequest } from "./api.js";

function showLoading(show) {
    document.getElementById("loading").style.display = show ? "block" : "none";
}

async function loadSummary() {
    showLoading(true)
    try {
        const data = await apiRequest("/analytics/summary");

        document.getElementById("totalExpense").innerText = data.total_expense;
        document.getElementById("totalIncome").innerText = data.total_income;

    } catch (error) {
        alert("Failed to load dashboard");
    }
    showLoading(false)
}


const form = document.getElementById("expenseForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const amount = document.getElementById("amount").value;
    const type = document.getElementById("type").value;
    const description = document.getElementById("description").value;
    const date = document.getElementById("date").value;

    try {
        await apiRequest("/expense/", "POST", {
            amount: parseFloat(amount),
            type,
            description,
            transaction_date: date
        });

        alert("Expense added!");

        form.reset();

        // Refresh summary after adding
        loadSummary();

    } catch (error) {
        alert("Failed to add expense");
    }
});

let offset = 0;
const limit = 5;

async function loadExpenses() {
    const type = document.getElementById("filterType").value;
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;

    let url = `/expense/?limit=${limit}&offset=${offset}`;

    if (type) url += `&type=${type}`;
    if (startDate) url += `&start_date=${startDate}`;
    if (endDate) url += `&end_date=${endDate}`;

    try {
        const data = await apiRequest(url);

        const table = document.getElementById("expenseTable");
        table.innerHTML = "";

        data.forEach(exp => {
            const row = `
                <tr>
                    <td>${exp.amount}</td>
                    <td>${exp.type}</td>
                    <td>${exp.description || "-"}</td>
                    <td>${exp.transaction_date}</td>
                </tr>
            `;
            table.innerHTML += row;
        });

    } catch (error) {
        alert("Failed to load expenses");
    }
}
loadExpenses()
document.getElementById("applyFilter").addEventListener("click", () => {
    offset = 0;
    loadExpenses();
});

document.getElementById("nextBtn").addEventListener("click", () => {
    offset += limit;
    loadExpenses();
});

document.getElementById("prevBtn").addEventListener("click", () => {
    if (offset >= limit) {
        offset -= limit;
        loadExpenses();
    }
});


// Initialize the Bootstrap Modal component instance
    const transactionModal = new bootstrap.Modal(document.getElementById('addTransactionModal'));
    const expenseForm = document.getElementById('expenseForm');

    // Handles modal closing & form resetting on form submit
    expenseForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Closes the open modal pop-up window cleanly
        transactionModal.hide();
        
        // Clears out all entered input field form data 
        expenseForm.reset();
    });

async function loadCategoryChart() {
    const data = await apiRequest("/analytics/by-category");

    const labels = data.map(item => item.category);
    const values = data.map(item => item.total);

    new Chart(document.getElementById("categoryChart"), {
        type: "pie",
        data: {
            labels: labels,
            datasets: [{
                data: values
            }]
        }
    });
}

async function loadMonthlyChart() {
    const data = await apiRequest("/analytics/monthly");

    const labels = data.map(item => item.month);
    const values = data.map(item => item.total);

    new Chart(document.getElementById("monthlyChart"), {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Monthly Expense",
                data: values
            }]
        }
    });
}



document.getElementById("logoutBtn").addEventListener("click", () => {
    localStorage.clear();
    window.location.href = "login.html";
});

async function loadDashboard() {
    try {
        await Promise.all([
            loadSummary(),
            loadExpenses(),
            loadCategoryChart(),
            loadMonthlyChart()
        ]);
    } catch (error) {
        console.error("Dashboard load failed");
    }
}

loadDashboard();