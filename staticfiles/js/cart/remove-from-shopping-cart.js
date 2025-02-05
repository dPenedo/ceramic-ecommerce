if (!isAuthenticated) {
    const removeButtons = document.querySelectorAll(".remove-from-cart");

    removeButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-id");
            removeProduct(productId);
        });
    });

    function removeProduct(id) {
        console.log(id);
    }
}
