const shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
const conservarCarrito = document.getElementById("conservar-carrito");
const carritoData = document.getElementById("carrito-data");
const form = document.querySelector("form");

console.log("Carrito => ", shoppingCart);
console.log("boton conservar carrito => ", conservarCarrito);
console.log("boton conservar carrito value => ", conservarCarrito.value);

conservarCarrito.addEventListener("change", () => {
    if (conservarCarrito.checked) {
        carritoData.value = JSON.stringify(shoppingCart);
        console.log(carritoData.value);
    } else {
        carritoData.value = "";
    }
    console.log("Carrito data => " + carritoData.value);
});
