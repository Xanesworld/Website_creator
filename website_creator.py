import webbrowser
import os
from datetime import datetime

# Function to create a basic HTML website
def create_website():
    # Define the HTML content with live date and time using JavaScript
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Xane's World</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
            }
            header {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                font-size: 1.5em;
            }
            main {
                padding: 20px;
            }
            footer {
                background-color: #333;
                color: white;
                padding: 10px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
            #datetime {
                font-size: 1.2em;
            }
        </style>
        <script>
            function updateDateTime() {
                const now = new Date();
                document.getElementById('datetime').textContent = now.toLocaleString();
            }
            setInterval(updateDateTime, 1000);
        </script>
    </head>
    <body onload="updateDateTime()">
        <header>Welcome to Xane's World</header>
        <main>
            <h1>Hi, Xane!</h1>
            <p>The live date and time is:</p>
            <p id="datetime"></p>
        </main>
        <footer>&copy; 2025 Xane's World</footer>
    </body>
    </html>
    """

    # Save the HTML content to a file
    file_name = "xane_world.html"
    with open(file_name, "w") as file:
        file.write(html_content)

    # Open the website in the default browser
    webbrowser.open(f"file://{os.path.abspath(file_name)}")

# Create the website
if __name__ == "__main__":
    create_website()
