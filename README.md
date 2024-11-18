# Bio Generator

A Flask-based web application that generates personalized dating profile bios using AI. The application takes user inputs like career, personality traits, interests, hobbies, and relationship goals to create unique and engaging bios.

Live Demo: [Bio Generator on Render](https://biogenerator-ihcg.onrender.com)

## Features

- **Personalized Bio Generation**: Creates unique bios based on user preferences
- **Multiple Input Categories**: 
  - Career/Profession
  - Personality Traits
  - Interests
  - Hobbies
  - Relationship Goals
- **AI-Powered**: Uses Groq's LLaMa 3 70B model for natural and engaging bio generation
- **Responsive Design**: Works seamlessly across different devices
- **User-Friendly Interface**: Simple and intuitive UI for easy interaction

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: Groq's LLaMa 3 70B
- **Hosting**: Render.com
- **Environment Variables**: python-dotenv
- **API Handling**: Flask REST API

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Hemant-Shashikant-Yadav/BioGenerator.git
cd BioGenerator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
BioGenerator/
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── .env               # Environment variables
├── .gitignore        # Git ignore file
├── app.py            # Main application file
├── LICENSE          # License file
├── README.md        # Project documentation
├── requirements.txt  # Python dependencies
└── vercel.json      # Vercel configuration
```

## API Endpoints

### Generate Bio
- **URL**: `/generate-bio`
- **Method**: `POST`
- **Data Params**:
  ```json
  {
    "career": "string",
    "personality": "string",
    "interests": "string",
    "hobby": "string",
    "relationship_goal": "string"
  }
  ```
- **Success Response**:
  ```json
  {
    "bio": "Generated bio text"
  }
  ```
- **Error Response**:
  ```json
  {
    "error": "Failed to generate bio"
  }
  ```

## Environment Variables

The following environment variables are required:

- `GROQ_API_KEY`: Your Groq API key for accessing the LLaMa 3 model

## Deployment

The application is deployed on Render.com. To deploy your own instance:

1. Create a new account on [Render](https://render.com)
2. Connect your GitHub repository
3. Create a new Web Service
4. Configure the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Add your environment variables in the Render dashboard
6. Deploy the application

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Sample Bios

Here are some example bios that the application can generate:

- **The Creative Professional**: "Tech-savvy software engineer with a creative twist. When I'm not coding, you'll find me strumming my guitar or exploring local art galleries. Seeking a kindred spirit who appreciates both logic and creativity."

- **The Active Explorer**: "Adventure-seeking photographer who finds beauty in unexpected places. Passionate about hiking, rock climbing, and capturing nature's wonders. Looking for someone to share thrilling experiences and quiet moments alike."

- **The Cultural Enthusiast**: "Multilingual teacher with an insatiable curiosity for different cultures. Love cooking international cuisines and attending cultural festivals. Hoping to meet someone who shares my passion for learning and global adventures."

## Contact

Hemant Yadav - [GitHub](https://github.com/Hemant-Shashikant-Yadav)

Project Link: [https://github.com/Hemant-Shashikant-Yadav/BioGenerator](https://github.com/Hemant-Shashikant-Yadav/BioGenerator)
