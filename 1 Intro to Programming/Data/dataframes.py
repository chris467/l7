import pandas as pd

tscore = pd.DataFrame({'Team': ['a', 'a', 'b', 'b', 'c', 'c'], 'Score': [2, 4, 0, 5, 5, 10]})


customers = pd.DataFrame({
    'ID':['CS111','CS222','CS333','CS444','CS555'],
    'Name':['Rachel','Dee','Kris','Isabell','Robyn'],
    'Age':[30,25,45,65,32],
    'Product_ID':['101','NA','105','101','103'],
})

products = pd.DataFrame({
    'Product_ID':['101','102','103','104','105'],
    'Product_name':['Watch','Bag','Shoes','Smartphone','Books'],
    'Category':['Fashion','Fashion','Fashion','Electronics','Education'],
    'Price':[300,50,110,1490,14],
})

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
         
