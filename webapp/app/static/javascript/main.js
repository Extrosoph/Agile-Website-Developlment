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
        $('#ahome').hide(),
        $('#sb').hide(),
        $('#abase').show(),
        $('#but').show();
    })

    $('#next').click(function(){
        // NextPage function
        if($('#abase').css('display') !== 'none'){
            $('#abase').hide(),
            $('#page1').show();
        } else if($('#page1').css('display')!=='none'){
            $('#page1').hide(),
            $('#page2').show();
        } else if($('#page2').css('display')!=='none'){
            $('#page2').hide(),
            $('#page3').show();
        }
        //needs to continue for whole assessment - loop?
    })

    $('#prev').click(function(){
        // PrevPage function
        if($('#page3').css('display')!=='none'){
            $('#page3').hide(),
            $('#page2').show();
        }else if($('#page2').css('display')!=='none'){
            $('#page2').hide(),
            $('#page1').show();
        } else if($('#page1').css('display')!=='none'){
            $('#abase').show(),
            $('#page1').hide();
        } else if($('#abase').css('display') !== 'none'){
            $('#abase').hide(),
            $('#but').hide(),
            $("#sb").show(),
            $('#ahome').show();
        }
        //needs to continue for whole assessment - loop?
    })

    $('.lBlock').click(function(){
        window.location.replace('/login');
    })

    $('.sgBlock').click(function(){
        window.location.replace('/signup');
    })

    $('.asBlock').click(function(){
        window.location.replace('/assessment');
    })

    $('.uBlock').click(function(){
        window.location.replace('/login');
    })
})

