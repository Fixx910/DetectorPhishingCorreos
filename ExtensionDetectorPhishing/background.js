fetch('http://localhost:5000/check_spam', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email_content: "Este es el contenido del correo que quieres verificar"
    })
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
  