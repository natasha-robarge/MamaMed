$(document).ready(function () {
    $("#responses").html('<iframe src="https://plot.ly/~karmakettle/0/google-home-responses-vs-weeks/#/" height="250" width="1450"></iframe>');
    $("#diagnoses").html('<iframe src="https://plot.ly/~karmakettle/6/diagnoses-vs-weeks/#/" height="250" width="1450"></iframe>')
    $("#visits").html('<iframe src="https://plot.ly/~karmakettle/2/visits-vs-weeks/#/" height="250" width="1450"></iframe>')
    $("#medications").html('<iframe src="https://plot.ly/~karmakettle/4/medications-vs-weeks/#/" height="250" width="1450"></iframe>')

    //file:///C:/dev/MamaMed/dashboards-gh-pages/layouts/hero-thirds/index.html

    $.get({
        type: 'GET',
        url: 'https://ec2-54-225-45-156.compute-1.amazonaws.com:5000/mamamed/patient/1',
        contentType: 'application/json',
        dataType: 'json',
        success: function(response) {
            console.log(response, " response data");
            $("#patient-name").append(response[0].patientInfo.name);
            $("#birth-date").append(response[0].patientInfo.dateOfBirth);
            $("#age").append(" " + response[0].patientInfo.age);
            $("#pregnancy-start-date").append(" " + response[0].patientInfo.pregnancyStartDate.slice(0, 11));
            $("#due-date").append(response[0].patientInfo.dueDate.slice(0, 10));

                // For iterating through medications
                for(var m = 0; m < response[0].medications.length; m++) {
                    var meds = $("#meds-list").append(`<li>${response[0].medications[m].name}</li>`)
                        .append(`<span class="bolder-text ft-sz-sm">Prescribed By:</span> ${response[0].medications[m].prescribedBy}`);

                        meds.append(`<br/><span class="bolder-text ft-sz-sm">Start Date:</span> ${response[0].medications[m].date.slice(0, 11).toString()}`);
                        meds.append(`<hr class="hr-style-1"/>`);
                }

                // For iterating through appointments
                for (var a = 0; a < response[0].appointments.length; a++) {
                    $("#visit-history").append(`<li>${response[0].appointments[a].date}</li>`)
                        .append(`&emsp;&emsp;<span class="italicize bolder-text">Notes:</span><span class="italicize"> ${response[0].appointments[a].name}</span>`)
                }

                // For iterating through patient responses to Google Voice
                for (var r = 0; r < response[0].patientGoogleVoiceSessions.length; r++) {
                    $("#recent-voice-responses").append(`<li>${response[0].patientGoogleVoiceSessions[r].date}</li>`)
                        .append(`&emsp;<span class="italicize bolder-text">Patient Responses:</span><span class="italicize"> ${response[0].patientGoogleVoiceSessions[r].name}</span><hr class="hr-style-1"/>`);
                }

        },
        error: function(error) {
            console.log(error, " error message");
        }
    })

});

