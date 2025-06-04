submitBtn.addEventListener("click", async (e) => {
    e.preventDefault();
    console.log("Clicked!");
    resultCont.innerHTML = `<img width="123" src="img/loading.svg" alt="">`;
    let key = "ema_live_yDiFaCgmS4wJuTwA8oIIL4S1SOUeonByf9Nq17DO";
    let email = document.getElementById("username").value;
    let url = `https://api.emailvalidation.io/v1/info?apikey=${key}&email=${email}`;
    let res = await fetch(url);
    let result = await res.json();
    let str = ``;

    // SMTP check
    if (result.smtp_check) {
        str += `<div>✅ The email is active and can receive messages.</div>`;
    } else {
        str += `<div>❌ This email does not seem to be able to receive messages.</div>`;
    }

    // MX record check
    if (result.mx_found) {
        str += `<div>✅ The email domain has proper mail servers.</div>`;
    } else {
        str += `<div>⚠️ The email domain has no mail servers. It might be fake or inactive.</div>`;
    }

    // Disposable email
    if (result.disposable) {
        str += `<div>⚠️ This is a disposable (temporary) email address.</div>`;
    } else {
        str += `<div>✅ This is a regular email address (not temporary).</div>`;
    }

    // Role based email
    if (result.role) {
        str += `<div>⚠️ This is a role-based email (like info@ or support@), not a personal email.</div>`;
    } else {
        str += `<div>✅ This looks like a personal email address.</div>`;
    }

    // Free email provider
    if (result.free) {
        str += `<div>✅ This is a free email provider (like Gmail, Yahoo).</div>`;
    } else {
        str += `<div>✅ This is a business email address.</div>`;
    }

    // Format validity
    if (result.format_valid) {
        str += `<div>✅ The email format is valid.</div>`;
    } else {
        str += `<div>❌ The email format is invalid.</div>`;
    }

    // Raw data fields (could be undefined)
    str += `<div>📊 Overall Score: ${result.score}</div>`;
    str += `<div>📬 Email Address: ${result.email}</div>`;
    str += `<div>📁 Domain: ${result.domain}</div>`;
    str += `<div>📝 Status: ${result.state}</div>`;
    str += `<div>🧐 Reason: ${result.reason}</div>`;

    resultCont.innerHTML = str;
});
