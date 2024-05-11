function updateTime() {
    
    var currentTimeUTC = new Date().toUTCString();
    var currentTimeLocal = new Date().toLocaleString();

    document.getElementById('GMT time').textContent = currentTimeUTC;
    document.getElementById('local time').textContent = currentTimeLocal;
}

updateTime();

setInterval(updateTime, 1000);