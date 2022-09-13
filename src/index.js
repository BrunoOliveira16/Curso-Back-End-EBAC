
function titleComponent(){
    const elemH1 = document.createElement('h1')
    elemH1.innerHTML = 'Hello World'
    return elemH1
}

document.body.appendChild(titleComponent())