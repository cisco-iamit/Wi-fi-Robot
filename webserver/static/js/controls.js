function moveForward(){
    // console.log("Moving forward");
    $('.fa-arrow-up').css('color','crimson');
}

function turnLeft(){
    // console.log("Turning Left");
    $('.fa-arrow-left').css('color','crimson');
}

function turnRight(){
    // console.log("Turning right");
    $('.fa-arrow-right').css('color','crimson');
}

function moveBack(){
    // console.log("Moving back");
    $('.fa-arrow-down').css('color','crimson');
}

function resetArrowColours(){
    $('.fas').css('color','darkgray');
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
        resetArrowColours();
    }
}

//on click Listeners for arrow keys
$( document ).ready(function() {
    $('.fa-arrow-up').mousedown(function(){
        moveForward();
    }).mouseup(function(){
        resetArrowColours();
    });

    $('.fa-arrow-left').mousedown(function(){
        turnLeft();
    }).mouseup(function(){
        resetArrowColours();
    });

    $('.fa-arrow-right').mousedown(function(){
        turnRight();
    }).mouseup(function(){
        resetArrowColours();
    });

    $('.fa-arrow-down').mousedown(function(){
        moveBack();
    }).mouseup(function(){
        resetArrowColours();
    });
});
