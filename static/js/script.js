// x = 2
// o = 1
// empty = 0
var mainPanel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
var fisrtTurn = true;
const result = document.getElementById('result')
const loader = document.getElementById('loading_gif')

var xmlHttp = new XMLHttpRequest();

function postButtonVal(theUrl) {
  xmlHttp.open("GET", theUrl, false); //Keep this false for discouraged synchronous request. Or don't.
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

function updateBoard(id) {
  mainPanel[id] = 2;
  console.log(mainPanel.toString());
  console.log("Responding...");
  mainPanel = postButtonVal('/get?board=' + mainPanel.toString()).slice(1,-2).split(",");
  //result.innerText=mainPanel;
  placeValuesOnBoard();
  if (fisrtTurn) {
    fisrtTurn = false;
    updateBoard()
  }
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
}