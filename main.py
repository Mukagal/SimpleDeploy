from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests
import os

app = FastAPI()

api_key = os.getenv("API_KEY")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>My First Deployment</title>
        </head>
        <body>
            <h1>Hello My FastAPI App is Live!</h1>
            
            <form action="/greet" method="post">
                <input type="text" name="name" placeholder="Enter your name"/>
                <button type="submit">Submit</button>
            </form>
            <a href="/weather">Check Weather</a>
        </body>
    </html>
    """

@app.post("/greet", response_class=HTMLResponse)
def greet(name: str = Form(...)):
    return f"""
    <html>
        <body>
            <h2>Hello, {name}!</h2>
            <a href="/">Go back</a>
        </body>
    </html>
    """

@app.get("/api/hello")
def api_hello():
    return {"message": "Hello from API "}

@app.get("/weather", response_class=HTMLResponse)
def get_weather(city: str = "Almaty"):    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return f"<h3>Error: {data.get('message')}</h3>"

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"""
    <html>
        <body>
            <h2>Weather in {city} </h2>
            <p>Temperature: {temp}°C</p>
            <p>Condition: {description}</p>
            <a href="/">Go back</a>
        </body>
    </html>
    """