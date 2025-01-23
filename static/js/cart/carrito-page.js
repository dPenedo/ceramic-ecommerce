const shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
const productsIds = shoppingCart.map((item) => item.id);
const amountOfEachProductSpans = document.querySelectorAll(
    ".amount-of-each-product",
);

if (productsIds.length > 0) {
    const queryString = new URLSearchParams();
    productsIds.forEach((id) => {
        queryString.append("shopping-cart", id);
    });
    if (!window.location.href.includes(queryString.toString())) {
        window.location.href = `/carrito?${queryString.toString()}`;
    }
}

// WARN: Funciona pero no se actualiza
export function setAmountOfProducts() {
    console.log("set amount");
    amountOfEachProductSpans.forEach((span) => {
        const productId = span.getAttribute("data-id");
        const product = shoppingCart.find((item) => item.id == productId);
        if (product) {
            span.textContent = "";
            span.textContent = product.amount || 1;
        }
    });
}
setAmountOfProducts();
