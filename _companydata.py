class Care:
    def __init__(self, company_name, address, phone):
        self.company_name = company_name
        self.address = address
        self.phone = phone
        self.manager = []  # Initialize with an empty list
        self.region = []
        self.staff = []
       
       
    def __len__(self):
        return len(self.manager)
    

    def __str__(self):
       return f"Company name: { self.company_name}\nAddress: {self.address}\nContact Number: {self.phone}\nManagers: {', '.join(self.manager) if self.manager else 'No managers assigned'}\nRegion: {self.region}"
    

    def get_details(self):
        return f"The Company name is {self.company_name} and is located at {self.address}. you can contact us o {self.phone}"
    
    def add_manager(self, manager):
        managettotal = 5
        if len(self.manager) + 1 <= managettotal:
            self.manager.append(manager)
        else:
            print("Manager limit reached")


    def checkvacancy(self):
        totalstaff = 20
        if(len(self.staff) < 20):
            self.vacancy = True
        else:
            self.vacancy = False
    
    def __setItem__(self, time, value):
        self.daily_note[time] = value



class Region(Care):


    def __init__(self,company_name,address,phone, client_name, location,region ):
        super().__init__(company_name, address, phone)
        self.name = client_name
        self.location = location
        self.team_leader = []
        self.senior_ss = None
        self.staff = []
        self.vacancy = False
        self.region = region
        self.daily_note = {}

    def __len__(self):
        return len(self.staff)
    
    def __str__(self):
       return f"Company name: { self.company_name}\nAddress: {self.address}\nContact Number: {self.phone}\nClient Name: {self.name}\nLocation: {self.location}\nTeamLeader: {', '.join(self.team_leader) if self.team_leader else 'No team leader assigned'}\nSenior Social Worker: {self.senior_ss if self.senior_ss else 'No senior social worker assigned'}\nStaff: {', '.join(self.staff) if self.staff else 'No staff assigned'}\nVacancy: {self.vacancy}\nRegion: {self.region}\nDaily Note: {self.daily_note}"
    
    
    
    def get_details(self):
        return f"The new client is {self.name} and is located at {self.location}.\nThe team leader is {self.team_leader} and the senior social worker is {self.senior_ss}."
    
    def __setItem__(self, time, value):
        self.daily_note[time] = value
     
    

company1 = Care("IBC", "07353532", "Uk")
company1.manager = ["John", "Peter", "James", "Paul"]
company1.add_manager("David")
company1.add_manager("David")
company1.region = ["London", "Manchester", "Birmingham", "Liverpool"]

company1_region1 = Region("IBC", "UK","07373", "Jake", "Woolwich", "London")
company1_region1.team_leader = ["Emma"]
company1_region1.senior_ss = "Gbenga"
company1_region1.staff = ["Tom", "Jerry", "John", "Peter", "James", "Paul", "David"]
company1_region1.checkvacancy()
company1_region1.daily_note[1] = "he had lunch"
print(company1)
print(company1_region1)



    



