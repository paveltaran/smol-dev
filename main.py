```python
from flask import Flask, request
from agent import Agent
from database import connect_to_db
from config import DATABASE_URI, TOKEN

app = Flask(__name__)
agent = Agent(TOKEN)
connect_to_db(DATABASE_URI)

@app.route('/hire', methods=['POST'])
def hire_programmer():
    hire_request = request.get_json()
    hire_response = agent.handle_request(hire_request)
    return hire_response

if __name__ == "__main__":
    app.run(debug=True)
```