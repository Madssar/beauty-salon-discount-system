class Customer:
    global memberShips
    memberShips = ["Premium","Gold","Silver"]
    def __init__(self,name,memberType=''):
        self.__Name= name
        self.__MemberType = memberType
        
    def __repr__(self):
         return f"\nName:{self.__Name}\nMembership:{self.__MemberType}"

    @property
    def isMember(self):
        '''
        check if given memberType is present in available list or not

        Returns
        -------
        bool
            if MemberType present return True else False.

        '''
        if self.__MemberType in memberShips:
            return True
        else:
            print("\nInvalid Membership")
            return False
    
        
    def getName(self):
        return self.__Name
    
    def setName(self,name):
        self.__Name=name

    def getMemberType(self):
        return self.__MemberType
    
    def setMemberType(self,memberType):
        self.__MemberType = memberType
        
    def addMembership(self):
        '''
        ask for membership name you want to add and append it into memberShips list and print new list

        '''
        memberShipName = input("Enter the name of membership:")
        memberShips.append(memberShipName) #adding new membership at end of list
        print(f'Now the list of membership is:{memberShips}')