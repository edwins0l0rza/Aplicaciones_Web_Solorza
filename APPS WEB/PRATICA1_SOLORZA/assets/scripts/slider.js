    //Seleccione las imagenes del slider
let slides = document.querySelectorAll('.slide');
let currentSlide = 0;

    //Funcion para cambiar imagen
function changeSlide() {
        //oculta la imagen actual
    slides[currentSlide].classList.remove('active');

        //cambiar al siguiente slide
    currentSlide = (currentSlide + 1) % slides.length;

        //muestra la siguiente imagen
    slides[currentSlide].classList.add('active');

}

    //inicia el slider cambiando cada 3 segundos
setInterval(changeSlide, 3000);