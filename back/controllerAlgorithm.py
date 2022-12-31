from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import numpy as np

def regresionLineal(x_name, y_name,prediccion,data):
    
    try:
        x = data[x_name].values.reshape(-1,1)
        y = data[y_name].values.reshape(-1,1)
        # inicializacion de modelo de regresion lineal
        model = LinearRegression().fit(x, y)
        y_prediccion = model.predict(x)
        # calculo del rmse y r^2
        rmse = np.sqrt(mean_squared_error(y, y_prediccion))
        r2 = r2_score(y,y_prediccion)
        y_new_pred = None
        # prediccion del nuevo dato
        if prediccion != "":
            new_y = model.predict([[int(prediccion)]])
            y_new_pred = new_y[0][0]
        
        # generar grafica
        graph, ax = plt.subplots(layout='constrained')
        # print("RMSE: ", rmse)
        # print("r2: ", r2)
        # print("predic: ", y_new_pred)
        ax.scatter(x,y)
        ax.plot(x,y_prediccion,color='red')
        ax.set_title("Gráfica de regresion lineal")
        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        plt.show()

        return [rmse,r2,y_new_pred]
                  
    # out = io.BytesIO()
    # FigureCanvas(graph).print_png(out)
    # print(out.getvalue())

    except :
        print("Error en parametros o generar grafica. ")

    

    # print("regresionLineal")
    

def regresionPolinomial():
    print("regresionPolinomial")

def clasificadorGaussiano():
    print("gaussiano")