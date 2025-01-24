export function setAmountOfProducts() {
    const amountOfEachProductSpans = document.querySelectorAll(
        ".amount-of-each-product",
    );
    console.log(amountOfEachProductSpans);

    amountOfEachProductSpans.forEach((span) => {
        const productId = span.getAttribute("data-id");
        const shoppingCart =
            JSON.parse(localStorage.getItem("shoppingCart")) || [];
        const product = shoppingCart.find((item) => item.id == productId);
        const parentDiv = span.closest("#pieza-en-carrito");
        if (product && product.amount > 0) {
            span.textContent = "";
            span.textContent = product.amount || 1;
            parentDiv.classList.remove("hidden");
        } else {
            parentDiv?.classList.add("hidden");
        }
    });
}
setAmountOfProducts();
