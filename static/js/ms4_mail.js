
/*jshint esversion: 6*/
// Send email using EmailJS template
// Report success on console 
// Clear the form
// Show confirmation modal


function sendMail(ms3_contact_form){
    emailjs.send("service_turuhuh","template_d54kn78",{
from_name: ms4_contact_form.name.value,
from_email: ms4_contact_form.email_address.value,
add_message: ms4_contact_form.message_text.value,
})
      .then(
       function(response){
           console.log("Successful", response);
       },
       function(error){
          console.log("Failed", error);  
       })
       .then( 
         function (){
           document.getElementById("ms4_contact_form").reset(); 
        })
        .then(
          $('#formSubmitModal').modal('show'));
       return false; 
}