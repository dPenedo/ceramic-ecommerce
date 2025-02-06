import { setAmountOfProducts } from "./set-amount-of-products.js";
import { updateNavbarCartAmount } from "./update-navbar-cart-amount.js";
import { noElementsInCart } from "./no-elements-in-cart.js";

if (!isAuthenticated) {
    const removeButtons = document.querySelectorAll(".remove-from-cart");
    const storedShoppingCart = JSON.parse(localStorage.getItem("shoppingCart"));
    removeButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-id");
            removeProduct(productId);
        });
    });

    function removeProduct(id) {
        const product = storedShoppingCart.find((pro) => pro.id == id);

        if (product) {
            product.amount -= 1;
            if (product.amount <= 0) {
                const index = storedShoppingCart.findIndex(
                    (pro) => pro.id == id,
                );
                storedShoppingCart.splice(index, 1);
            }

            localStorage.setItem(
                "shoppingCart",
                JSON.stringify(storedShoppingCart),
            );
        }
        if (storedShoppingCart.length === 0) {
            noElementsInCart();
        }

        console.log(product ? product.amount : "Producto no encontrado");
        updateNavbarCartAmount();
        setAmountOfProducts();
    }
}
