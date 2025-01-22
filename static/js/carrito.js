const shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];

const productsIds = shoppingCart.map((item) => item.id);

if (productsIds.length > 0) {
    const queryString = new URLSearchParams({
        "shopping-cart": productsIds,
    }).toString();
    window.location.href = `/carrito?${queryString}`;
}
