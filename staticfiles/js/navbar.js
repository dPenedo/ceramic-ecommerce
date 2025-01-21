  const burgerButton = document.getElementById("burger-button")
  const navbarMenu = document.getElementById("ecommerce-navbar-menu-1")

  const accountButton = document.getElementById("accountDropdownButton")
  const accountMenu = document.getElementById("accountMenu")

  // BurgerLogic
  burgerButton.addEventListener("click", function () {
    navbarMenu.classList.toggle("hidden");
  })

  document.addEventListener("click", function (event) {
    if (!burgerButton.contains(event.target) && !navbarMenu.contains(event.target)) {
      navbarMenu.classList.add("hidden");
    }
  });


  // AccountLogic
  accountButton.addEventListener("click", function () {

    accountMenu.classList.toggle("hidden");
  })

  document.addEventListener("click", function (event) {
    if (!accountButton.contains(event.target) && !accountMenu.contains(event.target)) {
      accountMenu.classList.add("hidden");
    }
  });
