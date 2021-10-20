$(document).ready(function () {
    // On Click Of The Submit Button Call The Function To Generate New Be Like Bill
    $(".btn-sub").click(function () {
        generate_belike();
    });

    // Function Responsible For Gettin User Input Values And Refereshing The Page Content With Update Content 
    function generate_belike() {
        var name = $('#name').val();
        var gender = $('#gender').val();
        csrf = $('input[name="csrfmiddlewaretoken"]').val()

        $.ajax({
            url: "http://127.0.0.1:8000/",
            type: "POST",
            dataType: "json",
            data: {
                'name': name,
                'gender': gender,
                'csrfmiddlewaretoken': csrf
            },
            success: function (data) {
                url = 'https://belikebill.ga/billgen-API.php?default=1&name=' + data.name + '&sex=' + data.gender;
                $("#srcapi").attr('src', url);
            }
        });
    };

    // To Add Active Class On Nav Item 
    var path = location.pathname.split("/")[1];
    if (path != "") {
        $('nav a[href^="/' + location, pathname.split("/")[1] + '"]').addClass('active');
    } else {
        $('nav a[href="/"').addClass('active');
    }
});