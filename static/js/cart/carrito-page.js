import { noElementsInCart } from "./no-elements-in-cart.js";

if (!isAuthenticated) {
    const shoppingCart = JSON.parse(localStorage.getItem("shoppingCart")) || [];
    const productsIds = shoppingCart.map((item) => item.id);

    if (productsIds.length > 0) {
        const queryString = new URLSearchParams();
        productsIds.forEach((id) => {
            queryString.append("shopping-cart", id);
        });
        if (!window.location.href.includes(queryString.toString())) {
            window.location.href = `/carrito?${queryString.toString()}`;
        }
    } else {
        noElementsInCart();
    }
}
