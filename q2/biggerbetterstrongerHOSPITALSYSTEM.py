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

    def display_patient_type(self):
        return "Regular Patient"

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.80
    def display_patient_type(self):
        return "Senior Citizen"

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85
    def display_patient_type(self):
        return "PhilHealth Member"


regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patients = [regular_patient,senior_patient,philhealth_patient]
print(f"Hospital Billing System\n-----------------------")

for i in patients:
    print(f"Patient Name: {i.get_name()}")
    print(f"Patient Type: {i.display_patient_type()}")
    print(f"Original Bill: ₱{i.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{i.calculate_bill():,.2f}\n")
