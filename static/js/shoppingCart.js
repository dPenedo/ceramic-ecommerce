const agregarAlCarrito = document.getElementById("agregar-al-carrito");
const stockCantidad = document.getElementById("stock-cantidad");
const stockDisponible = document.getElementById("stock-disponible");
let shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
let virtualTotalStock = {};

const productId = selectedProductId || null

const initialStock = parseInt(stockCantidad.textContent || 0);

virtualTotalStock[productId] = initialStock;

agregarAlCarrito.addEventListener("click", async function () {
    try {
        const response = await fetch(`/api/stock/${productId}`);
        const products = await response.json();

        const fetchedId = products.id;
        const fetchedTitle = products.titulo;
        let fetchedStock = products.stock;

        const productInCart = shoppingCart.find(
            (item) => item.id === fetchedId,
        );
        if (productInCart) {
            productInCart.amount += 1;
        } else {
            shoppingCart.push({
                id: fetchedId,
                amount: 1,
                title: fetchedTitle,
            });
        }

        if (virtualTotalStock[fetchedId] > 0) {
            virtualTotalStock[fetchedId] -= 1;
            stockCantidad.textContent = virtualTotalStock[productId];
        }
        if (virtualTotalStock[productId] === 0  ) {
            stockDisponible.textContent = "Agotado";
            stockDisponible.classList.remove("text-green-700");
            stockDisponible.classList.add("text-red-800");
            agregarAlCarrito.disabled = true
            agregarAlCarrito.classList.remove("bg-yellow-700", "hover:bg-yellow-800") = true
            agregarAlCarrito.classList.add("bg-gray-400", "cursor-not-allowed")
        }
      localStorage.setItem("shoppingCart", JSON.stringify(shoppingCart))



      console.log("Cart-> ", shoppingCart)
      console.log("Virtual stock-> ", virtualTotalStock)
    } catch (error) {
        console.log("Error al cargar", error);
    }
});
