function submitSignupForm() {
    document.getElementById("signupbtn").addEventListener("click", () => {
        console.log("sign up clicked")

        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
        var confirmPassword = document.getElementById("confirmpassword").value;

        var requestBody = {
            email,
            password
        }


        console.log(requestBody)

        

        var options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email, password
            })
        }

        console.log(options)

        fetch('http://localhost:8080/signup', options)
            .then(data => {
                if (!data.ok) {
                    throw Error(data.status);
                }
                return data.json();
            }).then(update => {
                console.log(update);

            }).catch(e => {
                console.log(e);
            });

    })
}

//DELETE A NOTE
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }