
$(document).ready(function () {
    $('.timepicker').timepicker({
        timeFormat: 'h:mm p',
        interval: 30,
        minTime: '01:00',
        maxTime: '11:59 pm',
        defaultTime: '12:00 am',
        startTime: '12:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});