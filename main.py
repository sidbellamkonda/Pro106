import csv
import numpy as np 
import plotly.express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x": coffee, "y": sleep}

def findCorrolation(dataSource):
    corrolation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corrolation between coffee and hours of sleep: \n ", corrolation[0, 1])

def main():
    data_path = "pro106.csv"
    dataSource = getDataSource(data_path)
    findCorrolation(dataSource)
    plotFigure(data_path)

main()