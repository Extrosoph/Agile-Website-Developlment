$(document).ready(function() {

    //Function to show and hide password
    const password = $('#passwordInput') ;
    $('#eye').click(function(){
        if(password.prop('type') == 'password'){
            $(this).addClass('fa-eye-slash');
            password.attr('type','text')
        }
        else {
            $(this).removeClass('fa-eye-slash');
            password.attr('type','password');
        }
    })

    var href = document.location.href;
    var lastPathSegment = href.substr(href.lastIndexOf('/') + 1);

    //Check if forms are empty depending on the page
    if(lastPathSegment == 'login') {
        //Cool function to add later
        $('#forget-password').click(function() {
            $('h1').text("Forget Password");
            $('#password').remove();
            $('#login').remove();
            $('#forget-password').remove();
            $('#signup').remove();
            $('#myform').append('<button type="submit" id="Verify" class="button">Verify</button>')
        })

        $('#login').click(function() {
            if ($('#email').val().length === 0 || $('#passwordInput').val().length === 0) {
                alert('Need to fill all fields!');
                return false;
            }
        })
    }

    else {
        $('#signup').click(function() {
            if ($('#email').val().length === 0 || $('#passwordInput').val().length === 0 || $('#username').val().length === 0) {
                alert('Need to fill all fields!');
                return false;
            }
        })
    }

})