export function updateNavbarCartAmount() {
    if (!isAuthenticated) {
        const amountProducts = document.getElementById(
            "amount-products-in-cart",
        );

        const storedShoppingCart =
            JSON.parse(localStorage.getItem("shoppingCart")) || [];
        let totalAmountInCart = 0;

        storedShoppingCart.forEach((product) => {
            totalAmountInCart += product.amount;
        });

        if (amountProducts && totalAmountInCart > 0) {
            amountProducts.textContent = totalAmountInCart;
        } else {
            amountProducts.textContent = "";
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    updateNavbarCartAmount();
});
