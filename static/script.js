document.addEventListener('DOMContentLoaded', function () {
    const openPopupButton = document.getElementById('open-popup');
    const closePopupButton = document.getElementById('close-popup');
    const popup = document.getElementById('popup');

    if (openPopupButton && closePopupButton && popup) { // Проверяем, что элементы существуют
        openPopupButton.addEventListener('click', function () {
            popup.style.display = 'block';
        });

        closePopupButton.addEventListener('click', function () {
            popup.style.display = 'none';
        });

        window.addEventListener('click', function (event) {
            if (event.target === popup) {
                popup.style.display = 'none';
            }
        });
    } else {
        console.error("Одни или несколько элементов не найдены в DOM.");
    }
});