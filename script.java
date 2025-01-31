const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const messageContainer = document.querySelector(".message-container");

sendButton.addEventListener("click", async () => {
    const message = userInput.value.trim();
    if (message) {
        const response = await fetch("/chatbot", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });
