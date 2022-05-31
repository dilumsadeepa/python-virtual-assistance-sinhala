var canvas = document.getElementById('mycanvas');
var ctx = canvas.getContext('2d');
ctx.lineWidth = 13;
ctx.lineCap = 'round';
ctx.shadowBlur = 45;
ctx.shadowColor = "#4EC9F2"

function degToRad(degrees){
    return degrees*Math.PI/180;
}


function getTime() {
    var now = new Date();
    var time = now.toLocaleTimeString();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    var milliseconds = now.getMilliseconds();
    var newSeconds = seconds+(milliseconds/1000);
    var month = new Array();
        month[0] = "January";
        month[1] = "February";
        month[2] = "March";
        month[3] = "April";
        month[4] = "May";
        month[5] = "June";
        month[6] = "July";
        month[7] = "August";
        month[8] = "September";
        month[9] = "October";
        month[10] = "November";
        month[11] = "December";
    var months = month[now.getMonth()];
    var days = now.getDate();
    var year = now.getYear() + 1900;


    //Background
    var gradient = ctx.createRadialGradient(250,250,5,250,250,250);
    gradient.addColorStop(0, '#09303a');
    gradient.addColorStop(1, 'black');
    ctx.fillStyle = gradient;
    ctx.fillRect(0,0,500,500);

    //Hours / eyeball
    ctx.beginPath();
    ctx.arc(182, 180, 1, degToRad(270), degToRad(hours*30-90));
    ctx.stroke();

    //Minutes / faceshape
    ctx.beginPath();
    ctx.arc(250, 230, 200, degToRad(270), degToRad(minutes*3-360));
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(322, 180, 1, degToRad(270), degToRad(minutes*3-360));
    ctx.stroke();

    //Seconds / happyface
    ctx.beginPath();
    ctx.arc(250, 270, 110, degToRad(0), degToRad(newSeconds*3-360));
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(180, 180, 40, degToRad(180), degToRad(newSeconds*3-180));
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(320, 180, 40, degToRad(180), degToRad(newSeconds*3-180));
    ctx.stroke();

    // body stroke
    ctx.beginPath();
    ctx.moveTo(250, 450);
    ctx.lineTo(250, 500);
    ctx.strokeStyle = '#77F24E'
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(230, 450);
    ctx.lineTo(200, 470);
        // animation for hand movement
        if ( seconds % 2 ) {
            ctx.lineTo(150, 430);
        } else {
        ctx.lineTo(150, 490);
        }
    ctx.strokeStyle = '#C94EF2';
    ctx.lineJoin = 'round';
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(270, 450);
    ctx.lineTo(300, 470);
        // animation for hand movement
        if ( seconds % 2 ) {
            ctx.lineTo(350, 490);
        } else {
        ctx.lineTo(350, 430);
        }
    ctx.lineJoin = 'round';
    ctx.stroke();

    // face blinking
    if ( seconds % 2 ) {
        ctx.strokeStyle = "#000"
    } else {
        ctx.strokeStyle = '#4EC9F2'
    }

    // fill date and clock
    ctx.font = '19px Orbitron';
    ctx.fillStyle = '#4EC9F2';
    ctx.fillText(months, 190, 220);
    ctx.fillText(days, 280, 240);
    ctx.fillText(year, 260, 260);
    ctx.font = '23px Orbitron';
    ctx.fillText(time, 180, 300);

    var dataURL = canvas.toDataURL();

    document.getElementById('myImage').src = dataURL;

}

setInterval(getTime, 40);
