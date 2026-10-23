class Patient:
    name:str
    bill_amount:float
  
    def __init__(self,name,bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount
        
    def set_bill_amount(self):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85



regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = Patient("Maria Santos", 15000)
philhealth_patient = Patient("Pedro Reyes", 15000)

patients = [regular_patient,senior_patient,philhealth_patient]
print(f"Hospital Billing System\n-----------------------")

for i in patients:
    print(f"Patient Name: {i.get_name()}")
    print(f"Original Bill: ₱{i.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{i.calculate_bill():,.2f}\n")
