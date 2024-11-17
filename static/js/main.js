document.getElementById('generate-btn').addEventListener('click', async () => {
    const generateBtn = document.getElementById('generate-btn');
    const generatedBio = document.getElementById('generated-bio');
    
    // Gather form data
    const career = document.getElementById('career').value;
    const personality = document.getElementById('personality').value;
    const interests = document.getElementById('interests').value;
    const hobby = document.getElementById('hobby').value;
    const relationship_goal = document.getElementById('relationship_goal').value;

    // Validate form
    if (!career || !personality || !interests || !hobby || !relationship_goal) {
        alert('Please fill in all fields');
        return;
    }

    try {
        // Show loading state
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';
        generatedBio.textContent = 'Crafting your perfect bio...';

        // Send request to backend
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
        
        // Display the generated bio
        generatedBio.textContent = data.bio;
    } catch (error) {
        console.error('Error:', error);
        generatedBio.textContent = 'An error occurred while generating your bio. Please try again.';
    } finally {
        // Reset button state
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Bio';
    }
});