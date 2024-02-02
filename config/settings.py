```python
# config/settings.py

# Database settings
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'password',
    'database': 'programmer_hiring'
}

# ChatGPT settings
CHATGPT_CONFIG = {
    'api_key': 'your_openai_api_key',
    'model_name': 'gpt-3.5-turbo'
}

# Hiring service settings
HIRING_SERVICE_CONFIG = {
    'max_candidates': 5,
    'interview_questions': [
        'What is your main programming language?',
        'How many years of experience do you have?',
        'What is your preferred development environment?',
        'Can you describe a challenging programming task you recently faced?',
        'How do you handle tight deadlines?'
    ]
}
```