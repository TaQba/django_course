

function click(element) {
    var X = '<p class="big">X</p>';
    var O = '<p class="big">O</p>';
    if (element.innerHTML == X) {
        element.innerHTML = O;
    } else if (element.innerHTML == O) {
        element.innerHTML = '';
    } else {
        element.innerHTML = X;
    }
}

var tds = document.querySelectorAll('td');
tds.forEach(function(elem) {
    elem.addEventListener('click', function(){
        click(elem);
    });
});
