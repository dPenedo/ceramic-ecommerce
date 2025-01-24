export function noElementsInCart() {
    const mensajeCarroVacio = document.getElementById("mensaje-carro-vacio");
    if (mensajeCarroVacio) {
        mensajeCarroVacio.textContent = "No hay elementos en tu carrito.";
    }
}
