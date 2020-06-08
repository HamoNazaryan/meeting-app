
    // document.addEventListener("DOMContentLoaded", function(){
    //   $('.preloader-background').delay(1700).fadeOut('slow');
      
    //   $('.preloader-wrapper')
    //     .delay(1700)
    //     .fadeOut();
    // });



$(".flash-block i").click(function(){
  $(".flash-block").fadeOut("slow");
});

setTimeout(function() {
  $('.flash-block').fadeOut('slow');
}, 7000);


$('select').formSelect();


let url;
$('.modal-trigger').on('click',function (event) {  
  url = $(this).attr('data-id');  
});

$('.modal').modal({
  onOpenStart: function(){
    $(".delete_form").attr("action", url);
  },
});

function mySubmit(form) {};

$.validator.setDefaults({
       ignore: []
});

$('#meeting-form').validate({
  // submitHandler: mySubmit,
  // errorClass: "invalid form-error",
  // errorElement: 'div',
  errorPlacement: function(error, element) {
    // error.appendTo(element.parent());
    element.parent().addClass("invalid");
    element.addClass("validate invalid");
  },
  // rules: {
  //   EndDate: { greaterThan: "#pickerStart" }
// }
});



$(".input-field").change(function(){
  if ($(".input-field").val() != ""){
    $(".input-field").removeClass("invalid");
    $(".input-field").removeClass("error");
    $(".select-wrapper").removeClass("invalid");
    $(".select-wrapper").addClass('del-after');
  } 
  else 
  {
    $(".input-field").addClass("invalid");
    $(".select-wrapper").removeClass('del-after');   
  }
})


let valid = true;


  
  let startToEnd;


let currYear = (new Date()).getFullYear();
let currDay = (new Date()).getDate();
let currMonth = (new Date()).getMonth();
let isoDate;
 
  $('#datepickerStart, #datepickerEnd').datepicker({
    minDate: new Date(currYear,currMonth,currDay),
    setDefaultDate: true,
    defaultDate: new Date(currYear,currMonth,currDay),
    maxDate: new Date(currYear+1,currMonth,currDay),
    // format: 'dd/mm/yyyy',
  });


$("#datepickerStart").change(function(){
    
 startToEnd = ($("#datepickerStart").val());
  
  let d = $('#datepickerStart').val();

  isoDate = new Date(d).toString();
  $('#datepickerEnd').datepicker({
    minDate: new Date((new Date(isoDate)).getFullYear(),(new Date(isoDate)).getMonth(),(new Date(isoDate)).getDate()),
    setDefaultDate: true,
    defaultDate: new Date(currYear,currMonth,currDay),
    maxDate: new Date(currYear+1,currMonth,currDay),
  });
  
});





$('#datepickerEnd').change(function(){
  let secondDate = new Date($('#datepickerEnd').val()).toString();
  $('#datepickerStart').datepicker({
    minDate: new Date(currYear,currMonth,currDay),
    maxDate: new Date((new Date(secondDate)).getFullYear(),(new Date(secondDate)).getMonth(),(new Date(secondDate)).getDate()),
  });
 
});


$(".datepicker").change(function(){

  if ($(this).val() != ""){
    $(this).removeClass("validate invalid");
    $(this).addClass("valid");
  } 
  else 
  {
    $(this).closest('.top-row').addClass("");
  }
})

$('.datepicker').change(function(){
  if ( ($("#datepickerStart").val() !="") && ($("#datepickerEnd").val() !="")){
    if ($("#datepickerStart").val() > $("#datepickerEnd").val()){
      valid = false;
      if( event.target.id == "datepickerEnd") {
        $("#datepickerEnd").closest(".field-wrap").find('span.helper-text').attr("data-error","The end date must be greater than the start date.");
        $('#datepickerEnd').addClass("invalid").removeClass("valid");
      }
      if( event.target.id == "datepickerStart") {
        $("#datepickerStart").closest(".field-wrap").find('span.helper-text').attr("data-error","The start date must be less than the end date.");
        $('#datepickerStart').addClass("invalid").removeClass("valid");
      }
    }
    else {
      $('.datepicker').addClass("valid").removeClass("invalid");
      valid = true;
    }
  }
})



$('#pickerStart, #pickerEnd').timepicker({
  twelveHour: false,
});

$('#pickerStart').change(function(){
  let time=$('#pickerStart').val();
  $('#pickerEnd').timepicker({
    twelveHour: false,
    defaultTime: time,
  })
})

$(".timepicker").change(function(event){
  let start_time = $("#pickerStart").val();
  let end_time = $("#pickerEnd").val();


  if ($(this).val() != ""){
    $(this).removeClass("validate invalid").addClass("valid");
  } 
  else 
  {
    $(this).closest('.top-row').addClass("");
  }
  if( start_time != "" && end_time != ""){
    var stt = new Date("May 10, 2020 " + start_time);
    stt = stt.getTime();
    
    var endt = new Date("May 10, 2020 " + end_time);
    endt = endt.getTime();


    if(stt >= endt) {
      if( event.target.id == "pickerEnd") {
        $("#pickerEnd").closest(".field-wrap").find('span.helper-text').attr("data-error","The end time must be greater than the start time.");
        $('#pickerEnd').addClass("invalid").removeClass("valid");
      }
      if( event.target.id == "pickerStart") {
        $("#pickerStart").closest(".field-wrap").find('span.helper-text').attr("data-error","The start time must be less than the end time.");
        $('#pickerStart').addClass("invalid").removeClass("valid");
      }
      
      valid = false;

      } else
      {
        valid=true;

        $(".timepicker").removeClass("invalid").addClass("valid");
      }
 
    }
})


function validateForm() {

  let start_time = $("#pickerStart").val();
  let end_time = $("#pickerEnd").val();

  if (end_time == ""){
    $("#pickerEnd").closest(".field-wrap").find('span.helper-text');
    $('#pickerEnd').addClass("invalid").removeClass("valid");
  }

  if( start_time != "" && end_time != ""){
    var stt = new Date("May 10, 2020 " + start_time);
    stt = stt.getTime();
    
    var endt = new Date("May 10, 2020 " + end_time);
    endt = endt.getTime();
        
    if(stt >= endt) {     
        // $("#pickerStart").closest(".field-wrap").find('span.helper-text').attr("data-error","The start time must be less than the end time.");
        // $('#pickerStart').addClass("invalid").removeClass("valid");
        // $("#pickerEnd").closest(".field-wrap").find('span.helper-text').attr("data-error","The end time must be greater than the start time.");
        // $('#pickerEnd').addClass("invalid").removeClass("valid");
          valid = false
          return valid
    } 
    else 
    {
      valid = true;

    }
  }
 

    if ($("#datepickerStart").val() > $("#datepickerEnd").val()){
      valid = false;
    }
    else {
      valid = true;
    }


  return valid;
}





  if ($('#signup').length > 0){    
  let password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");

  function validatePassword(){
    if(password.value!="" && confirm_password.value!=""){
      if(password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Field must be equal to password.");
      } else {
        confirm_password.setCustomValidity('');
      }
    }
  }

    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;
    $('.signupPass, .signupConfimPass').characterCounter();
  }


$('#passLogin, .length, input[type=password').characterCounter();


  $('.sidenav').sidenav({
    edge: 'right',
  });




$(".dropdown-content.select-dropdown li").attr('required');


// var select = $('select');

// $("#reset").click(function(){
//     $("form input").val("");
//     select.prop('selectedIndex', 0); 
//     select.material_select();
// });




var pageX = $(document).width();
var pageY = $(document).height();
var mouseY=0;
var mouseX=0;

$(document).mousemove(function( event ) {
  //verticalAxis
  mouseY = event.pageY;
  yAxis = (pageY/2-mouseY)/pageY*300; 
  //horizontalAxis
  mouseX = event.pageX / -pageX;
  xAxis = -mouseX * 100 - 100;

  $('.box__ghost-eyes').css({ 'transform': 'translate('+ xAxis +'%,-'+ yAxis +'%)' }); 

  //console.log('X: ' + xAxis);

});



// $('#pickerEnd').timepicker({
//   twelveHour: false,
// });




// let pickStartTime;
// let pickEndTime;


//   $("#pickerStart").change(function(){
  
//     if($("#pickerStart").val() != ""){
//       $('#pickerEnd').removeAttr("disabled");
//     } 
//     let disabledHours=[];
//     pickStartTime = ($(this).val()).split(":");
    
//     for (i=0; i<pickStartTime[0]; i++){
//         disabledHours.push(i);
//     } 

// //   $('#pickerEnd').pickatime({
// //       default: ($(this).val()),
// //       fromnow: 0,
// //       twelvehour: false,
// //       // donetext: 'OK',
// //       // autoclose: false,
// //       // ampmclickable: true,
// //       disabledHours: disabledHours,
// //       afterShow: function()
// //       {
// //         $(".clockpicker-dial.clockpicker-hours .clockpicker-tick").each(
// //             function()
// //             {
// //               if($.inArray(parseInt($(this).text()),disabledHours)!==-1)
// //                   $(this).addClass('grey-text');    
// //               return;
// //             }
// //         );    
// //         return;
// //       },
// //   });

// // });

//   $('#pickerEnd').change(function() {
//     $(this ).closest(".field-wrap").find("label").addClass( "active" );
//     pickEndTime = $('#pickerEnd').val().split(":");
//   });
// });