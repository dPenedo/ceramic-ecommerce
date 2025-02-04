import { updateNavbarCartAmount } from "./update-navbar-cart-amount.js";

const botonDeAgregarAlCarrito = document.getElementById(
    "boton-de-agregar-al-carrito",
);
const mensajeNoMasStock = document.getElementById("mensaje-no-mas-stock");
// Tomar cart del localStorage
let shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
// Tomar id del producto
const productId =
    typeof selectedProductId !== "undefined" ? selectedProductId : null;

if (botonDeAgregarAlCarrito && !isAuthenticated) {
    botonDeAgregarAlCarrito.addEventListener("click", async function () {
        mensajeNoMasStock.classList.add("hidden");
        try {
            const response = await fetch(`/api/stock/${productId}`);
            if (!response.ok)
                throw new Error("Error al obtener los datos del stock");

            const { id, titulo, stock } = await response.json();

            const productInCart = shoppingCart.find((item) => item.id === id);
            if (stock > 0) {
                if (productInCart) {
                    if (productInCart.amount >= stock) {
                        mensajeNoMasStock.classList.remove("hidden");
                    } else {
                        productInCart.amount += 1;
                        console.log("Producto sumado", productInCart.amount);
                    }
                } else {
                    shoppingCart.push({
                        id: id,
                        amount: 1,
                        title: titulo,
                    });
                    console.log("Producto añadido", titulo);
                }
            }

            localStorage.setItem("shoppingCart", JSON.stringify(shoppingCart));

            updateNavbarCartAmount();
        } catch (error) {
            console.error("Error al cargar el producto al carrito:", error);
        }
    });
}
// Actualizar la cantidad del carrito al cargar la página
updateNavbarCartAmount();
