# AI Image Generator

A beautiful web application that generates images using Google's Gemini AI. Features a modern frontend with a Java backend.

## Features

- 🎨 Beautiful, responsive web interface
- 🚀 Real-time image generation
- 📥 Download generated images
- 🎯 Custom prompts from users
- ⚡ Fast and efficient

## Setup

### Prerequisites

1. **Java 8 or higher**
2. **Python 3.7 or higher**
3. **Google Gemini API Key**

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Compile the Java program:**
   ```bash
   javac GeminiImageGenerator.java
   ```

4. **Set up your API key:**
   - Open `GeminiImageGenerator.java`
   - Replace the `API_KEY` value with your actual Gemini API key
   - Recompile: `javac GeminiImageGenerator.java`

## Running Locally

1. **Start the web server:**
   ```bash
   python server.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. **Enter a description and click "Generate Image"**

## Deployment Options

### Option 1: Heroku (Recommended)

1. **Create a `Procfile`:**
   ```
   web: python server.py
   ```

2. **Create a `runtime.txt`:**
   ```
   python-3.9.18
   ```

3. **Deploy to Heroku:**
   ```bash
   heroku create your-app-name
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

### Option 2: Railway

1. **Connect your GitHub repository to Railway**
2. **Railway will automatically detect and deploy the Python app**

### Option 3: Render

1. **Create a `render.yaml` file:**
   ```yaml
   services:
     - type: web
       name: ai-image-generator
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: python server.py
       envVars:
         - key: PYTHON_VERSION
           value: 3.9.18
   ```

### Option 4: Vercel

1. **Create a `vercel.json`:**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "server.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "server.py"
       }
     ]
   }
   ```

## Security Considerations

⚠️ **Important:** Before deploying, make sure to:

1. **Move your API key to environment variables:**
   ```java
   // Instead of hardcoding:
   private static final String API_KEY = "your-key-here";
   
   // Use environment variable:
   private static final String API_KEY = System.getenv("GEMINI_API_KEY");
   ```

2. **Set the environment variable in your deployment platform**

3. **Never commit API keys to version control**

## File Structure

```
image_generator/
├── index.html          # Frontend HTML
├── styles.css          # Frontend styles
├── script.js           # Frontend JavaScript
├── server.py           # Python web server
├── GeminiImageGenerator.java  # Java backend
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## API Usage

The application uses Google's Gemini 2.0 Flash Image Generation API. Make sure you have:
- A valid Gemini API key
- Sufficient API quota
- Proper billing setup

## Troubleshooting

### Common Issues:

1. **"Java not found" error:**
   - Make sure Java is installed and in your PATH
   - Try: `java -version`

2. **"API key invalid" error:**
   - Verify your Gemini API key is correct
   - Check your API quota and billing

3. **"Image generation failed":**
   - Check your internet connection
   - Verify the API endpoint is accessible
   - Review the API response for error details

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License. # image-generator
