var overlay = document.getElementById('overlay');

overlay.addEventListener('animationend', function(e) {
    setTimeout(function () {
      overlay.style.display = 'none';
    }, 400);
}, false);
