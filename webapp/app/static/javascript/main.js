$(document).ready(function() {
    var href = document.location.href;
    var lastPathSegment = href.substr(href.lastIndexOf('/') + 1);

    //Js for login and signup page
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

        //Js for login page
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

        //Js for signup page
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

                if (/[a-z]/.test($('#passwordInput').val()) == false) {
                    alert('Password requires lowercase characters!')
                    return false;
                }

                if (/[A-Z]/.test($('#passwordInput').val()) == false) {
                    alert('Password requires uppercase characters!')
                    return false;
                }

                if (/[0-9]/.test($('#passwordInput').val()) == false) {
                    alert('Password requires numbers!')
                    return false;
                }
            })
        }
    }

    //Js for admin page
    if (lastPathSegment == 'admin') {
        // Function to add the menu items and move everything to the right
        $('#menus').click(function() {
            $('#mySidenav').css('width', '250px');
            $('#main').css('margin-left', '250px');
        })

        $('#close').click(function() {
            $('#mySidenav').css('width', '0px');
                $('#main').css('margin-left', '0px');
        })
    }

    //Js for adminAssessment page
    if (lastPathSegment == 'adminAssessment') {
        $('#newCategory').click(function() {
            $('h1').html('New Assessment');
            $('#assessmentTable').remove();
            $('main').append(`<form method="post" id="myform"><div class="input-box"><input id="name"
                             placeholder="Assessment name" maxlength="100"></div><div class="input-box"
                             id="initial"><input id="numQuestions" placeholder="Number of Questions"
                             maxlength="3" ></div><p id="createQs" class="button">Create</p>`);

            $('#createQs').click(function() {
                $('h1').html($('#name').val());
                $('#name').val('');
                $('#name').attr('placeholder', 'New name if unsatisfied');
                const numberOfQs = $('#numQuestions').val();
                $('#initial').remove();
                $(this).remove();
                for(var i=0; i < numberOfQs; i++) {
                    var html1 = '<div class="questionBox"><textarea id="numQuestions" placeholder="Question ';
                    var html2 = html1.concat((i+1).toString());
                    var html3 = html2.concat('" maxlength="200"></textarea></div>');
                    var answers = `<div class="answerBox"><textarea id="answer1" placeholder="Answer1" maxlength="200"></textarea>
                                   <textarea id="answer2" placeholder="Answer2" maxlength="200"></textarea>
                                   <textarea id="answer3" placeholder="Answer3" maxlength="200"></textarea>
                                   <textarea id="correctAnswer" placeholder="Correct Answer" maxlength="200"></textarea></div>`
                    var html4 = html3.concat(answers);
                    $('#myform').append(html4);
                }
                $('form').append(`<div style="width:60%;margin:40px auto;" ><p style="float:left" type="submit" id="reset" class="button">Reset</p>
                                 <button style="float:right" type="submit" id="submit" class="button">Submit</button></div>`)
                $('#reset').click(function() {
                    $('textarea').val('');
                })
            })
        })

        // Function to add the menu items and move everything to the right
        $('#menus').click(function() {
            $('#mySidenav').css('width', '250px');
            $('#main').css('margin-left', '250px');
        })

        $('#close').click(function() {
            $('#mySidenav').css('width', '0px');
                $('#main').css('margin-left', '0px');
        })
    }

    //Js for adminAssessment page
    if (lastPathSegment == 'adminUser') {
        // Function to add the menu items and move everything to the right
        $('#menus').click(function() {
            $('#mySidenav').css('width', '250px');
            $('#main').css('margin-left', '250px');
        })

        $('#close').click(function() {
            $('#mySidenav').css('width', '0px');
                $('#main').css('margin-left', '0px');
        })
    }

})