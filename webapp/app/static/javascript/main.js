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

        // Fix for a POST sumbit after refreshing a page
        if ( window.history.replaceState ) {
            window.history.replaceState( null, null, window.location.href );
        }

        $('.categoryAssessment').click(function() {
            $.post(`${window.origin}/getAssessment`, {'category': $(this).html()}, function(data, status) {
                console.log(data);
                var html = '<div class="questionBox"><textarea id="numQuestions" placeholder="Question';
                $('table').remove();
                console.log(data['name']);
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
                                  <p style="float:left" id="reset" class="button">Reset</p>
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
                    alert('Please speicify the number of questions!');
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

    //Js for adminAssessment page
    if (lastPathSegment == 'adminUser') {

        $('#search').click(function() {
            console.log($('#query').val());
            $.post(`${window.origin}/getUser`, {'query': $('#query').val()}, function(data, status) {
                console.log(data);
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
        $('#sb1').click(function(){
            $('#ahome').hide(),
            $('#sb1').hide(),
            $('#sb2').hide(),
            $('#1P0').show(),
            $('#but').show();
        })
        $('#sb2').click(function(){
            $('#ahome').hide(),
            $('#sb1').hide(),
            $('#sb2').hide(),
            $('#2P0').show(),
            $('#but').show();
        })
    
        $('#next').click(function(){
            // NextPage function
            if($('#1P0').css('display') !== 'none'){
                $('#1P0').hide(),
                $('#1P1').show();
            } else if($('#1P1').css('display')!=='none'){
                $('#1P1').hide(),
                $('#1P2').show();
            } else if($('#1P2').css('display')!=='none'){
                $('#1P2').hide(),
                $('#1P3').show();
            }else if($('#1P3').css('display')!=='none'){
                $('#1P3').hide(),
                $('#1P4').show();
            }else if($('#1P4').css('display')!=='none'){
                $('#1P4').hide(),
                $('#1P5').show();
            }else if($('#1P5').css('display')!=='none'){
                $('#1P5').hide(),
                $('#1P6').show();
            }else if($('#1P6').css('display')!=='none'){
                $('#1P6').hide(),
                $('#1P7').show();
            }else if($('#1P7').css('display')!=='none'){
                $('#1P7').hide(),
                $('#1P8').show();
            }else if($('#1P8').css('display')!=='none'){
                $('#1P8').hide(),
                $('#1P9').show(),
                $('#but').hide();
            }else if($('#2P0').css('display')!=='none'){
                $('#2P0').hide(),
                $('#2P1').show();
            }else if($('#2P1').css('display')!=='none'){
                $('#2P1').hide(),
                $('#2P2').show();
            }
        })
    
        $('#prev').click(function(){
            // PrevPage function
            if($('#2P1').css('display')!=='none'){
                $('#2P1').hide(),
                $('#2P0').show();
            }else if($('#2P2').css('display')!=='none'){
                $('#2P2').hide(),
                $('#2P1').show();
            }else if($('#1P9').css('display')!=='none'){
                $('#1P9').hide(),
                $('#1P8').show();
            }else if($('#1P8').css('display')!=='none'){
                $('#1P8').hide(),
                $('#1P7').show();
            }else if($('#1P7').css('display')!=='none'){
                $('#1P7').hide(),
                $('#1P6').show();
            }else if($('#1P6').css('display')!=='none'){
                $('#1P6').hide(),
                $('#1P5').show();
            }else if($('#1P5').css('display')!=='none'){
                $('#1P5').hide(),
                $('#1P4').show();
            }else if($('#1P4').css('display')!=='none'){
                $('#1P4').hide(),
                $('#1P3').show();
            }else if($('#1P3').css('display')!=='none'){
                $('#1P3').hide(),
                $('#1P2').show();
            }else if($('#1P3').css('display')!=='none'){
                $('#1P3').hide(),
                $('#1P2').show();
            }else if($('#1P2').css('display')!=='none'){
                $('#1P2').hide(),
                $('#1P1').show();
            } else if($('#1P1').css('display')!=='none'){
                $('#1P0').show(),
                $('#1P1').hide();
            } else if($('#1P0').css('display') !== 'none'){
                $('#1P0').hide(),
                $('#but').hide(),
                $('#sb1').show(),
                $('#sb2').show(),
                $('#ahome').show();
            } else if($('#2P0').css('display') !== 'none'){
                $('#2P0').hide(),
                $('#but').hide(),
                $('#sb1').show(),
                $('#sb2').show(),
                $('#ahome').show();
            }
        })
    
        $('.uBlock').click(function(){
            window.location.replace('/login');
        })

        $('#ex1').click(function(){
            window.location.replace('/assessment');
        })
    }

    if(lastPathSegment == ''){
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

    //get this to work
    // if(lastPathSegment == 'statistics'){
    //     $('#numUsers').ready(function(){
    //         var numUsers=0;
    //         var usersNum = db.exec("SELECT userId FROM Users")
    //         console.log(usersNum);
    //         for (users in usersNum) 
    //             numUsers=+1;
    //         $('#numUsers').html(numUsers);
    //     })
    // }

    //get this to work - low prio
    // if(lastPathSegment == 'user'){
    //     $(function changeFormat(inputDate){
    //         var splitDate = inputDate.split('-');
    //         if(splitDate.count == 0){
    //             return null;
    //         }
    //         var year = splitDate[0];
    //         var month = splitDate[1];
    //         var day = splitDate[2];

    //         return day + '-' + month + '-' + year;
    //     })

        //get this to work - can just hard code
        // $('userAssess').onload = function createAssessTable(){
        //     console.log("1");
        //     var assessTable = $('#assessTable');
        //     var count = 1;
        //     // //for each row in assessment where userId = {{user.Id}}
        //     //     var newRow = assessTable.insertRow(count);
        //     //     var nRow1 = newRow.insertCell(0);
        //     //     var nRow2 = newRow.insertCell(1);
        //     //     var nRow3 = newRow.insertCell(2);
        //     //     nRow1.innerHTML = 0;//assessment.name
        //     //     nRow2.innerHTML = 1;//in progress/completed
        //     //     nRow3.innerHTML = 2;//assessment.score
        //     //     count+=1;
        // }
    // }

})

