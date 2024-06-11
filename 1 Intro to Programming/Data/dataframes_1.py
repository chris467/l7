import pandas as pd

students = pd.DataFrame({"Name": ["Jesse", "Kotryna", "Xiaoyi", "David"], 
                         "Subject": ["Physics", "Biochemistry", "Chemistry", "Medicine"]})

residents = pd.DataFrame({"Name": ["Jesse", "Kotryna", "Xiaoyi", "Raoul"], 
                          "Age": [21, 22, 23, 29]})

dimensions = pd.DataFrame({"length (cm)": [500, 220, 150],
                          "width (cm)": [450, 250, 800]})


europe = pd.DataFrame({"location_id": [1, 2, 3, 4], 
                          "Country": ["UK", "Italy", "France", "Germany"], 
                          "City": ["Cambridge", "Sanremo", "Paris", "Berlin"]})

americas = pd.DataFrame({"location_id": [1, 2, 3, 4], 
                          "Country": ["Argentina", "Brazil", "USA", "USA"], 
                          "City": ["Buenos Aires", "Rio", "New York", "San Francisco"]})

dublin = pd.DataFrame({"location_id": ["5"], 
                       "Country": ["Ireland"], 
                       "City": ["Dublin"]
                      })

requirements = pd.DataFrame({"name": ["table", "chair", "coffee machine"],
                          "quantity": [30, 100, 2]})

prices = pd.DataFrame({"name": ["table", "chair", "coffee machine"],
                        "price": [50, 20, 1000]})


currencies = pd.DataFrame({"country": ["UK", "Ireland", "Italy", "France", "Germany", "Argentina", "Brazil", "USA"],
                           "currency": ["Pound", "Euro", "Euro", "Euro", "Euro", "Peso", "Real", "Dollar"]
                          })

exchange_rates = {"Pound": 1.0, 
         "Euro": 1.2,
         "Dollar": 1.4,
         "Peso": 94.2,
         "Real": 6.8,
        }
         
