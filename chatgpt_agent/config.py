```python
# chatgpt_agent/config.py

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'password',
    'database': 'chatgpt_agent_db'
}

# OpenAI GPT-3 API configuration
OPENAI_API_CONFIG = {
    'api_key': 'your_openai_api_key'
}

# Configuration for hiring programmers
HIRING_CONFIG = {
    'programming_languages': ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'Go', 'Swift', 'Kotlin'],
    'experience_levels': ['Junior', 'Mid', 'Senior', 'Lead'],
    'locations': ['Remote', 'On-site']
}
```