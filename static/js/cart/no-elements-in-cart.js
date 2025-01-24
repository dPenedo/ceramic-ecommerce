export function noElementsInCart() {
    // WARN: no se muestra cuando se borra el ultimo elemento pero si cuando no hay ninguno al entrar
    console.log("nooo");
    const mensajeCarroVacio = document.getElementById("mensaje-carro-vacio");
    console.log(mensajeCarroVacio);
    mensajeCarroVacio.textContent = "No hay elementos";
}
