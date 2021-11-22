const classX = 'x' 
const classO = 'circle'
const winMethot = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
const cellElements = document.querySelectorAll('[data-cell]')
const board = document.getElementById('board')
const winMessageElement = document.getElementById('winMessage')
const restButton = document.getElementById('restButton')
const winMessageTextElement = document.querySelector('[data-winMsgText]')
let turnO

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
  const currentClass = turnO ? classO : classX
  placeMark(cell, currentClass)
  if (checkWin(currentClass)) {
    endGame(false)
  } else if (isDraw()) {
    endGame(true)
  } else {
    swapTurns()
    setBoardHoverClass()
  }
}

function endGame(draw) {
  if (draw) {
    winMessageTextElement.innerText = 'Berabere!'
  } else {
    winMessageTextElement.innerText = `${ turnO ? "O" : "X"} Kazandı!`
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

function swapTurns() {
  turnO = !turnO
}

function setBoardHoverClass() {
  board.classList.remove(classX)
  board.classList.remove(classO)
  if (turnO) {
    board.classList.add(classO)
  } else { board.classList.add(classX) }
}

function checkWin(currentClass) { return winMethot.some(combination => { return combination.every(index => {
      return cellElements[index].classList.contains(currentClass)
    })
  })
}