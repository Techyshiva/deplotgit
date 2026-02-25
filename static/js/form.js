const contactForm = document.getElementById('contactForm');
const successMessage = document.getElementById('successMessage');

if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Stop the page from reloading

    const formData = new FormData(contactForm);

    fetch(contactForm.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (response.ok) {
            contactForm.style.display = 'none';

            successMessage.style.display = 'flex';

            setTimeout(() => {
              successMessage.style.display = 'none';
              
              contactForm.style.display = 'block';
              
              contactForm.reset();
            }, 3000);
        } else {
            alert("Oops! Something went wrong on the server. Please try again.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("A network error occurred. Please check your connection.");
    });
  });
}