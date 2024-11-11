from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def show_items():
    # Read data from items.json
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        items = []  # Fallback if JSON file is missing or corrupt

    # Pass items to the template
    return render_template('items.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)
