document.getElementById("modal").addEventListener("click", function (e) {
    if (e.target === this) {
        this.style.display = "none";
    }
});

function openModal(noteElement) {
    // Extract data from the clicked note
    const noteId = noteElement.dataset.id;
    const noteTitle = noteElement.dataset.title;
    const noteDescription = noteElement.dataset.description;
    const noteDate = noteElement.dataset.date;
    const parentApproved = noteElement.dataset.parentApproved === "true";
    const teacherApproved = noteElement.dataset.teacherApproved === "true";
    const qrCodeImage = document.getElementById("modal-qr-code");

    // Populate modal fields
    document.getElementById("modal-note-title").textContent = noteTitle;
    document.getElementById("modal-note-date").textContent = `Создана: ${noteDate}`;
    document.getElementById("modal-title").value = noteTitle;
    document.getElementById("modal-description").value = noteDescription;

    // Toggle form visibility based on approval statuses
    const parentForm = document.getElementById("parent-approve-form");
    const teacherForm = document.getElementById("teacher-approve-form");
    const denyForm = document.getElementById("deny-form");

    if (qrCodeImage) {
        if (parentApproved && teacherApproved) {
            qrCodeImage.style.display = "block"; // Показываем QR-код
            qrCodeImage.src = `/exit_notes/qr_code/${noteId}/`;
        } else {
            qrCodeImage.style.display = "none"; // Скрываем QR-код
        }
    }

    if (parentForm) {
        parentForm.style.display = parentApproved ? "none" : "block";
        parentForm.action = `/exit_notes/${noteId}/parent_approve/`;
    }

    if (teacherForm) {
        teacherForm.style.display = teacherApproved ? "none" : "block";
        teacherForm.action = `/exit_notes/${noteId}/teacher_approve/`;
    }

    if (denyForm) {
        denyForm.style.display = "block";
        denyForm.action = `/exit_notes/${noteId}/deny/`;
    }

    // Show the modal
    document.getElementById("modal").style.display = "flex";
}

function updateCounter() {
    const input = document.getElementById("note-title");
    const counter = document.getElementById("title-counter");
    counter.textContent = `${input.value.length}/15`;
}
