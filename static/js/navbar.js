const burgerButton = document.getElementById("burger-button");
const navbarMenu = document.getElementById("ecommerce-navbar-menu-1");

const accountButton = document.getElementById("accountDropdownButton") || null;
const accountMenu = document.getElementById("accountMenu");

const amountProducts = document.getElementById("amount-products-in-cart");

// BurgerLogic
burgerButton.addEventListener("click", function () {
    navbarMenu.classList.toggle("hidden");
});

document.addEventListener("click", function (event) {
    if (
        !burgerButton.contains(event.target) &&
        !navbarMenu.contains(event.target)
    ) {
        navbarMenu.classList.add("hidden");
    }
});

// AccountLogic
accountButton.addEventListener("click", function () {
    accountMenu.classList.toggle("hidden");
});

document.addEventListener("click", function (event) {
    if (
        !accountButton.contains(event.target) &&
        !accountMenu.contains(event.target)
    ) {
        accountMenu.classList.add("hidden");
    }
});

// Display Products in cart

const storedShoppingCart =
    JSON.parse(localStorage.getItem("shoppingCart")) || [];
let totalAmountInCart = 0;

for (let i = 0; i < storedShoppingCart.length; i++) {
    const product = storedShoppingCart[i];
    console.log(`cantidad de ${product.title} => ${product.amount}`);
    totalAmountInCart += product.amount;
}
amountProducts.textContent = totalAmountInCart;
