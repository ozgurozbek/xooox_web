// x = 2
// o = 1
// empty = 0
var mainPanel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
var firstTurn = true;
var aiTurn = 0
const result = document.getElementById('result')

var xmlHttp = new XMLHttpRequest();

function postButtonVal(theUrl) {
  xmlHttp.open("GET", theUrl, false); //Keep this false for discouraged synchronous request. Or don't.
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

function updateBoard(id) {
  mainPanel[id] = 2;
  console.log(mainPanel.toString());
  result.innerText = "AI is thinking for turn "+aiTurn+". Please wait...";
  aiDiff = document.getElementById("difficultySelect").value
  aiDepth = document.getElementById("depthSelect").value
  mainPanel = postButtonVal('/get?board='+mainPanel.toString()+'&aiTurn='+aiTurn+'&aiDiff='+aiDiff+'&aiDepth='+aiDepth).slice(1,-2).split(",")
  placeValuesOnBoard();
  if (firstTurn) {
    firstTurn = false;
    updateBoard()
  }
  console.log("Board updated.");
  aiTurn += 1;
}

function placeValuesOnBoard(){
  for (let index = 0; index < 25; index++) {
    if (mainPanel[index] == 1) {
      document.getElementById("o"+index).style.display = 'block';
      document.getElementById(index).removeAttribute("onclick");
    } else if (mainPanel[index] == 2) {
      document.getElementById("x"+index).style.display = 'block';
      document.getElementById(index).removeAttribute("onclick");
    };
  }

  getScoreInfo();
}

function getScoreInfo(){
  console.log(mainPanel.toString());
  result.innerText = "Getting Score...";
  output = postButtonVal('/get_result?board=' + mainPanel.toString()).slice(1,-2).split(",");
  result.innerText = "X > "+output[0]+" with "+output[2]+" tiles\nO > "+output[1]+" with "+output[3]+" tiles.";
  winner = ""

  if (mainPanel.filter(x => x == 0).length == 0){
    if (output[0]>output[1]) {
      winner="X wins!"
    } else if (output[0]==output[1]) {
      if (output[2]>output[3]) {
        winner="X wins!"
      } else if (output[2]==output[3]) {
        winner="It is a Draw!"
      } else {
        winner="O wins!"
      }
    } else {
      winner="O wins!"
    }
    result.innerText = "X > "+output[0]+" with "+output[2]+" tiles\nO > "+output[1]+" with "+output[3]+" tiles.\n"+winner+" Thank you for playing!";
  }
  console.log("Score updated.");
}