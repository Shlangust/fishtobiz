document.addEventListener("DOMContentLoaded", function() {
    const popupOverlay = document.getElementById("popupOverlay");
    const openPopupButton = document.querySelector("become-client-button");
    const closePopupButton = popupOverlay.querySelector("close-button");

    // Открыть всплывающее окно
    openPopupButton.addEventListener("click", () => {
        popupOverlay.classList.add("active");
    });

    // Закрыть всплывающее окно
    closePopupButton.addEventListener("click", () => {
        popupOverlay.classList.remove("active");
    });

    // Закрыть всплывающее окно при клике вне окна
    popupOverlay.addEventListener("click", (event) => {
        if (event.target === popupOverlay) {
            popupOverlay.classList.remove("active");
        }
    });
});