const cards = document.querySelectorAll(".competency-card");
const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modalTitle");
const closeModal = document.getElementById("closeModal");

cards.forEach(card => {
    card.addEventListener("click", () => {
        modalTitle.innerText = card.dataset.competency;
        modal.classList.remove("hidden");
    });
});

if (closeModal) {
    closeModal.addEventListener("click", () => {
        modal.classList.add("hidden");
    });
}

const adminForm = document.getElementById("adminForm");
if (adminForm) {
    adminForm.addEventListener("submit", (e) => {
        const inputs = adminForm.querySelectorAll("input");

        for (let input of inputs) {
            if (!input.value.trim()) {
                alert("All leadership fields are required.");
                e.preventDefault();
                return;
            }
        }
    });
}
