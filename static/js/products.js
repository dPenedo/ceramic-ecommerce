document.addEventListener("DOMContentLoaded", function () {
  const tipoDePiezaButton = document.getElementById("tipoDePiezaButton")
  const tipoDePiezaMenu = document.getElementById("tipoDePiezaMenu")

  const filtrarPorBoton = document.getElementById("filtrarPorBoton")
  const filtrarPorMenu = document.getElementById("filtrarPorMenu")

  const ordenarPorBoton = document.getElementById("ordenarPorBoton")
  const ordenarPorMenu = document.getElementById("ordenarPorMenu")



  // tipoDePiezaLogic
  tipoDePiezaButton.addEventListener("click", function () {
    tipoDePiezaMenu.classList.toggle("hidden");
  })

  document.addEventListener("click", function (event) {
    if (!tipoDePiezaButton.contains(event.target) && !tipoDePiezaMenu.contains(event.target)) {
      tipoDePiezaMenu.classList.add("hidden");
    }
  });


  // FiltroLogic
  filtrarPorBoton.addEventListener("click", function () {

    filtrarPorMenu.classList.toggle("hidden");
  })
  // OrdenarLogic
  ordenarPorBoton.addEventListener("click", function () {

    ordenarPorMenu.classList.toggle("hidden");
  })

});
