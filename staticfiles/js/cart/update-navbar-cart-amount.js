export function updateNavbarCartAmount() {
    const amountProducts = document.getElementById("amount-products-in-cart");

    const storedShoppingCart =
        JSON.parse(localStorage.getItem("shoppingCart")) || [];
    let totalAmountInCart = 0;

    storedShoppingCart.forEach((product) => {
        totalAmountInCart += product.amount;
    });

    if (amountProducts && totalAmountInCart !== 0) {
        amountProducts.textContent = totalAmountInCart;
    }
}

if (!isAuthenticated) {
    document.addEventListener("DOMContentLoaded", () => {
        console.log("update navbar");
        updateNavbarCartAmount();
    });
}
