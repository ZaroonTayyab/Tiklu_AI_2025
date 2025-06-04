const messagesDiv = document.getElementById("messages");
const userInput = document.getElementById("userInput");

function appendMessage(sender, text) {
    const msgDiv = document.createElement("div");
    const senderSpan = document.createElement("span");
    senderSpan.className = "sender";
    senderSpan.textContent = sender + ":";
    msgDiv.appendChild(senderSpan);
    msgDiv.appendChild(document.createTextNode(" " + text));
    messagesDiv.appendChild(msgDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    appendMessage("You", message);
    userInput.value = "";

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("TikluAI", data.reply);
        speak(data.reply);
    })
    .catch(() => {
        appendMessage("TikluAI", "Sorry, something went wrong.");
    });
}

function speak(text) {
    if (!window.speechSynthesis) return;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = 1;
    utterance.voice = speechSynthesis.getVoices().find(voice => voice.name === "Google US English") || null;
    window.speechSynthesis.speak(utterance);
}

userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        sendMessage();
    }
});
function addMessage(sender, text) {
    const messagesDiv = document.getElementById("messages");
    const messageElem = document.createElement("div");
    messageElem.classList.add("message");
    messageElem.classList.add(sender); // "user" or "bot"
    messageElem.textContent = text;
    messagesDiv.appendChild(messageElem);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll down
}

function sendMessage() {
    const input = document.getElementById("userInput");
    const userText = input.value.trim();
    if (!userText) return;

    addMessage("user", "You: " + userText);  // Show user input on screen
    input.value = "";

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
    })
    .then(response => response.json())
    .then(data => {
        addMessage("bot", "Jarvis: " + data.reply);  // Show AI reply on screen
        // Optional: Speak the reply with speechSynthesis here
        if ("speechSynthesis" in window) {
            const utterance = new SpeechSynthesisUtterance(data.reply);
            utterance.voice = speechSynthesis.getVoices().find(voice => voice.name.includes("Male")) || null;
            speechSynthesis.speak(utterance);
        }
    })
    .catch(error => {
        addMessage("bot", "Error: Could not get response.");
        console.error("Error:", error);
    });
}
