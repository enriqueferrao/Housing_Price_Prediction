from flask import Flask, request, jsonify
import data_handler
app = Flask(__name__)

@app.route('/get_locations')
def get_locations():
    response = jsonify({
        'locations' : data_handler.get_locations()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/predict_price', methods=['GET','POST'])
def predict_price():
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    bhk = int(request.form['bhk'])

    print(location,total_sqft,bath,balcony,bhk)

    response = jsonify({
        'predicted_price' : data_handler.make_predictions(location,total_sqft,bath,balcony,bhk)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
   
    return response

if __name__== "__main__":
    data_handler.load_columns_data()
    print("Starting Python FLask server...")
    app.run()