from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

app = Flask(__name__)
 
# Initialize Groq client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def generate_prompt(data):
    return f"""Generate a unique and engaging dating profile bio based on the following information:
    Career: {data['career']}
    Personality: {data['personality']}
    Interests: {data['interests']}
    Hobby: {data['hobby']}
    Relationship Goal: {data['relationship_goal']}

    The bio should be personal, engaging, and around 2-3 sentences long. Make it sound natural and highlight the unique combination of traits and interests. Don't use emojis or hashtags."""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-bio', methods=['POST'])
def generate_bio():
    try:
        data = request.get_json()
        
        # Create the prompt for Groq
        prompt = generate_prompt(data)
        
        # Make request to Groq API
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a creative bio writer for a dating app. Write engaging, authentic, and natural-sounding bios."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            stream=False
        )
        
        # Extract the generated bio
        generated_bio = completion.choices[0].message.content.strip()
        
        return jsonify({'bio': generated_bio})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to generate bio'}), 500

if __name__ == '__main__':
    app.run(debug=True)