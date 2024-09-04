/* Pregunta: ¿Cuál es la función de 'document.getElementById' en JavaScript? */
/*La función document.getElementById en JavaScript se utiliza para seleccionar y acceder a un elemento del DOM (Document Object Model)*/
        function checkAnswer() {
            /* Pregunta: ¿Qué hace 'prompt' y cómo se puede usar en lugar de 'alert'? */
            let answer = prompt("Enter your answer:");

            /* Pregunta: ¿Cuál es el propósito de la instrucción 'if' en este fragmento de código? */
                /*Es una condicion que nos indica que si la respuesta es  igual a 'paris' lance una alerta de que es correcta*/
            if (answer.toLowerCase() === 'paris') {
                alert("Correct!");
            } else {
                alert("Try again!");
            }
        }

        /* Pregunta: ¿Cómo se puede manipular el DOM usando JavaScript para cambiar el contenido de un elemento? */
        document.getElementById("question").innerText = "What is the capital of France?";
