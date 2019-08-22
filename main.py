import matplotlib.pyplot as plt
from random import randint

def main():
    
    total = 1000
    monthly_total = []
    net_income = 0
    
    months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    
    for i in range(12):
        
        income = randint(800,1000)
        bills = randint(800,1050)
        
        net_income += (income - bills)
        
        monthly_total.append(total + net_income)
        
    plt.xticks([i for i in range(12)],months)
    plt.plot([i for i in range(12)],monthly_total)
    plt.show()
    
main()