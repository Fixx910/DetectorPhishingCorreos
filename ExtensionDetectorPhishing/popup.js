document.getElementById("checkPhishing").addEventListener("click", async () => {
    const emailBody = document.getElementById("emailBody").value;
    
    if (emailBody.trim() === "") {
        alert("Por favor, pega el cuerpo del email.");
        return;
    }

    // Enviar la solicitud al servidor local
    try {
        const response = await fetch("http://localhost:5000/check_phishing", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: emailBody })
        });
        const data = await response.json();
        document.getElementById("result").innerText = data.result;
    } catch (error) {
        console.error("Error al conectarse al servidor:", error);
        document.getElementById("result").innerText = "Error al conectarse al servidor.";
    }
});
