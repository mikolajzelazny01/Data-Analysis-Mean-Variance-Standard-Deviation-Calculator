import numpy as np

def calculate(list):
    if len(list) != 9: #test if list consists of 9 elements
        raise ValueError("List must contain nine numbers.")
    
    list = np.array(list).reshape(3,3) #converting input list into a 3x3 numpy array

    mean_values = [list.mean(axis = 0).tolist(), list.mean(axis = 1).tolist(), list.flatten().mean()] #calculatng mean values
    var_values = [list.var(axis = 0).tolist(), list.var(axis = 1).tolist(), list.flatten().var()]     #calculating variance values
    std_values = [list.std(axis = 0).tolist(), list.std(axis = 1).tolist(), list.flatten().std()]     #calculating standard deviation values
    max_values = [list.max(axis = 0).tolist(), list.max(axis = 1).tolist(), list.flatten().max()]     #calculating maximum values
    min_values = [list.min(axis = 0).tolist(), list.min(axis = 1).tolist(), list.flatten().min()]     #calculating minimum values
    sum_values = [list.sum(axis = 0).tolist(), list.sum(axis = 1).tolist(), list.flatten().sum()]     #calculating sum values

    #packing up results into a dictionary
    calculations = {
    'mean': mean_values,
    'variance': var_values,
    'standard deviation': std_values,
    'max': max_values,
    'min': min_values,
    'sum': sum_values
    }

    return calculations