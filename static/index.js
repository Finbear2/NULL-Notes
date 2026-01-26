const searchInput = document.getElementById("search");
const cards = document.querySelectorAll(".note-card");

searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase();

    cards.forEach(element => {
        const text = element.textContent.toLowerCase();
        element.style.display = text.includes(query) ? "" : "none";
    });
})

cards.forEach(card => {
    card.addEventListener("click", () => {
        const hiddenText = card.dataset.hiddenText;
        window.location.href = `/edit/${hiddenText}/`;
    })
})