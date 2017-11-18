(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space


$("#submit").click(function () {
    $(".error").hide();
    var valueX = $("#captcha_x").val();
    var valueY = $("#captcha_y").val();
    if (valueX != valueY) {
        alert("Каптча не совпадает");
    }
});

$(function() {
  $('input.autocomplete').autocomplete({
    data: {
        "Аллерголог-иммунолог":null,
        "Андролог":null,
        "Венеролог":null,
        "Гастроэнтеролог":null,
        "Гепатолог":null,
        "Гинеколог":null,
        "Дерматолог":null,
        "Диетолог":null,
        "Кардиолог":null,
        "Маммолог":null,
        "Мануальныйтерапевт":null,
        "Нарколог":null,
        "Невролог":null,
        "Нейрохирург":null,
        "Онколог":null,
        "Ортопед":null,
        "Отоларинголог":null,
        "Офтальмолог":null,
        "Педиатр":null,
        "Проктолог":null,
        "Психотерапевт":null,
         "Рефлексотерапевт":null,
        "Сексолог":null,
        "Терапевт":null,
        " Уролог":null,
         "Физиотерапевт":null,
        "Флеболог":null,
        "Хирург":null,
        "Эндокринолог":null,
    }
  });
});

$(function() {
  $('input.location').autocomplete({
    data: {
        "Альметьевск":null,

    }
  });
});