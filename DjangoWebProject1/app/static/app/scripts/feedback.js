document.addEventListener("DOMContentLoaded", function () {
    // �������� �������� �����
    const submitButton = document.getElementById("submitButton");
    const inputs = document.querySelectorAll("input");
    const textArea = document.querySelectorAll("textArea");

    // ��������� ����������� ������� ��� ������
    if (submitButton) { // ���� ������ ������ ��������� null �������� �� ���� �������� ����� - �������� �����
        submitButton.addEventListener("mouseover", function () {
            this.style.color = "red";
        });
    }

    if (submitButton) { // ���� ������ ������ ��������� null �������� �� ���� �������� ����� - �������� �����
        submitButton.addEventListener("mouseout", function () {
            this.style.color = ""; // �������������� ��������� �����
        });
    }

    // ��������� ����������� ������� ��� ����� �����
    inputs.forEach(input => {
        input.addEventListener("focus", function () {
            this.style.backgroundColor = "lightblue";
        });

        input.addEventListener("blur", function () {
            this.style.backgroundColor = ""; // �������������� ��������� �����
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
