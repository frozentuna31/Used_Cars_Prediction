# Used Cars Prediction

## Table of Contents:

- [Overview](#Overview)
- [Website and Demo](#Website)
- [Installation](#Installation)
- [Deployment](#Deployment)
- [Directory Tree](#Tree)
- [Packages Used](#Packages)
- [Bug / Issue](#Bug)
- [Dataset's Source and Notebook](#Source)
- [Future Development](#Development)

## Overview <a name="Overview"></a>

This is a Flask web app that predicts price of used car in India. It has ten columns, i.e. Car's brand, car's transmission, and many more. 
These columns can be customized to the car spesification that is suitable for you. After clicking submit, the web app will use 
the machine learning model for predicting the most appropriate used car price. 

## Website and Demo <a name="Website"></a>

Link: https://used-car-pred.herokuapp.com 
\
\
![messageImage_1627202649899](https://user-images.githubusercontent.com/69710173/126893249-c0b4c1bd-1281-40ca-80ce-e5053b8a0067.jpg)
![messageImage_1627202665512](https://user-images.githubusercontent.com/69710173/126893248-5a00c156-2706-4316-b1b0-47a1a123a920.jpg)
![Used Car Prediction - Google Chrome 2021-07-25 13-56-59](https://user-images.githubusercontent.com/69710173/126893866-b6fc9c14-cba0-4b09-aa10-6b1ba64623c5.gif)

## Installation <a name="Installation"></a>

Code is made in python 3.8.5 which you can install [here](https://www.python.org/downloads/). If you have lower version of Python, you can upgrade it with pip packages. To install the needed packages, 
run this code in directory after [cloning](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) the repository:

```
pip install -r requirements.txt
```

## Deployment <a name="Deployment"></a>

![messageImage_1627203393353](https://user-images.githubusercontent.com/69710173/126894631-6a6b0a78-c8c8-4407-852c-15698d269258.jpg)
\
\
For deployment, Heroku is helping for providing the place. Log in or sign up to Heroku in order to make project app [here](https://www.heroku.com/). You can deploy this project with 
connecting to Github or deploy it manually by downloading Heroku CTL. After that, you could do the instruction in the following [Heroku Documentation](https://devcenter.heroku.com/categories/deployment) 
to deploy the web app. 

## Directory Tree <a name="Tree"></a>
```
├── template
│   ├── home.html
├── Procfile
├── Used Car Prediction.ipynb
├── README.md
├── app.py
├── requirements.txt
├── test-data.csv
├── train-data.csv
├── used-car-pred.pkl
```

## Packages Used <a name="Packages"></a>

![download](https://user-images.githubusercontent.com/69710173/126894305-2bab7d98-f710-4310-b9fe-9eb45d03e364.png) ![download (1)](https://user-images.githubusercontent.com/69710173/126894331-e09c0ea7-1017-458e-b5ea-c117f21b9f2a.png) 
![download (2)](https://user-images.githubusercontent.com/69710173/126894349-15d993db-ee9c-499b-baad-810fb8196ad9.png)

## Bug / Issue <a name="Bug"></a>

If someone found a bug (the web gives unwanted results or some errors), please open an issue [here](https://github.com/frozentuna31/Used_Cars_Prediction/issues) by including your search query and desired result.

## Dataset's Source and Notebook <a name="Source"></a>

The train and test dataset is taken from Kaggle, if you want to see the source of those dataset or the dataset analysis in kaggle notebook, check out here:
- [Source](https://www.kaggle.com/avikasliwal/used-cars-price-prediction)
- [Kaggle notebook](hhttps://www.kaggle.com/studyvortex/used-car-prediction-elastic-net-lasso-rforest)

## Future Development <a name="Development"></a>

Some feature that can be developed in the future:
- Utilize more models and method
- Optimizing the flask application
- Give a better front-end display
