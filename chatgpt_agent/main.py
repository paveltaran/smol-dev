```python
import sys
from chatgpt_agent import programmer, database, utils, config

def main():
    db = database.Database(config.DB_CONFIG)
    while True:
        user_input = input("Enter your command: ")
        if user_input.lower() == 'quit':
            break
        elif 'hire programmer' in user_input.lower():
            programmer_info = utils.extract_programmer_info(user_input)
            prog = programmer.Programmer(programmer_info)
            db.insert_programmer(prog)
        elif 'update programmer' in user_input.lower():
            programmer_info = utils.extract_programmer_info(user_input)
            prog = programmer.Programmer(programmer_info)
            db.update_programmer(prog)
        elif 'delete programmer' in user_input.lower():
            programmer_id = utils.extract_programmer_id(user_input)
            db.delete_programmer(programmer_id)
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
```