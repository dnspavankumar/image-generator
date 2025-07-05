from flask import Flask, request, jsonify, send_from_directory
import subprocess
import json
import os
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
        
        # Get the base64 image data from stdout
        image_data = result.stdout.strip()
        
        if not image_data:
            return jsonify({
                'success': False, 
                'error': 'Image generation failed - no image data received'
            }), 500
        
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