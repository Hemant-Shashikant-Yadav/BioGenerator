"""
This Flask web application provides an API endpoint to generate a unique and engaging dating profile bio based on user-provided information.

The `generate_prompt` function takes a dictionary of user data (career, personality, interests, hobby, and relationship goal) and generates a prompt for the language model to use in generating the bio.

The `/generate-bio` route accepts a POST request with the user data, generates a prompt, and uses the Groq language model to generate a 2-3 sentence bio. The generated bio is then returned as a JSON response.

The application also includes a home route (`/`) that renders the index.html template.
"""
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)
 
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
        
        prompt = generate_prompt(data)
        
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
        
        generated_bio = completion.choices[0].message.content.strip()
        
        return jsonify({'bio': generated_bio})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to generate bio'}), 500

if __name__ == '__main__':
    app.run()