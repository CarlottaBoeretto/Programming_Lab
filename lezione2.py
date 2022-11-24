my_list=[1,2,3,4,5,6]
def sum_list(my_list):
    somma=0
    for item in my_list:
        somma=somma+item
    return somma

print('la somma dei numeri è: {}'.format(sum_list(my_list)))
    