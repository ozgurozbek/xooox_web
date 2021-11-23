const getBtn = document.getElementById('get-btn');


const getData = () => {
    const xhr = new XMLHttpRequest()
    xhr.open('GET', 'http://xeculus.pythonanywhere.com/generate')

    xhr.responseType = "json"

    xhr.onload = () => {
        const data = xhr.response
        console.log(data)
    };

    xhr.send();

}

const sendData = () => { }

getBtn.addEventListener('click', getData);