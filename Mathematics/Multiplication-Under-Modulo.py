def multiplicationUnderModulo(a,b):
    '''
    :param a: given value of a
    :param b: given value of b
    :return: Integer , sum under modulo
    '''   
    M = 1000000007
    # code here
    return((a%M) * (b%M))%M


