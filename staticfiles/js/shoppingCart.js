const agregarAlCarrito = document.getElementById("agregar-al-carrito")
let shoppingCart = {}


agregarAlCarrito.addEventListener("click", async function () {
    try {
        const response = await fetch('/api/stock')
        const products = await response.json()
        console.log(products)
    } catch (error) {
        console.log("Error al cargar", error)
    }

})