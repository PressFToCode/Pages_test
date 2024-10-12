document.getElementById('get-fact-button').addEventListener('click', function() {
    const factContainer = document.getElementById('fact-container');
    const factText = document.getElementById('fact');
    const catImage = document.getElementById('cat-image');
    const loader = document.getElementById('loader');

    loader.style.display = "block";
    factText.textContent = "Загрузка факта...";
    catImage.style.display = "none";

    fetch('/get_fact')
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при получении факта.');
            }
            return response.json();
        })
        .then(data => {
            return fetch(`/translate?text=${encodeURIComponent(data.fact)}`);
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при переводе факта.');
            }
            return response.json();
        })
        .then(translatedData => {
            factText.textContent = translatedData.translatedText;
            return fetch('/get_cat_image');
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при получении изображения.');
            }
            return response.json();
        })
        .then(imageData => {
            catImage.src = imageData.image_url;
            catImage.style.display = "block";
        })
        .catch(error => {
            factText.textContent = 'Ошибка: ' + error.message;
        })
        .finally(() => {
            // Скрыть загрузчик после завершения всех операций
            loader.style.display = "none";
        });
});
