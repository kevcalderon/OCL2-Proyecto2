from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
import io
import numpy as np
from globalArray import graphArray

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
        graphArray.append(graph)
        return [rmse,r2,y_new_pred]
                  
    except :
        print("Error en parametros o generar grafica. ")


def regresionPolinomial(x_name,y_name,prediccion,data):
    x = data[x_name].values.reshape(-1,1)
    y = data[y_name].values.reshape(-1,1)
    poly = PolynomialFeatures(degree=2, include_bias=False)

    x_poly = poly.fit_transform(x)
    
    model = LinearRegression()
    model.fit(x_poly,y)
    y_pred = model.predict(x_poly)
    y_new_pred = None
    if prediccion != "":
        x_polyPred = poly.fit_transform([[int(prediccion)]])
        new_y = model.predict(x_polyPred)
        y_new_pred = new_y[0][0]
    
    rmse = np.sqrt(mean_squared_error(y,y_pred))
    r2 = r2_score(y,y_pred)

    # generar grafica
    graph, ax = plt.subplots(layout='constrained')
    ax.scatter(x,y)
    ax.plot(x,y_pred,color='red')
    ax.set_title("Gráfica de regresion polinomial")
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    graphArray.append(graph)
    return [rmse,r2,y_new_pred]

def clasificadorGaussiano(x_name,y_name,prediccion,data):
    # x, y = load_iris(return_X_y=True)
    # print("X", x)
    # print("Y", y)
    x = np.array(data[x_name]).reshape(-1,1)
    y = np.array(data[y_name]).reshape(-1,1)
    le = preprocessing.LabelEncoder()
    y_enco = le.fit_transform(y)
    feature = list(zip(y_enco))

    clf = GaussianNB()
    # X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)
    clf.fit(x, feature)
    y_pred = clf.predict(x)
    y_pred2 = clf.predict([[float(prediccion)]])
    print("YPRED: ", y_pred)
    print("YPRED: ", y_pred2)
    print("ACCURACY: ", accuracy_score(y, y_pred))



    # X, y = load_iris(return_X_y=True)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
    # gnb = GaussianNB()
    # y_pred = gnb.fit(X_train, y_train).predict(X_test)
    # print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
    


def arbolDecision(x_name,y_name,prediccion,data):
    # opcion1
    le = preprocessing.LabelEncoder()
    x = np.array(data[x_name]).reshape(-1,1)
    y = np.array(data[y_name]).reshape(-1,1)
    
    y_enco = le.fit_transform(y)
    feature = list(zip(y_enco))
    model = DecisionTreeClassifier().fit(x,feature)
    y_pred = model.predict(x)
    # print("YPRED: ", y_pred)
    y_pred2 = None
    if prediccion != "":
        y_pred2_new = model.predict([[float(prediccion)]])
        y_pred2 = y_pred2_new[0]
    # print("YPRED_NEW: ", y_pred2)
    accuracy = accuracy_score(y, y_pred)
    print("EVALUACION: ", accuracy)
    fig,ax = plt.subplots(layout='constrained')
    plot_tree(model,filled=True)
    ax.set_title("Arbol de decisión.")
    graphArray.append(fig)
    return [y_pred2, accuracy]
    # plt.show()
    
    # opcion2
    # x = data[x_name].values.reshape(-1,1)
    # y = data[y_name].values.reshape(-1,1)
    # X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # model = DecisionTreeClassifier()
    # model.fit(X_train, y_train)
    # y_pred = model.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)


    # fig, ax = plt.subplots(layout='constrained')
    # plot_tree(model, filled=True)
    # plt.show()
    # print("EVALUACION: ", accuracy)
    # pass

def redesNeuronales(x_name,y_name,prediccion,data):
    pass