document.addEventListener('DOMContentLoaded', function() {
    const promptInput = document.getElementById('prompt');
    const generateBtn = document.getElementById('generateBtn');
    const resultSection = document.getElementById('resultSection');
    const errorSection = document.getElementById('errorSection');
    const generatedImage = document.getElementById('generatedImage');
    const downloadBtn = document.getElementById('downloadBtn');
    const newImageBtn = document.getElementById('newImageBtn');
    const errorText = document.getElementById('errorText');
    const btnText = document.querySelector('.btn-text');
    const loadingSpinner = document.querySelector('.loading-spinner');

    // Generate image function
    async function generateImage(prompt) {
        try {
            // Show loading state
            generateBtn.disabled = true;
            btnText.textContent = 'Generating...';
            loadingSpinner.style.display = 'flex';
            hideError();
            hideResult();

            // Make request to backend
            const response = await fetch('/generate-image', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: prompt })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                // Display the generated image
                generatedImage.src = `data:image/png;base64,${data.imageData}`;
                showResult();
            } else {
                throw new Error(data.error || 'Failed to generate image');
            }

        } catch (error) {
            console.error('Error:', error);
            showError(error.message || 'Failed to generate image. Please try again.');
        } finally {
            // Reset button state
            generateBtn.disabled = false;
            btnText.textContent = 'Generate Image';
            loadingSpinner.style.display = 'none';
        }
    }

    // Event listeners
    generateBtn.addEventListener('click', function() {
        const prompt = promptInput.value.trim();
        if (!prompt) {
            showError('Please enter a description for your image.');
            return;
        }
        generateImage(prompt);
    });

    // Allow Enter key to generate
    promptInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            generateBtn.click();
        }
    });

    // Download image
    downloadBtn.addEventListener('click', function() {
        const link = document.createElement('a');
        link.download = 'generated-image.png';
        link.href = generatedImage.src;
        link.click();
    });

    // Generate new image
    newImageBtn.addEventListener('click', function() {
        hideResult();
        promptInput.focus();
    });

    // Utility functions
    function showResult() {
        resultSection.style.display = 'block';
        resultSection.scrollIntoView({ behavior: 'smooth' });
    }

    function hideResult() {
        resultSection.style.display = 'none';
    }

    function showError(message) {
        errorText.textContent = message;
        errorSection.style.display = 'block';
        errorSection.scrollIntoView({ behavior: 'smooth' });
    }

    function hideError() {
        errorSection.style.display = 'none';
    }

    // Auto-resize textarea
    promptInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });

    // Focus on input when page loads
    promptInput.focus();
}); 