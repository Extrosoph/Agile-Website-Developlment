$(document).ready(function() {
    var href = document.location.href;
    var lastPathSegment = href.substr(href.lastIndexOf('/') + 1);

    //Check what page it is on
    if(lastPathSegment == 'login' || lastPathSegment == 'signup') {

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
                    alert('Need to fill all fields!')
                    return false;
                }
            })
        }

        else {
            $('#signup').click(function() {
                if ($('#email').val().length === 0 || $('#passwordInput').val().length === 0 || $('#username').val().length === 0) {
                    alert('Need to fill all fields!')
                    return false;
                }

                // Password checking for stronger password
                if ($('#passwordInput').val().length < 7) {
                    alert('Password requires at least 8 characters!')
                    return false;
                }

                if ($('#passwordInput').val().search('/[a-z]/') < 1) {
                    alert('Password requires lowercase characters!')
                    return false;
                }

                if ($('#passwordInput').val().search('/[A-Z]/') < 1) {
                    alert('Password requires uppercase characters!')
                    return false;
                }

                if ($('#passwordInput').val().search('/[0-9]/') < 1) {
                    alert('Password requires numbers!')
                    return false;
                }
            })
        }
    }

    $('#sb').click(function(){
        $('#sb').hide();
        $('#abase').show();
        $('#but').show();
    })

    $('#next').click(function(){
        // NextPage function
        if($('#abase').css('display') !== 'hidden'){
            $('#abase').hide();
        }
    })

    $('#prev').click(function(){
        // PrevPage function
    })
})

