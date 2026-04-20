from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

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