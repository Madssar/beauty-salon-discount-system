import customer
import discountRate
from datetime import date


class Visit():
    global todayDate
    todayDate = date.today()

    def __init__(self, customer, date, serviceExpense, productExpense):
        self.__Customer = customer
        self.__Date = date
        self.__ServiceExpense = serviceExpense
        self.__ProductExpense = productExpense

    def __repr__(self):
        return f'\nDate:{self.__Date}\nService Expense:{self.__ServiceExpense}\nProduct Expense:{self.__ProductExpense}'

    def getServiceExpense(self):
        return self.__ServiceExpense

    def setServiceExpense(self, serviceExpense):
        self.__ServiceExpense = serviceExpense

    def getProductExpense(self):
        return self.__ProductExpense

    def setProductExpense(self, productExpense):
        self.__ProductExpense = productExpense

    def getTotalExpense(self):
        '''
        if customer is member then go in DiscountRate class and check memberType and return discount rate according
        to member type and multiply it with service or product expense and return total bill.
        if customer is not member then just return total bill by aggregating service expense and product expense.

        '''
        if self.__Customer.isMember == True:
            servicesDiscount = discountRate.DiscountRate.getServiceDiscRate(
                self.__Customer.getMemberType())
            totalServicesDisc = self.__ServiceExpense * servicesDiscount

            productDiscount = discountRate.DiscountRate.getProductDiscRate(
                self.__Customer.getMemberType())
            totalProductDisc = self.__ProductExpense * productDiscount

            totalDiscount = totalServicesDisc + totalProductDisc

            totalBill = f'\nYour Total Bill after {self.__Customer.getMemberType()} membership discount is:{(self.__ServiceExpense + self.__ProductExpense) - totalDiscount}'
            return totalBill
        else:
            totalBill = f'\nYour Total Bill is:{self.__ServiceExpense + self.__ProductExpense}'
            return totalBill


try:
    name = input('Enter the name:').capitalize()
    membership = input('Enter the membership:').capitalize()
    servicePurchased = int(input('Enter total cost of Services Purchased:'))
    productPurchased = int(input('Enter total cost of Product Purchased:'))
    
    customer_obj = customer.Customer(name, membership)
    visit_obj = Visit(customer_obj, todayDate, servicePurchased, productPurchased)
    print(customer_obj, visit_obj, visit_obj.getTotalExpense())
    
except ValueError:
    print("Please enter valid values")
