let currentVoteType = null;
let currentSuggestionId = null;

document.getElementById("modal").addEventListener("click", function (e) {
    if (e.target === this) {
        closeModal();
        currentVoteType = null;
        currentSuggestionId = null;
    }
});

function openModal(type, suggestionId, voteLabel) {
    currentVoteType = type;
    currentSuggestionId = suggestionId;

    const modalTitle = document.querySelector('.modal-title');
    modalTitle.textContent = `Вы уверены, что хотите проголосовать "${voteLabel}"? Ваш голос потом нельзя будет поменять.`;

    const approveForm = document.getElementById("approve-form");
    approveForm.action = `/suggestions/vote_${currentVoteType}/${currentSuggestionId}/`;

    document.getElementById('confirmation-modal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('confirmation-modal').style.display = 'none';
    currentVoteType = null;
    currentSuggestionId = null;
}

function confirmVote() {
    const approveForm = document.getElementById("approve-form");
    approveForm.submit(); // Submit the form
    closeModal(); 
}

function updateProgressBars(suggestionId, votesFor, votesAgainst) {
    const forBar = document.getElementById(`progressForBar${suggestionId}`);
    const forCount = document.getElementById(`forCount${suggestionId}`);
    const againstBar = document.getElementById(`progressAgainstBar${suggestionId}`);
    const againstCount = document.getElementById(`againstCount${suggestionId}`);

    forBar.style.width = `${(votesFor / maxForVotes) * 100}%`;
    forCount.textContent = `${votesFor}/${maxForVotes}`;

    againstBar.style.width = `${(votesAgainst / maxAgainstVotes) * 100}%`;
    againstCount.textContent = `${votesAgainst}/${maxAgainstVotes}`;
}