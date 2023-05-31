from flask import Flask, request
import requests

app = Flask(__name__)

sheetsdb_url = 'https://sheetdb.io/api/v1/pi6be28suam8z'

@app.route('/process-user-input', methods=['POST'])
def process_user_input():
    user_input = request.form['SpeechResult']
    
    data = {
        'input': user_input
    }
    
    try:
        response = requests.post(sheetsdb_url, json=data)
        if response.status_code == 201:
            return "User input saved successfully in SheetsDB API."
        else:
            return "Error saving user input in SheetsDB API."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
