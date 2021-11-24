const classX = 'x'
const classO = 'o'
const mainPanel = [
  [0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0]
]

const winMethot = [
  [0, 1, 2],
  [5, 6, 7],
  [10, 11, 12],
  [0, 5, 10],
  [1, 6, 11],
  [2, 7, 12],
  [0, 6, 12],
  [2, 6, 10],
]
const cellElements = document.querySelectorAll('[data-cell]')
const board = document.getElementById('board')
const winMessageElement = document.getElementById('winMessage')
const restButton = document.getElementById('restButton')
const xChoose = document.getElementById('xChoose')
const oChoose = document.getElementById('oChoose')
const winMessageTextElement = document.querySelector('[data-winMsgText]')
var choose = 0
let turnO

function chooseOne() {
   chooseTextElement.innerText = 'Seçim Yapın'
    xChoose.addEventListener('click', choosingX)
    oChoose.addEventListener('click', choosingO)

}

function choosingX() {
  choose = 1;
  startGame()
  chooseElement.classList.remove('show')
}
function choosingO() {
  startGame()
  choose = 2
  chooseElement.classList.remove('show')
}
startGame()


restButton.addEventListener('click', startGame)

function startGame() {
  turnO = false
  cellElements.forEach(cell => {
    cell.classList.remove(classX)
    cell.classList.remove(classO)
    cell.removeEventListener('click', handleClick)
    cell.addEventListener('click', handleClick, { once: true })
  })
  setBoardHoverClass()
  winMessageElement.classList.remove('show')
}

function handleClick(e) {
  const cell = e.target
  const currentClass = classX
  //var cellArray = Array.from(document.querySelectorAll('.cell')); //this code writes the cell name to the array. like div.cell.x div.cell.o or div.cell
  placeMark(cell, currentClass)
  responseAi()
  if (checkWin(currentClass)) {
    endGame(false)
  } else if (isDraw()) {
    endGame(true)
  } else {
    setBoardHoverClass()
  }
}

function endGame(draw) {
  if (draw) {
    winMessageTextElement.innerText = 'Berabere!'
  } else {
    winMessageTextElement.innerText = `${turnO ? "O" : "X"} Kazandı!`
  }
  winMessageElement.classList.add('show')
}

function isDraw() {
  return [...cellElements].every(cell => {
    return cell.classList.contains(classX) || cell.classList.contains(classO)
  })
}

function placeMark(cell, currentClass) {
  cell.classList.add(currentClass)
}

function setBoardHoverClass() {
  board.classList.remove(classX)
  board.classList.remove(classO)
  if (turnO) {
    board.classList.add(classO)
  } else { board.classList.add(classX) }
}

function checkWin(currentClass) {
  return winMethot.some(combination => {
    return combination.every(index => {
      return cellElements[index].classList.contains(currentClass)
    })
  })
}

function postButtonVal(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); //Keep this false for discouraged synchronous request. Or don't.
    xmlHttp.send(null);
    return xmlHttp.responseText;
    console.log(xmlHttp.responseText)
}

function updateBoard(id) {
  document.getElementById('result').innerText = postButtonVal('/get?board='+id);
}

function responseAi() {
  const currentClass = classO;
  var response = 5;
  const cellAi = document.getElementById(response)
  cellAi.classList.add(currentClass)
}