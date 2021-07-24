from flask import Flask, request, render_template
import requests
from flask_cors import cross_origin
import pickle

app = Flask(__name__)
model = pickle.load(open("used-car-pred.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        #Numerical Columns

        # Year
        Year = float(request.form["Year"])

        # Kilometers_Driven
        Kilometers_Driven = float(request.form["Kilometers_Driven"])
        
        # Mileage
        New_Mileage = float(request.form["Mileage"])

        # Engine
        Engine = float(request.form["Engine"])

        # Power
        Power = float(request.form["Power"])
        
        # Seats
        Seats = float(request.form["Seats"])

        #Categorical Columns
        
        # Location
        location=request.form['Location']
        if(location=='Bangalore'):
            Bangalore = 1
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 0

        elif(location=='Chennai'):
            Bangalore = 0
            Chennai = 1
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 0

        elif(location=='Coimbatore'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 1
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 0
            
        elif(location=='Delhi'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 1
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 0
            
        elif(location=='Hyderabad'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 1
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 0
        
        elif(location=='Jaipur'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 1
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 0
        
        elif(location=='Kochi'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 1
            Kolkata = 0
            Mumbai = 0
            Pune = 0
            
        elif(location=='Kolkata'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 1
            Mumbai = 0
            Pune = 0
            
        elif(location=='Mumbai'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 1
            Pune = 0
        elif(location=='Pune'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 1
            
        elif(location=='Ahmedabad'):
            Bangalore = 0
            Chennai = 0
            Coimbatore = 0
            Delhi = 0
            Hyderabad = 0
            Jaipur = 0
            Kochi = 0
            Kolkata = 0
            Mumbai = 0
            Pune = 0
            
        #Fuel_Type
        fuel_type=request.form['Fuel_Type']
        if(fuel_type=='Diesel'):
            Diesel = 1
            LPG = 0
            
        elif(fuel_type=='LPG'):
            Diesel = 0
            LPG = 1
            
        elif(fuel_type=='CNG'):
            Diesel = 0
            LPG = 0
        
        #Transmission
        transmission=request.form['Transmission']
        if transmission == "Manual":
            Manual = 1
        elif transmission == "Automatic":
            Manual = 0
            
        brand=request.form['Brand']
        if brand == "BMW":
            BMW = 1
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0

        elif brand == "Bentley":
            BMW = 0
            Bentley = 1
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0

        elif brand == "Chevrolet":
            BMW = 0
            Bentley = 0
            Chevrolet = 1
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0

        elif brand == "Datsun":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 1
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
            
        elif brand == "Fiat":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 1
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0

        elif brand == "Ford":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 1
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
            
        elif brand == "Honda":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 1
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Hyundai":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 1
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Isuzu":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 1
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Jaguar":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 1
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Jeep":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 1
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Land":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 1
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
            
        elif brand == "Mahindra":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 1
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
            
        elif brand == "Maruti":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 1
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Mercedes_Benz":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 1
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Mini":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 1
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Mitsubishi":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 1
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Nissan":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 1
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Porsche":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 1
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Renault":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 1
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
        
        elif brand == "Skoda":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 1
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Tata":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 1
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
            
        elif brand == "Toyota":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 1
            Volkswagen = 0
            Volvo = 0
        
        elif brand == "Volkswagen":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 1
            Volvo = 0
        
        elif brand == "Volvo":
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 1
        else:
            BMW = 0
            Bentley = 0
            Chevrolet = 0
            Datsun = 0
            Fiat = 0
            Ford = 0
            Honda = 0
            Hyundai = 0
            ISUZU = 0
            Isuzu = 0
            Jaguar = 0
            Jeep = 0
            Land = 0
            Mahindra = 0
            Maruti = 0
            Mercedes_Benz = 0
            Mini = 0
            Mitsubishi = 0
            Nissan = 0
            Porsche = 0
            Renault = 0
            Skoda = 0
            Tata = 0
            Toyota = 0
            Volkswagen = 0
            Volvo = 0
            
        
        
        prediction=model.predict([[
            Year,
            Kilometers_Driven,
            Engine,
            Power,
            Seats,
            New_Mileage,
            Bangalore,
            Chennai,
            Coimbatore,
            Delhi,
            Hyderabad,
            Jaipur,
            Kochi,
            Kolkata,
            Mumbai,
            Pune,
            Diesel,
            LPG,
            Manual,
            BMW,
            Bentley,
            Chevrolet,
            Datsun,
            Fiat,
            Ford,
            Honda,
            Hyundai,
            ISUZU,
            Isuzu,
            Jaguar,
            Jeep,
            Land,
            Mahindra,
            Maruti,
            Mercedes_Benz,
            Mini,
            Mitsubishi,
            Nissan,
            Porsche,
            Renault,
            Skoda,
            Tata,
            Toyota,
            Volkswagen, 
            Volvo
            ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Used Car Price is INR Laks {}".format(output))

    
    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=False)