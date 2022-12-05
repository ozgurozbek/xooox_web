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
  console.log("Responding for AI turn "+aiTurn+"...");
  mainPanel = postButtonVal('/get?board='+mainPanel.toString()+'&aiTurn='+aiTurn).slice(1,-2).split(",")
  placeValuesOnBoard();
  if (firstTurn) {
    firstTurn = false;
    updateBoard()
  }
  console.log("Done.");
  aiTurn += 1;
}

function placeValuesOnBoard(){
  for (let index = 0; index < 25; index++) {
    if (mainPanel[index] == 0) {
      value = "-"
    } else if (mainPanel[index] == 1) {
      value = "O";
      document.getElementById(index).removeAttribute("onclick");
    } else if (mainPanel[index] == 2) {
      value = "X";
      document.getElementById(index).removeAttribute("onclick");
    };
    document.getElementById(index).innerText = value;
  }

  getScoreInfo();
}

function getScoreInfo(){
  console.log(mainPanel.toString());
  console.log("Getting Score...");
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
  console.log("Done.");
}