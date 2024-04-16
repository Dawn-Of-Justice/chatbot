# Chatbot 

## Introduction
This repository contains the code for a chatbot developed using Python. The chatbot is designed to interact with users, answer questions based on provided documents, and provide a user-friendly interface.

## Features
- **Document-Based Question Answering**: The chatbot is capable of answering questions based on the content of a specified document. It utilizes advanced natural language processing techniques to understand and respond to user queries effectively.
- **User Interface**: The chatbot comes with a simple and intuitive user interface built using Flask framework, allowing users to interact with the bot seamlessly through a web browser.
- **Contextual Understanding**: The chatbot incorporates contextual understanding by providing pieces of context from the document to assist in generating accurate responses to user queries.

## Installation
To run the chatbot locally, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Make sure you have the necessary API key for Google's services and set it as an environment variable named `API_KEY`.
4. Ensure that the document you want the chatbot to reference is available and provide its filename or path accordingly in the code.

## Usage
To use the chatbot, execute the `app.py` file. This will start the Flask server and make the chatbot accessible through a web browser. Users can then interact with the chatbot by entering their queries in the provided input box and receiving responses in real-time.

## Code Structure
- `bot.py`: Contains the implementation of the chatbot class, including methods for initializing the chatbot, preparing the document for question answering, and handling user queries.
- `app.py`: Implements the Flask web application for the chatbot's user interface. It handles user requests, interacts with the chatbot backend, and renders the HTML templates.
- `templates/chat.html`: HTML template for the chat interface, allowing users to input queries and display bot responses.

## Configuration
- **Document**: Specify the document filename or path in the `app.py` file to define the document the chatbot will reference for question answering.
- **API Key**: Ensure that you have a valid Google API key and set it as an environment variable named `API_KEY` for accessing Google's services.

## Dependencies
- `dotenv`: For loading environment variables from a `.env` file.
- `langchain_google_genai`: Provides access to Google's Generative AI for natural language processing tasks.
- `Flask`: Web framework used for building the chatbot's user interface.
- `PyPDF2`: Library for reading PDF files and extracting text content.

## Contributors
- [Salo Soja Edwin]: Developer of the chatbot.

## License
This project is licensed under [MIT] - see the [LICENSE](LICENSE) file for details.
