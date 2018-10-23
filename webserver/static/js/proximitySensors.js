window.setInterval(query_sensors, 500);

function query_sensors(){
    query_sensor("left")
    query_sensor("right")
    query_sensor("front")
}

function query_sensor(pos){
    $.get('/query_proximity_sensor/'+pos, function(data){
        console.log(data);
        val = data;
        if(val == 0){
            $('.proximity-' + pos).css('color','crimson');
        }else{
            $('.proximity-' + pos).css('color','darkgray');
        }
    });
}
