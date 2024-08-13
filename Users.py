class Users:

    def __init__(self,Userid,FirstName,LastName,Address,LoginType,FlatVisit,Phone):
        self.Userid=Userid
        self.FirstName= FirstName
        self.LastName=LastName
        self.Address=Address
        self.LoginType=LoginType
        self.FlatVisit=FlatVisit
        self.Phone=Phone

    def visitior_to_dict(self):
        return {
            "userid":self.Userid,
                "FirstName":self.FirstName,
                "LastName":self.LastName,
                "Address":self.Address,
                "LoginType":self.LoginType,
                "FlatVisit":self.FlatVisit,
                "Phone":self.Phone
        }
