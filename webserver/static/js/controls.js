function send_command(command){
    $.get('/' + command, function(){
        console.log("command sent!");
    });
}

function moveForward(){
    // console.log("Moving forward");
    $('.fa-arrow-up').css('color','crimson');
    send_command('move_forward');
}

function turnLeft(){
    // console.log("Turning Left");
    $('.fa-arrow-left').css('color','crimson');
    send_command('turn_left');
}

function turnRight(){
    // console.log("Turning right");
    $('.fa-arrow-right').css('color','crimson');
    send_command('turn_right');
}

function moveBack(){
    // console.log("Moving back");
    $('.fa-arrow-down').css('color','crimson');
    send_command('move_back')
}

function resetArrowColours(){
    $('.fas').css('color','darkgray');
}

function stopRobot(){
    resetArrowColours();
    send_command('stop');
}


// Handle keypress events
document.onkeydown = function(e){
    var keyCode = e.keyCode;
    switch(keyCode){
        case 37: // left
            turnLeft()
            break
        case 38: // up
            moveForward()
            break
        case 39: // right
            turnRight()
            break
        case 40: // down
            moveBack()
            break
    }
}

document.onkeyup = function(e){
    var arrowKeyCodes = new Set([37, 38, 39, 40]);
    var keyCode = e.keyCode;

    if(arrowKeyCodes.has(keyCode)){
        // console.log("Arrow key released!")
        stopRobot();
    }
}

//on click Listeners for arrow keys
$( document ).ready(function() {
    $('.fa-arrow-up').mousedown(function(){
        moveForward();
    }).mouseup(function(){
        stopRobot();
    });

    $('.fa-arrow-left').mousedown(function(){
        turnLeft();
    }).mouseup(function(){
        stopRobot();
    });

    $('.fa-arrow-right').mousedown(function(){
        turnRight();
    }).mouseup(function(){
        stopRobot();
    });

    $('.fa-arrow-down').mousedown(function(){
        moveBack();
    }).mouseup(function(){
        stopRobot();
    });
});
