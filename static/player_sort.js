function replacePlayers(results) {
    let playersList = document.querySelector('#players_list');
    playersList.innerHTML = ''; // Clear the existing content

    // Loop through the results and generate the HTML for each player
    results.forEach(player => {
        let playerItem = document.createElement('li');
        let playerLink = document.createElement('a');
        playerLink.href = `/players/${player.player_id}`;
        playerLink.textContent = `${player.player_name} | ${player.team_id} | ${player.player_position} | ${player.poked_score}`;
        playerLink.classList.add('link-danger');
        playerItem.appendChild(playerLink);
        playersList.appendChild(playerItem);
    });
}

function sortTeam(evt) {
    fetch('/sortTeam')
        .then(response => response.json())
        .then(replacePlayers);
}
document.querySelector('#sortTeam').addEventListener('click', sortTeam);

function sortPosition(evt) {
    fetch('/sortPosition')
        .then(response => response.json())
        .then(replacePlayers);
}

document.querySelector('#sortPosition').addEventListener('click', sortPosition); 

function sortPOKED(evt) {
    fetch('/sortPOKED')
        .then(response => response.json())
        .then(replacePlayers);
}

document.querySelector('#sortPOKED').addEventListener('click', sortPOKED);