# weather-forecating-using-ML
This project is a simple weather forecasting web application built using machine learning. It predicts the temperature based on historical weather data such as humidity, wind speed, and atmospheric pressure.
The trained model is connected to a Flask web application, allowing users to enter values and instantly see the predicted temperature.

Technologies Used

  1.Python 
  
  2.Flask 
  
  3.Machine Learning (scikit-learn) 
  
  4.pandas, NumPy 
  
  5.HTML, CSS

For running this project use this commands after setting up the files 

1.pip install -r requirements.txt

2.python train_model.py

3.python app.py

Ater running the above command the localhost link will be generated , by clicking the generated link and providing the 

1.humidity level - range 0 to 1 (min = 0 , max = 1, ex: 0.05), 

2.wind speed - range 0 to 150 (min = 0 , max = 150) , 

3.pressure - range 870 to 1085 (min = 870 , max = 1085)

as the input then click predict temperature . the predicted temperature will be given as the output.
