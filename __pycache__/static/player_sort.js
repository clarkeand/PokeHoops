function sortTeam(evt) {
    fetch('/sortTeam')
        .then((response) => response.text())
        .then(replaceFortune);
    }

document.querySelector('#sortTeam').addEventListener('click', showFortune);

function sortPosition(evt) {
    fetch('/sortPosition')
        .then((response) => response.text())
        .then(replaceFortune);
    }

document.querySelector('#sortPosition').addEventListener('click', showFortune); 
          
function sortPOKED(evt) {
    fetch('/sortPOKED')
      .then((response) => response.text())
      .then(replaceFortune);
    }

document.querySelector('#sortPOKED').addEventListener('click', showFortune);    