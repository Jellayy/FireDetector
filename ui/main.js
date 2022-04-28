$(document).ready(function () {
    $('#button').click(function () {
        eel.detect_fire()();
    })

    var alarm = 0
    eel.expose(say_words);
    function say_words(value) {
        $('#words').html(`${value}`);
        if (value === "dear sir stroke madam FIRE EXCLAMATION MARK" && alarm === 0) {
            var audio = new Audio('alarm.mp3');
            alarm = 1;
            audio.play();
        }
    }

})