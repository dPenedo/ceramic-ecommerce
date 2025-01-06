document.addEventListener("DOMContentLoaded", function () {
  const cartButton = document.getElementById("myCartDropdownButton1");
  const dropdown = document.getElementById("myCartDropdown1");
  const burgerButton = document.getElementById("burger-button")
  const navbarMenu = document.getElementById("ecommerce-navbar-menu-1")
  const accountButton = document.getElementById("accountDropdownButton")
  const accountMenu = document.getElementById("accountMenu")

  // CartLogic
  cartButton.addEventListener("click", function () {
    // Alternar la clase 'hidden' para mostrar u ocultar el menú
    dropdown.classList.toggle("hidden");
  });
  // Cerrar el menú al hacer clic fuera
  document.addEventListener("click", function (event) {
    if (!cartButton.contains(event.target) && !dropdown.contains(event.target)) {
      dropdown.classList.add("hidden");
    }
  });

  // BurgerLogic
  burgerButton.addEventListener("click", function () {
    navbarMenu.classList.toggle("hidden");
  })

  // AccountLogic
  accountButton.addEventListener("click", function () {

    console.log("lalal")
    accountMenu.classList.toggle("hidden");
  })


});
