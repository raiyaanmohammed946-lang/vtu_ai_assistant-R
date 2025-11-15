from flask import Flask, jsonify, request, send_from_directory, render_template
import os, json

app = Flask(__name__, static_folder='static', template_folder='templates')

# Simple in-memory dataset (starter). You can expand these JSONs.
DATA = {
    "syllabus": {
        "CS101": ["Unit 1: Intro", "Unit 2: Data Structures", "Unit 3: Algorithms"]
    },
    "notes": {
        "CS101": {
            "Unit 1": "Short notes for Unit 1: basics of computing...",
            "Unit 2": "Short notes for Unit 2: arrays, lists..."
        }
    },
    "pyqs": {
        "CS101": ["Q1: Explain...", "Q2: Write program..."]
    },
    "labs": {
        "CS101": [
            {"title":"Lab1 - Hello Python", "code":"print('Hello VTU')", "explanation":"Prints greeting"}
        ]
    }
}

@app.route('/api/search')
def api_search():
    q = request.args.get('q','').lower()
    results = {"syllabus":[], "notes":[], "pyqs":[], "labs":[]}
    if not q:
        return jsonify(results)
    # very simple search through values
    for k,v in DATA.items():
        for key,item in (v.items() if isinstance(v, dict) else enumerate(v)):
            text = json.dumps(item).lower() if not isinstance(item, dict) else json.dumps(item).lower()
            if q in text or q in str(key).lower():
                results.setdefault(k, []).append({str(key): item})
    return jsonify(results)

@app.route('/api/data/<category>')
def api_data(category):
    return jsonify(DATA.get(category, {}))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
