document.addEventListener('DOMContentLoaded', function() {
let toastbox = document.getElementById('toastbox')
let successmsgQAform = '<i class="fa-solid fa-circle-check"></i> We Have Received Your Message Thank You'
let errormsgQAform = '<i class="fa-solid fa-circle-check"></i> There Was An error Please Try Again Later'
let successmsg = '<i class="fa-solid fa-circle-check"></i> Sign-up successful! You can now log in.'
let errormsg = '<i class="fa-sharp fa-solid fa-circle-xmark"></i> Please fix the error!'
let invalidmsg = '<i class="fa-solid fa-circle-exclamation"></i> Sign-up failed. Please check the form for .'
function showToast(msg){
  let toasts = document.createElement('div')
  toasts.classList.add('toasts')
  toasts.innerHTML = msg
  toastbox.appendChild(toasts)
  if(msg.includes('error')){
    toasts.classList.add('error')
  }
  if(msg.includes('failed')){
    toasts.classList.add('invalid')
  }
  setTimeout(()=>{
    toasts.remove()
  },5000)
}

// Active Link Indicator
const links = document.querySelectorAll('nav a');
links.forEach(link => {
  if (link.href === window.location.href) {
    link.classList.add('active');
  }
})

//upload photo file
function readURL(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
          $('#imagePreview').css('background-image', 'url('+e.target.result +')');
          $('#imagePreview').hide();
          $('#imagePreview').fadeIn(650);
      }
      reader.readAsDataURL(input.files[0]);
  }
}
$("#inputphoto").change(function() {
  readURL(this);
});

//toggle between signup and signin
const signuppage = document.getElementById('signuppage');
const signinpage = document.getElementById('signinpage');
const showsignupbutton = document.getElementById('showsignuppage');
const showsigninbutton = document.getElementById('showsigninpage');
const togglesigninbar = document.getElementById('togglesigninbar');
const togglesignupbar = document.getElementById('togglesignupbar');

if(showsignupbutton){
  showsignupbutton.addEventListener('click', ()=>{
    signuppage.style.display = 'flex'
    togglesignupbar.style.display = 'block'
    signinpage.style.display = 'none'
    togglesigninbar.style.display = 'none'
  
  })
}
if(showsigninbutton){
  showsigninbutton.addEventListener('click', ()=>{
    signuppage.style.display = 'none'
    togglesignupbar.style.display = 'none'
  
    signinpage.style.display = 'flex'
    togglesigninbar.style.display = 'block'
  
  })
}
// Setting the form into 2 parts
const buttonsignupsubmit = document.getElementById('buttonsignupsubmit');
const buttonsignupnext = document.getElementById('buttonsignupnext');
const formsubmitpart1 = document.getElementById('formsubmitpart1');
const formsubmitpart2 = document.getElementById('formsubmitpart2');
const buttonsignupback = document.getElementById('buttonsignupback');

if(buttonsignupnext){
  buttonsignupnext.addEventListener('click', ()=>{
    if(formsubmitpart1.style.display === 'flex' || formsubmitpart1.style.display !== 'none'){
      formsubmitpart1.style.display = 'none'
      formsubmitpart2.style.display = 'flex'
      buttonsignupnext.style.display = 'none'
      buttonsignupsubmit.style.display = 'block'
      buttonsignupback.style.display = 'block'
    }
  })
}
if(buttonsignupback){
  buttonsignupback.addEventListener('click', ()=>{
    formsubmitpart1.style.display = 'flex'
    formsubmitpart2.style.display = 'none'
    buttonsignupnext.style.display = 'block'
    buttonsignupsubmit.style.display = 'none'
    buttonsignupback.style.display = 'none'
  })
}

// submit the sign in form

const signinform = document.getElementById('signinform')
if(signinform){
  signinform.addEventListener('submit', ()=>{
    inputsigninemail=document.getElementById('inputsigninemail').value
    inputsigninpassword=document.getElementById('inputsigninpassword').value
    if(inputsigninemail !== '' && inputsigninpassword !== '')
    {
      console.log('Done')
    }
  
  })
}
const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');
  errorDisplay.innerText = message;
  inputControl.classList.add('error');
  inputControl.classList.remove('success')
}
const setSuccess = element => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');
  errorDisplay.innerText = '';
  inputControl.classList.add('success');
  inputControl.classList.remove('error');
};
const validateInputs = () => {
  const inputusername = document.getElementById('inputusernames');
  const inputphonenumber = document.getElementById('inputphonenumber');
  const inputphoto = document.getElementById('inputphoto');
  const inputemails = document.getElementById('inputemail');
  const inputpasswords = document.getElementById('inputpassword');
  const inputconfirmpasswords = document.getElementById('inputconfirmpassword');
  let allValid = true;

  // If any validation fails, set allValid to false
  if (inputusername.value === '') {
      setError(inputusername, 'Username is required');
      allValid = false;
  } else {
      setSuccess(inputusername);
  }

  if (inputemails.value === '') {
      setError(inputemails, 'Email is required');
      allValid = false;
  } else {
      setSuccess(inputemails);
  }

  if (inputphonenumber.value === '') {
      setError(inputphonenumber, 'Phonenumber is required');
      allValid = false;
  } else if (inputphonenumber.value.length < 11) {
      setError(inputphonenumber, 'Phonenumber must be at least 11 characters.');
      allValid = false;
  } else {
      setSuccess(inputphonenumber);
  }

  if (inputpasswords.value === '') {
      setError(inputpasswords, 'Password is required');
      allValid = false;
  } else if (inputpasswords.value.length < 8) {
      setError(inputpasswords, 'Password must be at least 8 characters.');
      allValid = false;
  } else {
      setSuccess(inputpasswords);
  }

  if (inputconfirmpasswords.value === '') {
      setError(inputconfirmpasswords, 'Please confirm your password');
      allValid = false;
  } else if (inputconfirmpasswords.value !== inputpasswords.value) {
      setError(inputconfirmpasswords, "Passwords don't match");
      allValid = false;
  } else {
      setSuccess(inputconfirmpasswords);
  }
  if (allValid) {
    showToast(successmsg)
    const formData = new FormData();
    formData.append('inputusername', inputusername.value);
    formData.append('inputphonenumber', inputphonenumber.value);
    formData.append('inputemail', inputemails.value);
    formData.append('inputpassword', inputpasswords.value);
    formData.append('inputconfirmpassword', inputconfirmpasswords.value);
    if (inputphoto.files.length > 0) {
      formData.append('inputphoto', inputphoto.files[0]);
    }
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch('/signup', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrftoken,
      },
        body: formData,    
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/signingupdone';
        } else {
            console.error('Failed to sign up:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}else{
showToast(invalidmsg)
}
}

// submit the sign up form 
const signupform = document.getElementById('signupform')
if(signupform){
  signupform.addEventListener('submit' , (event)=>{
    event.preventDefault()
    validateInputs();
  });
}
})


//QAform
formQAs = document.getElementById('formQAs')
usernameinputQA = document.getElementById('usernameinputQA')
emailinputQA = document.getElementById('emailinputQA')
messageinputQA = document.getElementById('messageinputQA')
if(formQAs){
  formQAs.addEventListener('submit',(e)=>{
    e.preventDefault()
    fetch("https://api.apispreadsheets.com/data/9Kn5cf9moZIUvk54/", {
      method: "POST",
      body: JSON.stringify({"data": {"UserName":usernameinputQA.value ,"Email":emailinputQA.value,"Message":messageinputQA.value,}}),
    }).then(res =>{
      if (res.status === 201){
        showToast(successmsgQAform)
        console.log(emailinputQA.value)
  
      }
      else{
        showToast(errormsgQAform)
  
      }
    })
  })
}