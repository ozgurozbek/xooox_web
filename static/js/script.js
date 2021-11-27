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
const chooseElement = document.getElementById('choose')
const restButton = document.getElementById('restButton')
const result = document.getElementById('result')
const xChoose = document.getElementById('xChoose')
const oChoose = document.getElementById('oChoose')
const loader = document.getElementById('timeout')

const winMessageTextElement = document.querySelector('[data-winMsgText]')
const chooseTextElement = document.querySelector('[data-chooseText]')
var choosen = 0
let turnO
var xmlHttp = new XMLHttpRequest();

chooseOne()

function chooseOne() {
  chooseTextElement.innerText = 'Seçim Yapın'
  xChoose.addEventListener('click', choosingX)
  oChoose.addEventListener('click', choosingO)

}

function choosingX() {
  choosen = 1;
  choose.style.display = "none";
  startGame()
  console.log(choosen)
}
function choosingO() {
  choosen = 2
  choose.style.display = "none";
  startGame()
  console.log(choosen)
}



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

function postButtonVal(theUrl) {
  xmlHttp.open("GET", theUrl, false); //Keep this false for discouraged synchronous request. Or don't.
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

function updateBoard(id) {
  loader.style.display = "flex";
  const currentClass = classO;
  const response = postButtonVal('/get?board=' + id);
  const cellAi = document.getElementById(response)
  cellAi.classList.add(currentClass)
  //loader.style.display = "none";
}


