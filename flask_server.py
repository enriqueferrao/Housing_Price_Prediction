from flask import Flask, request, jsonify, render_template
import data_handler
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# TODO : When the flask server is run the index.html file should show on the route

# ! : It gives a server error
# ! : Also check port 5500 in use error

@app.route('/get_locations')
def get_locations():
    response = jsonify({
        'locations' : data_handler.get_locations()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    bhk = int(request.form['bhk'])

    print(location,total_sqft,bath,balcony,bhk)

    # response = jsonify({
    #     'predicted_price' : data_handler.make_predictions(location,total_sqft,bath,balcony,bhk)
    # })

    # response.headers.add('Access-Control-Allow-Origin','*')
   
    # return response
    output = data_handler.make_predictions(location,total_sqft,bath,balcony,bhk)

    return render_template('index.html', prediction_text='Estimated House Price should be Rs. {} Lakh'.format(output))

if __name__== "__main__":
    data_handler.load_columns_data()
    print("Starting Python FLask server...")
    app.run(host='127.0.0.1', port=5501)