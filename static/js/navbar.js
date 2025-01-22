const burgerButton = document.getElementById("burger-button");
const navbarMenu = document.getElementById("ecommerce-navbar-menu-1");

const accountButton = document.getElementById("accountDropdownButton");
const accountMenu = document.getElementById("accountMenu");

const amountProducts = document.getElementById("amount-products-in-cart");

// Burger Logic
if (burgerButton && navbarMenu) {
    burgerButton.addEventListener("click", function () {
        navbarMenu.classList.toggle("hidden");
    });
}

// General click listener to close menus when clicking outside
document.addEventListener("click", function (event) {
    // Burger menu close logic
    if (
        burgerButton &&
        navbarMenu &&
        !burgerButton.contains(event.target) &&
        !navbarMenu.contains(event.target)
    ) {
        navbarMenu.classList.add("hidden");
    }

    // Account menu close logic
    if (
        accountButton &&
        accountMenu &&
        !accountButton.contains(event.target) &&
        !accountMenu.contains(event.target)
    ) {
        accountMenu.classList.add("hidden");
    }
});

// Account Logic
if (accountButton && accountMenu) {
    accountButton.addEventListener("click", function () {
        accountMenu.classList.toggle("hidden");
    });
}

// Display Products in cart
const storedShoppingCart =
    JSON.parse(localStorage.getItem("shoppingCart")) || [];
let totalAmountInCart = 0;

storedShoppingCart.forEach((product) => {
    totalAmountInCart += product.amount;
});

if (amountProducts && totalAmountInCart !== 0) {
    amountProducts.textContent = totalAmountInCart;
}
