;

"use strict";

var loadCallback = function () {
    
    var div = document.getElementById('clock')
    if (!div) {
        div = document.createElement('DIV');
        div.id = 'clock';
        document.body.appendChild(div);
    }
    div.innerHTML = new Date();

    setTimeout(loadCallback, 1000);
};

if (window.addEventListener) {
    window.addEventListener('load', loadCallback, false);
} else if (window.attachEvent) {
    window.attachEvent('onload', loadCallback);
} else {
        window.onload = loadCallback;
}



