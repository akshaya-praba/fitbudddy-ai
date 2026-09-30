import os 
from google import genai 
from dotenv import load_dotenv 
 
load_dotenv() 
 
client = genai.Client( 
    api_key=os.getenv("GOOGLE_API_KEY") 
) 
 
 
def generate_workout_gemini(name, age, weight, goal, intensity): 
 
    prompt = f""" 
Create a simple 7-day workout plan for this person: 
 
Name: {name} 
Age: {age} 
Weight: {weight} kg 
Fitness Goal: {goal} 
Workout Intensity: {intensity} 
 
Give the plan day by day from Day 1 to Day 7. 
Include: 
- Exercise name 
- Sets and repetitions 
- Rest time 
- One simple safety tip 
 
Keep it beginner-friendly and easy to understand. 
""" 
 
    response = client.models.generate_content( 
        model="gemini-3.8-flash",
        contents=prompt 
    ) 
 
    return response.text