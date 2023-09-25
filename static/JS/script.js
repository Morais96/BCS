video.addEventListener('ended', () => {
    video.pause();
    newsletter.style.display = "flex";
    setTimeout(() => {
        newsletter.style.opacity = 1;
    }, "100");
});

newsletterForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(newsletterForm);
    const response = await fetch(newsletterForm.action, {
        method: 'POST',
        body: formData,
    });
    if (response.ok) {
        const result = await response.json();
        if (result.valid && !result.subscribed) {
           
            subscribeVideo.style.display = 'flex';
            subscribeVideo.style.animation = 'fadein 1s';
            
            first.style.opacity = 0;
            
            subscribeVideo.addEventListener('ended', () => {
                thanks.style.display = "flex";
                thanks.style.animation = "fadein 1s";
            });
        }
        else if (result.valid && result.subscribed) {
            errorMessage.textContent = 'You are already subscribed to our newsletter.';
        }
        else if (!result.valid) {
            errorMessage.textContent = 'Invalid email address. Please enter a valid email.';
        }
    } else {
        errorMessage.textContent = 'An error occurred while validating the email.';
    }
});