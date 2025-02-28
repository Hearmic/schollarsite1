let currentVoteType = null;
let currentSuggestionId = null;

document.getElementById("modal").addEventListener("click", function (e) {
    if (e.target === this) {
        closeModal();
        currentVoteType = null;
        currentSuggestionId = null;
    }
});

function openModal(suggestionElement) {
    const suggestionId = suggestionElement.dataset.id;
    const title = suggestionElement.querySelector('.suggestion-title').textContent;
    const description = suggestionElement.querySelector('.suggestion-description').textContent;
    const votesFor = parseInt(suggestionElement.querySelector('.suggestion-votes-for').textContent);
    const votesAgainst = parseInt(suggestionElement.querySelector('.suggestion-votes-against').textContent);

    document.getElementById('suggestionTitle').textContent = title;
    document.getElementById('suggestionDescription').textContent = description;
    document.getElementById('suggestionVotesFor').textContent = votesFor;
    document.getElementById('suggestionVotesAgainst').textContent = votesAgainst;

    document.getElementById('progressForBar').style.width = `${(votesFor / maxForVotes) * 100}%`;
    document.getElementById('progressAgainstBar').style.width = `${(votesAgainst / maxAgainstVotes) * 100}%`;
}

function openConfirmModal(type, suggestionId, voteLabel) {
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