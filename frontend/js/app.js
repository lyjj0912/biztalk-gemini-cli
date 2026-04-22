const API_BASE = "http://localhost:8000";
const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");
const targetButtons = document.querySelectorAll(".target-btn");
const convertBtn = document.getElementById("convertBtn");

targetButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        targetButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
    });
});

convertBtn.addEventListener("click", async () => {
    const target = document.querySelector(".target-btn.active").dataset.target;
    const response = await fetch(`${API_BASE}/api/convert`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: inputText.value, target_audience: target })
    });
    const data = await response.json();
    outputText.value = data.converted_text;
});
