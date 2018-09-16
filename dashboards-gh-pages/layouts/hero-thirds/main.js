$(document).ready(function () {
    $("#responses").html('<iframe src="https://plot.ly/~cfwarnoc/18/#/" height="250" width="1450"></iframe>');
    $("#diagnoses").html('<iframe src="https://plot.ly/~cfwarnoc/14/#/" height="250" width="1450"></iframe>')
    $("#visits").html('<iframe src="https://plot.ly/~cfwarnoc/12/#/" height="250" width="1450"></iframe>')
    $("#medications").html('<iframe src="https://plot.ly/~cfwarnoc/16/#/" height="250" width="1450"></iframe>')

    //file:///C:/dev/MamaMed/dashboards-gh-pages/layouts/hero-thirds/index.html

    $.get({
        type: 'GET',
        url: 'https://ec2-54-225-45-156.compute-1.amazonaws.com:5000/mamamed/patient/1',
        contentType: 'application/json',
        dataType: 'json',
        success: function(response) {
            console.log(response, " response data");
            $("#age").append(" " + response[0].patientInfo.age);
            $("#pregnancy-start-date").append(" " + response[0].patientInfo.pregnancyStartDate);

                // For iterating through medications
                for(var m = 0; m < response[0].medications.length; m++) {
                    var meds = $("#meds-list").append(`<li>${response[0].medications[m].name}</li>`)
                        .append(`&emsp;<span class="bolder-text ft-sz-sm">Prescribed By:</span> ${response[0].medications[m].prescribedBy}`);

                        meds.append(`<br/>&emsp;&emsp;<span class="bolder-text ft-sz-sm">Start Date:</span> ${response[0].medications[m].startDate.slice(0, 11).toString()}`);
                }

                // For iterating through appointments
                for (var a = 0; a < response[0].appointments.length; a++) {
                    $("#visit-history").append(`<li>${response[0].appointments[a].date.slice(0, 11).toString()}</li>`)
                        .append(`&emsp;&emsp;<span class="italicize bolder-text">Notes:</span><span class="italicize"> ${response[0].appointments[a].comment}</span>`)
                }

                // For iterating through patient responses to Google Voice
                for (var r = 0; r < responses[0].patientGoogleVoiceSessions.length; r++) {
                    $("#recent-voice-responses").append(`${responses[0].patientGoogleVoiceSessions}`);
                }

        },
        error: function(error) {
            console.log(error, " error message");
        }
    })

});

