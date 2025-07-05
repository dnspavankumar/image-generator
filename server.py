from flask import Flask, request, jsonify, send_from_directory
import subprocess
import json
import os
import base64
import tempfile
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'success': False, 'error': 'No prompt provided'}), 400
        
        # Create a temporary file for the generated image
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            temp_filename = temp_file.name
        
        # Run the Java program with the prompt
        result = subprocess.run(
            ['java', 'GeminiImageGenerator', prompt],
            capture_output=True,
            text=True,
            cwd='.'
        )
        
        if result.returncode != 0:
            return jsonify({
                'success': False, 
                'error': f'Java execution failed: {result.stderr}'
            }), 500
        
        # Check if the image was generated
        if not os.path.exists('generated_image.png'):
            return jsonify({
                'success': False, 
                'error': 'Image generation failed - no output file created'
            }), 500
        
        # Read and encode the image
        with open('generated_image.png', 'rb') as img_file:
            image_data = base64.b64encode(img_file.read()).decode('utf-8')
        
        # Clean up the temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)
        
        return jsonify({
            'success': True,
            'imageData': image_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

if __name__ == '__main__':
    print("Starting AI Image Generator Server...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 