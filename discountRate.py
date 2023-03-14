class DiscountRate:
    servicePremium = 0.2
    serviceGold = 0.15
    serviceSilver = 0.1
    productPremium = 0.1
    productGold = 0.1
    productSilver = 0.1

    def getServiceDiscRate(memberType):
        '''
        Parameters
        ----------
        memberType : take it as argument from customer class.

        Returns
        -------
        match the memberType with available memberships and return discount rates of services

        '''
        if memberType == 'Premium':
            return DiscountRate.servicePremium
        elif memberType == 'Gold':
            return DiscountRate.serviceGold
        elif memberType == 'Silver':
            return DiscountRate.serviceSilver
    
    def getProductDiscRate(memberType):
        '''

        Parameters
        ----------
        memberType : take it as argument from customer class.

        Returns
        -------
        match the memberType with available memberships and return discount rates of products

        '''
        if memberType == 'Premium':
            return DiscountRate.productPremium 
        elif memberType == 'Gold':
            return DiscountRate.productGold
        elif memberType == 'Silver':
            return DiscountRate.productSilver
      