$(document).ready(function() {
    const password = $('#passwordInput') ;
    //Function to show and hide password
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

    //Function to make it into a Sign Up page
    $('#signup').click(function() {
        $('h1').text("Sign Up");
        $('h1').after('<div class="input-box"><input type="username" name="username" placeholder="Username"></div>');
        $('#login').remove();
        $('#forget-password').remove();
        $('#signup').remove();
        $('#myform').append('<button type="submit" id="signup" class="button">Sign up</button>')
    })

    //Function to make it into a Forget Password page
    $('#forget-password').click(function() {
        $('h1').text("Forget Password");
        $('#password').remove();
        $('#login').remove();
        $('#forget-password').remove();
        $('#signup').remove();
        $('#myform').append('<button type="submit" id="Verify" class="button">Verify</button>')
    })
})