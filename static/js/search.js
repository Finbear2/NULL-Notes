const searchInput = document.getElementById("search");
const cards = document.querySelectorAll(".note-card");

searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase();

    cards.forEach(element => {
        const text = element.textContent.toLowerCase();
        element.style.display = text.includes(query) ? "" : "none";
    });
})