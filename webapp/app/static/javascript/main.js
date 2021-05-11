// String manipulation function to assist
function stringManipulations(data) {
    var value = data.replaceAll('"', '');
    value = value.replaceAll('"', '');
    value = value.replaceAll('[', '');
    value = value.replaceAll(']', '');
    value = value.replace(/\s/g, "");
    value = value.split(',');
    return value;
}

// Function to create table for users
function createTable(username, email, admin, date) {
    var table = `<table class="user" >
                <tr>
                    <th>username</th>
                    <th>Email</th>
                    <th>Admin Privileges</th>
                    <th>Date Joined</th>
                <tr>`;

    // Add username to table
    table = table.concat('<tr><td>');
    table = table.concat(username);
    table = table.concat('</td>');

    // Add email to table
    table = table.concat('<td>');
    table = table.concat(email);
    table = table.concat('</td>');

    // Add admin privileges to table
    table = table.concat('<td>');
    table = table.concat(admin);
    table = table.concat('</td>');

    // Add admin privileges to table
    table = table.concat('<td>');
    table = table.concat(date.substring(0,3));
    table = table.concat(',');
    table = table.concat(date.substring(4,16));
    table = table.concat('</td>');

    return table;
}


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

        // Fix for a POST submit after refreshing a page
        if ( window.history.replaceState ) {
            window.history.replaceState( null, null, window.location.href );
        }

        $('.categoryAssessment').click(function() {
            $.post(`${window.origin}/getAssessment`, {'category': $(this).html()}, function(data, status) {
                var html = '<div class="questionBox"><textarea id="numQuestions" placeholder="Question';
                $('table').remove();
                $('h1').html(data['name']);
                var first = `<form method="post" id="myform">
                             <div class="input-box">
                             <input id="name" name="assessmentName" placeholder="namehere" maxlength="100">
                             </div>`;
                first = first.replace('namehere',data['name']);
                $('main').append(first);

                const questions = stringManipulations(data['questions']);

                const answers = stringManipulations(data['answers']);

                const correctAnswer = stringManipulations(data['correctAnswer']);

                const marks = stringManipulations(data['mark']);

                var a=0, b=1, c=2, d=3;
                for (var i=0; i < questions.length; i++) {
                    var html1 = '<div class="questionBox"><textarea id="numQuestions" placeholder="';
                    var html2 = html1.concat(questions[i]);
                    var html3 = html2.concat('" name="question');
                    var html4 = html3.concat((i+1).toString());
                    var html5 = html4.concat('" maxlength="200"></textarea><textarea id="score" placeholder="')
                    html5 = html5.concat(marks[i]);
                    html5 = html5.concat('" name="score" maxlength="2"></textarea></div>');
                    var answer = `<div class="answerBox" name="as">
                                   <textarea id="answer1" placeholder="Answer1" maxlength="200" name="answer"></textarea>
                                   <textarea id="answer2" placeholder="Answer2" maxlength="200" name="answer"></textarea>
                                   <textarea id="answer3" placeholder="Answer3" maxlength="200" name="answer"></textarea>
                                   <textarea id="correctAnswer" placeholder="Correct Answer" maxlength="200" name="answer"></textarea>
                                   </div>`;
                    answer = answer.replace('Answer1', answers[a]);
                    answer = answer.replace('Answer2', answers[b]);
                    answer = answer.replace('Answer3', answers[c]);
                    answer = answer.replace('Correct Answer', answers[d]);

                    a += 4;
                    b += 4,
                    c += 4;
                    d += 4;

                    var html6 = html5.concat(answer);
                    $('#myform').append(html6);

                }

                $('form').append(`<div style="width:60%;margin:40px auto;" >
                                  <p style="margin-left: -100px margin-right: 10px" id="reset" class="button">Reset</p>
                                  <p style="text-align:center vertical-align: middle" id="Delete" class="button">Delete</p>
                                  <button style="float:right" type="submit" id="update" class="button">Update</button>
                                  </div>`);

                $('#reset').click(function() {
                        $('textarea').val('');
                        $('#name').val('');
                })

                $('#update').click(function() {

                    // Check if any fields are empty
                    if ($('#score').val() == '' || $('textarea').val() == '' || $('#name').val() == '') {
                        alert('Please fill in all fields!');
                        return false;
                    }

                    // Check if the score is a number
                    if (isNaN($('#score').val())) {
                        alert('Scores need to be a number');
                        return false;
                    }
                })
            });
        });

        $('#newCategory').click(function() {
            $('h1').html('New Assessment');
            $('#assessmentTable').remove();
            $('main').append(`<form method="post" id="myform">
                              <div class="input-box">
                              <input id="name" name="assessmentName" placeholder="Assessment name" maxlength="100">
                              </div>
                              <div class="input-box" id="initial">
                              <input id="numQuestions" placeholder="Number of Questions" maxlength="3" >
                              </div>
                              <p id="createQs" class="button">Create</p>`);

            $('#createQs').click(function() {

                // Check if the number of question field is empty
                if (!$('#numQuestions').val()) {
                    alert('Please specify the number of questions!');
                    return false;
                }

                // Check if the number of question field is an Integer
                else if (!Number.isInteger(parseFloat($('#numQuestions').val()))) {
                    alert('Number of questions needs to be an integer');
                    return false;
                }

                // Create the question template
                else {
                    const numberOfQs = $('#numQuestions').val();
                    $('#initial').remove();
                    $(this).remove();
                    for(var i=0; i < numberOfQs; i++) {
                        var html1 = '<div class="questionBox"><textarea id="numQuestions" placeholder="Question';
                        var html2 = html1.concat((i+1).toString());
                        var html3 = html2.concat('" name="question');
                        var html4 = html3.concat((i+1).toString());
                        var html5 = html4.concat('" maxlength="200"></textarea><textarea id="score" placeholder="score" name="score" maxlength="2"></textarea></div>');
                        var answers = `<div class="answerBox" name="as">
                                       <textarea id="answer1" placeholder="Answer1" maxlength="200" name="answer"></textarea>
                                       <textarea id="answer2" placeholder="Answer2" maxlength="200" name="answer"></textarea>
                                       <textarea id="answer3" placeholder="Answer3" maxlength="200" name="answer"></textarea>
                                       <textarea id="correctAnswer" placeholder="Correct Answer" maxlength="200" name="answer"></textarea>
                                       </div>`;
                        var html6 = html5.concat(answers);
                        $('#myform').append(html6);
                    }

                    $('form').append(`<div style="width:60%;margin:40px auto;" >
                                      <p style="float:left" id="reset" class="button">Reset</p>
                                      <button style="float:right" type="submit" id="submit" class="button">Submit</button>
                                      </div>`);

                    $('#reset').click(function() {
                        $('textarea').val('');
                        $('#name').val('');
                    })

                    $('#submit').click(function() {

                        // Check if any fields are empty
                        if ($('#score').val() == '' || $('textarea').val() == '' || $('#name').val() == '') {
                            alert('Please fill in all fields!');
                            return false;
                        }

                        // Check if the score is a number
                        if (isNaN($('#score').val())) {
                            alert('Scores need to be a number');
                            return false;
                        }
                    })
                }
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

    //Js for adminUser page
    if (lastPathSegment == 'adminUser') {

        $('#search').click(function() {
            $.post(`${window.origin}/getUser`, {'query': $('#query').val()}, function(data, status) {
                if (Object.keys(data).length == 1) {
                    $('#userMessage').text('No such user!');
                }

                else {

                    const username = data['username'];
                    const email = data['email'];
                    const admin = data['Admin'];
                    const date = data['dateJoined'];

                    $('#main2').empty();
                    var header = '<h1>';
                    header = header.concat(username);
                    header = header.concat('</h1>')
                    $('#main2').append(header);

                    var table = createTable(username, email, admin, date)

                    $('#main2').append(table);

                    $('#main2').append(`<div style="width:60%;margin:40px auto;" >
                                          <p style="float:left" id="remove" class="button">Remove</p>
                                          <p style="float:right" id="makeAdmin" class="button">Make Admin</p>
                                          </div>`);

                    $('#remove').click(function() {
                        $.post(`${window.origin}/removeUser`, {'username': username},  function(data, status) {
                            window.location.replace(`${window.origin}/adminUser`);
                        })
                    })

                    $('#makeAdmin').click(function() {
                        $.post(`${window.origin}/makeAdmin`, {'username': username},  function(data, status) {
                        window.location.replace(`${window.origin}/adminUser`);
                        })
                    })

                }
            })
        })

        $('.categoryAssessment').click(function() {
            $.post(`${window.origin}/getUser`, {'query': $(this).html()}, function(data, status) {

            const username = data['username'];
            const email = data['email'];
            const admin = data['Admin'];
            const date = data['dateJoined'];

            $('#main2').empty();
            var header = '<h1>';
            header = header.concat(username);
            header = header.concat('</h1>')
            $('#main2').append(header);

            var table = createTable(username, email, admin, date);

            $('main').append(table);

            $('main').append(`<div style="width:60%;margin:40px auto;" >
                                  <p style="float:left" id="remove" class="button">Remove</p>
                                  <p style="float:right" id="makeAdmin" class="button">Make Admin</p>
                                  </div>`);

            $('#remove').click(function() {
                $.post(`${window.origin}/removeUser`, {'username': username},  function(data, status) {
                    window.location.replace(`${window.origin}/adminUser`);
                })
            })

            $('#makeAdmin').click(function() {
                $.post(`${window.origin}/makeAdmin`, {'username': username},  function(data, status) {
                window.location.replace(`${window.origin}/adminUser`);
                })
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

    if(lastPathSegment == 'assessment'){
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
    
        $('.uBlock').click(function(){
            window.location.replace('/login');
        })
    }

    if(lastPathSegment == ''){
        //Ajax query to create an admin account
        $.post(`${window.origin}/adminAccount`, {'query': 'make'},  function(data, status) {
            // Do nothing
            console.log(data);
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
    }

})

