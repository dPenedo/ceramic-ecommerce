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

function setAmountInProducts() {
    amountOfEachProductSpans.forEach((span) => {
        const productId = span.getAttribute("data-id");
        const product = shoppingCart.find((item) => item.id == productId);
        if (product) {
            span.textContent = product.amount || 1;
        }
    });
}
setAmountInProducts();
