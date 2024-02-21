import os
from flask import Flask, request, jsonify
import openai
from Tab3 import content_generation
from Tab1 import content_extraction
from Tab2 import generate_keywords
from Tab4 import *
from flask_cors import CORS

# Define the Flask app
app = Flask(__name__)
CORS(app)


# Define the API endpoint
@app.route('/topics', methods=["POST"])
def summarize_api():
    try:
        
    # Get the text from the request body
        data = request.get_json()
        result3 = content_extraction(data['reference1'], data['reference2'], data['reference3'])
    # Return the summary as JSON
        return jsonify(result3)
    except Exception as er:
        return jsonify({"Error":str(er)})


@app.route('/keyword', methods=['POST'])
def generate_kw():
    try:
        
        data2 = request.get_json()
    
        result2 = generate_keywords(data2['reference1'], data2['reference2'], data2['reference3'], data2['Topic'], data2['Keywords'])
        return jsonify(result2)
    except Exception as e2:
        return jsonify({"Error":str(e2)})
    
@app.route('/tab3', methods=['POST'])
def generate_content():
    try:
        
        data3 = request.get_json()
    
        result3 = content_generation(data3['reference1'], data3['reference2'], data3['reference3'], data3['Topic'], data3['finalized_keyword'], data3['content_type'])
    
        return jsonify(result3)
    except Exception as e3:
        return jsonify({"Error":str(e3)})

@app.route('/tab4', methods=['POST'])
def generate_style():
    try:
        
        data4= request.get_json()
        result4 = style_generation(data4['reference1'], data4['reference2'], data4['reference3'], data4['Topic'], data4['Title'], data4['finalized_keyword'], data4['style'])
    
        return jsonify(result4)
    
    except Exception as e4:
        return jsonify({"Error":str(e4)})




# Run the Flask app
if __name__ == "__main__":
    app.run()
