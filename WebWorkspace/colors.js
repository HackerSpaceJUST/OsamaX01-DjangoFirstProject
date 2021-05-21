document.addEventListener('DOMContentLoaded', function() {

    // document.querySelectorAll('button').forEach(function(button) {
    //     button.onclick = function() {
    //         document.querySelector('#choose').style.color = button.dataset.color;
    //     }
    // });

    document.querySelector('select').onchange = function() {
        document.querySelector('#choose').style.color = this.value;
    };
});