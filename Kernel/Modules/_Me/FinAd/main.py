def main(age, risk_tolerance):
    '''
    This function returns the optimal portfolio allocation.
    '''
    if risk_tolerance == 'low':
        bond_allocation = 100
        stock_allocation = 0

    elif risk_tolerance == 'medium':
        if age < 50:
            bond_allocation = 50
            stock_allocation = 50
        else:
            bond_allocation = 70
            stock_allocation = 30

    elif risk_tolerance == 'high':
        if age < 50:
            bond_allocation = 10
            stock_allocation = 90
        else:
            bond_allocation = 20
            stock_allocation = 80
    
    return bond_allocation, stock_allocation
