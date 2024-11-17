/**
 * Handles the click event of the "Generate Bio" button, sending a request to the backend to generate a bio based on the user's input.
 *
 * This function performs the following steps:
 * 1. Gathers the form data (career, personality, interests, hobby, and relationship goal) from the user.
 * 2. Validates that all form fields are filled out.
 * 3. Disables the "Generate Bio" button and displays a "Generating..." message.
 * 4. Sends a POST request to the "/generate-bio" endpoint with the form data.
 * 5. Displays the generated bio in the "generated-bio" element.
 * 6. Handles any errors that occur during the bio generation process.
 * 7. Enables the "Generate Bio" button and resets its text.
 */
document.getElementById('generate-btn').addEventListener('click', async () => {
    const generateBtn = document.getElementById('generate-btn');
    const generatedBio = document.getElementById('generated-bio');
    
    const career = document.getElementById('career').value;
    const personality = document.getElementById('personality').value;
    const interests = document.getElementById('interests').value;
    const hobby = document.getElementById('hobby').value;
    const relationship_goal = document.getElementById('relationship_goal').value;

    if (!career || !personality || !interests || !hobby || !relationship_goal) {
        alert('Please fill in all fields');
        return;
    }

    try {
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';
        generatedBio.textContent = 'Crafting your perfect bio...';

        const response = await fetch('/generate-bio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                career,
                personality,
                interests,
                hobby,
                relationship_goal
            })
        });

        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        generatedBio.textContent = data.bio;
    } catch (error) {
        console.error('Error:', error);
        generatedBio.textContent = 'An error occurred while generating your bio. Please try again.';
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Bio';
    }
});