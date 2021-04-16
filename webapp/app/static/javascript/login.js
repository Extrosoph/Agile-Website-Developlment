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