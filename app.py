from flask import Flask, request, session

app = Flask(**name**)
app.secret_key = "PXNAGUA_SECRET_2026"

@app.route("/", methods=["GET", "POST"])
def inicio():

```
if "chat" not in session:
    session["chat"] = []

if request.method == "POST":

    mensaje = request.form.get("mensaje", "")
    texto = mensaje.lower()

    respuesta = "No entendí muy bien eso."

    if "hola" in texto:
        respuesta = "Hola, ¿cómo estás?"

    elif "quien eres" in texto:
        respuesta = "Soy PXNAGUA'S IA."

    elif "como estas" in texto:
        respuesta = "Estoy excelente y lista para ayudarte."

    elif "motivame" in texto:
        respuesta = "Nunca es tarde para aprender algo nuevo."

    elif "taller matematicas" in texto:
        respuesta = """
```

TALLER DE MATEMATICAS

1. Resolver 5x + 10 = 35
2. Resolver 8 x 7
3. Hallar el área de un rectángulo de 8 x 5
   """

   ```
    elif "taller ingles" in texto:
        respuesta = """
   ```

TALLER DE INGLES

1. Traduce: Hola, ¿cómo estás?
2. Escribe 5 verbos en inglés.
3. Crea 3 oraciones en inglés.
   """

   ```
    elif "taller ciencias" in texto:
        respuesta = """
   ```

TALLER DE CIENCIAS

1. ¿Qué es la fotosíntesis?
2. Explica el ciclo del agua.
3. Nombra los estados de la materia.
   """

   ```
    elif "horario" in texto:
        respuesta = """
   ```

HORARIO RECOMENDADO

08:00 Clase principal
10:00 Descanso
10:30 Taller práctico
12:00 Almuerzo
14:00 Evaluaciones
15:30 Retroalimentación
"""

```
    elif "actividad" in texto:
        respuesta = "Actividad recomendada: Debate académico."

    elif "ayuda" in texto:
        respuesta = """
```

COMANDOS DISPONIBLES

hola
quien eres
como estas
motivame

horario
actividad

taller matematicas
taller ingles
taller ciencias
"""

```
    chat = session["chat"]

    chat.append(("TU", mensaje))
    chat.append(("IA", respuesta))

    session["chat"] = chat

historial = ""

chat = session.get("chat", [])

for autor, mensaje in chat:

    clase = "usuario" if autor == "TU" else "ia"

    historial += f"""
    <div class="{clase}">
        <b>{autor}:</b><br>
        {mensaje}
    </div>
    """

return f"""
```

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>PXNAGUA'S IA</title>

<style>

body {{
    background:#120818;
    color:white;
    font-family:"Courier New", monospace;
    max-width:1000px;
    margin:auto;
    padding:20px;
}}

h1 {{
    text-align:center;
    color:#ce53e9;
    border:4px solid #ce53e9;
    padding:15px;
    text-shadow:3px 3px #000;
    box-shadow:0 0 20px #ce53e9;
}}

.chat {{
    background:#1c1026;
    border:4px solid #ce53e9;
    min-height:500px;
    padding:15px;

    box-shadow:
        0 0 10px #ce53e9,
        0 0 20px #ce53e9,
        0 0 40px #ce53e9;
}}

.usuario {{
    background:#8a2be2;
    padding:12px;
    margin:10px;
    border:3px solid white;
    text-align:right;
}}

.ia {{
    background:#2a1838;
    padding:12px;
    margin:10px;
    border:3px solid #ce53e9;
}}

form {{
    display:flex;
    gap:10px;
    margin-top:15px;
}}

input {{
    flex:1;
    padding:12px;
    background:#1c1026;
    color:white;
    border:3px solid #ce53e9;
    font-size:16px;
}}

button {{
    padding:12px 20px;
    background:#ce53e9;
    color:white;
    border:none;
    font-weight:bold;
    cursor:pointer;
}}

.avatar {{
    text-align:center;
    font-size:100px;
    margin-bottom:10px;
}}

.corazon-izq {{
    position:fixed;
    left:0;
    top:50%;
    transform:translateY(-50%);
    width:350px;
    z-index:-1;
    pointer-events:none;
}}

.corazon-der {{
    position:fixed;
    right:0;
    top:50%;
    transform:translateY(-50%);
    width:350px;
    z-index:-1;
    pointer-events:none;
}}

@media (max-width:768px) {{

    .corazon-izq,
    .corazon-der {{
        width:150px;
    }}

    form {{
        flex-direction:column;
    }}

}}

</style>

</head>

<body>

<div class="avatar">
🤖
</div>

<h1>PXNAGUA'S IA WEB</h1>

<img src="/static/corazones.png" class="corazon-izq">
<img src="/static/corazones.png" class="corazon-der">

<div class="chat">

{historial}

</div>

<form method="POST">

<input
type="text"
name="mensaje"
placeholder="Escribe algo..."
required>

<button type="submit">
Enviar
</button>

</form>

</body>

</html>
"""

import os

if **name** == "**main**":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

