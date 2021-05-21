if(!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    let cnt = localStorage.getItem('counter');
    document.querySelector('h1').innerHTML = ++cnt;
    localStorage.setItem('counter', cnt);
    if(cnt % 10 === 0) alert(`The Count is now ${cnt}`);
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
    // setInterval(count, 1000);
});