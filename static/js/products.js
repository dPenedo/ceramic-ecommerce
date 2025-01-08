document.addEventListener("DOMContentLoaded", function () {
  const tipoDePiezaButton = document.getElementById("tipoDePiezaButton")
  const tipoDePiezaMenu = document.getElementById("tipoDePiezaMenu")

  // tipoDePiezaLogic
  tipoDePiezaButton.addEventListener("click", function () {
    tipoDePiezaMenu.classList.toggle("hidden");
  })

  document.addEventListener("click", function (event) {
    if (!tipoDePiezaButton.contains(event.target) && !tipoDePiezaMenu.contains(event.target)) {
      tipoDePiezaMenu.classList.add("hidden");
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

});
