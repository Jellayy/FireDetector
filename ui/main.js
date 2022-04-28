$(document).ready(function () {
    // Handler for button press
    $('#button').click(function () {
        $("#button").prop("value", "Fire Detection Enabled");
        $("#button").prop("disabled", true);
        eel.detect_fire()();
    })

    // Fire detection handler
    var alarm = 0
    eel.expose(update_fire_status);
    function update_fire_status(value) {
        if (value && alarm === 0) {
            var audio = new Audio('alarm.mp3');
            alarm = 1;
            audio.play();
        }
        else if (value) {
            $('#fire_detection').html(`FIRE DETECTED!`);
            $('#fire_detection').css("font-weight","bold");
        }
        else {
            $('#fire_detection').html(`No Fire Detected`);
            $('#fire_detection').css("font-weight","normal");
        }
    }

    // Stovetop detection handler
    eel.expose(update_stovetop_status);
    function update_stovetop_status(value) {
        if (value) {
            $('#stovetop_detection').html('STOVETOP ON!');
            $('#stovetop_detection').css("font-weight","bold");
        }
        else {
            $('#stovetop_detection').html(`Stovetop Off`);
            $('#stovetop_detection').css("font-weight","normal");
        }
    }

})