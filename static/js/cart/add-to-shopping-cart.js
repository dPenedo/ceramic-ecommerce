import { updateNavbarCartAmount } from "./update-navbar-cart-amount.js";

const botonDeAgregarAlCarrito = document.getElementById("boton-de-agregar-al-carrito");
const mensajeNoMasStock = document.getElementById("mensaje-no-mas-stock")
// Tomar cart del localStorage
let shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
// Tomar id del producto
const productId =
    typeof selectedProductId !== "undefined" ? selectedProductId : null;

if (botonDeAgregarAlCarrito) {
    botonDeAgregarAlCarrito.addEventListener("click", async function() {
        mensajeNoMasStock.classList.add("hidden")
        try {
            const response = await fetch(`/api/stock/${productId}`);
            if (!response.ok)
                throw new Error("Error al obtener los datos del stock");

            const productData = await response.json();

            const fetchedId = productData.id;
            const fetchedTitle = productData.titulo;
            const fetchedStock = productData.stock;

            const productInCart = shoppingCart.find(
                (item) => item.id === fetchedId
            );
            if (fetchedStock > 0) {
                if (productInCart) {
                    if (productInCart.amount >= fetchedStock) {
                        mensajeNoMasStock.classList.remove("hidden")
                    } else {
                        productInCart.amount += 1;
                        console.log("Producto sumado", productInCart.amount);
                    }
                } else {
                    shoppingCart.push({
                        id: fetchedId,
                        amount: 1,
                        title: fetchedTitle
                    });
                    console.log("Producto añadido", fetchedTitle);
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