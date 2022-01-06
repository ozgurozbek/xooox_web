const classX = 'x'
const classO = 'o'
const mainPanel = [
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,    
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0,
  0, 0, 0, 0, 0]

const board = document.getElementById('board')
const result = document.getElementById('result')
const loader = document.getElementById('timeout')

var xmlHttp = new XMLHttpRequest();

function postButtonVal(theUrl) {
  xmlHttp.open("GET", theUrl, false); //Keep this false for discouraged synchronous request. Or don't.
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

function updateBoard(id) {
  loader.style.display = "flex";
  mainPanel[id]= "x";
  console.log(mainPanel)
  // const response = postButtonVal('/get?board=' + id); 
}


