document.addEventListener("DOMContentLoaded", function () {
    // Получаем элементы формы
    const submitButton = document.getElementById("submitButton");
    const inputs = document.querySelectorAll("input");
    const textArea = document.querySelectorAll("textArea");

    // Добавляем обработчики событий для кнопки
    if (submitButton) { // Фикс ошибки нельзя прочитать null значение на всех вкладках кроме - Обратная связь
        submitButton.addEventListener("mouseover", function () {
            this.style.color = "red";
        });
    }

    if (submitButton) { // Фикс ошибки нельзя прочитать null значение на всех вкладках кроме - Обратная связь
        submitButton.addEventListener("mouseout", function () {
            this.style.color = ""; // Восстановление исходного цвета
        });
    }

    // Добавляем обработчики событий для полей ввода
    inputs.forEach(input => {
        input.addEventListener("focus", function () {
            this.style.backgroundColor = "lightblue";
        });

        input.addEventListener("blur", function () {
            this.style.backgroundColor = ""; // Восстановление исходного цвета
        });
    });

    textArea.forEach(textArea => {
        textArea.addEventListener("focus", function () {
            this.style.backgroundColor = "lightblue";
        });

        textArea.addEventListener("blur", function () {
            this.style.backgroundColor = "";
        });
    });
});
