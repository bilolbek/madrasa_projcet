// site loader
window.onload = function () {
    document.getElementById("siteLoader").style.display = "none";
    document.getElementById("loader").style.visibility = "visible";
    $('#loader_helper').empty();
}

$(document).ready(function () {

    /*---------------------------------------------------------------- One Page Navigation ----------------------------*/
    $('.nav').onePageNav({
        filter: ':not(.external)',
        scrollThreshold: 0.25,
        scrollOffset: 0,
    });

    /*---------------------------------------------------------------- Fixed menu ----------------------------*/
    $('header').scrollToFixed();


    /*---------------------------------------------------------------- animation1 ----------------------------*/
    $('.features .item').hover(function () {
        $(this).addClass('animated pulse')
    }, function () {
        $(this).removeClass('animated pulse')
    });

    $('.table .table-list').hover(function () {
        $(this).addClass('animated tada')
    }, function () {
        $(this).removeClass('animated tada')
    });


    /*---------------------------------------------------------------- Video ----------------------------*/
    $(".player").mb_YTPlayer();


    /*--------------------------------------------------------------------------- Tooltip-------------------------------*/
    $('.tooltips').tooltip();


    /*--------------------------------------------------------------- Responsive Video plugin ------------------*/
    $(".video").fitVids();


    /*--------------------------------------------------------------------------- ToTop -------------------------*/
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });

    $('.scrollup').click(function () {
        $("html, body").animate({scrollTop: 0}, 3000);
        return false;
    });


    $('.n1').click(function () {
        $("html, body").animate({scrollTop: 0}, 3000);
        return false;
    });


    /*----------------------------------------------------- contact Form -------------------------*/
    $("#request").submit(function () {
        $('#request').find('[type="submit"]').attr('disabled', 'disabled');
        var oData = $('#request').serialize();
        var name = $('#request').find('[name="name"]').val();
        var phone = $('#request').find('[name="phone"]').val();
        var address = $('#request').find(' [name="address"] ').val();

        if (name == '' || phone == '' || address == '') {
            alert("Заполните все поля")
             $('#request').find('[type="submit"]').removeAttr('disabled');
        } else {
            $.ajax({
                type: 'POST',
                url: '/',
                dataType: 'json',
                data: oData,
                success: function () {
                    $('#request').find('[name="name"]').val("");
                    $('#request').find(' [name="phone"]').val("");
                    $('#request').find('[name="adress"]').val("");
                    $('#request').find('[type="submit"]').removeAttr('disabled');
                }
            })
        }
        return false;
    });

    /*---------------------------------------------------------------- Cta Button Set Interval ----------------------------*/
    setInterval(function () {
        $('.cta a').toggleClass('animated shake')
    }, 2000);


});


 
