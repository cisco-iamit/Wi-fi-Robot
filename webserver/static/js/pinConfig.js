function submitPins(){
  console.log("here")
  var pin_settings = {
    left_motor_1 : $('#left_motor_1').val(),
    left_motor_2 : $('#left_motor_2').val(),
    right_motor_1 : $('#right_motor_1').val(),
    right_motor_2 : $('#right_motor_2').val()
  }

  $.post("/set_pins", pin_settings, function(response){
    console.log(response);
    getPins();
  });
}

function getPins(){
  $.get('/get_pins', function(pins){
    console.log(pins);
    var pin_config = JSON.parse(pins);
    console.log(pin_config['left_motor_1']);

    $('#left_motor_1').val(pin_config['left_motor_pin_1'])
    $('#left_motor_2').val(pin_config['left_motor_pin_2'])
    $('#right_motor_1').val(pin_config['right_motor_pin_1'])
    $('#right_motor_2').val(pin_config['right_motor_pin_2'])

  });
}

$( document ).ready(function() {
  getPins();
  $('#pin-submit').click(submitPins);
});
