# Should be in another file.
class Citizen:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def report_pothole(self, location, severity):
        # Method to report a pothole
        new_pothole = Pothole(location, severity)
        return new_pothole

    def view_pothole_information(self, pothole):
        # Method to view pothole information
        return f"Pothole location: {pothole.location}, Severity: {pothole.severity}, Status: {pothole.status}"

    def view_damage_reports(self):
        # Method to view damage reports
        return
    
    def print_details(self):
        # Method to print user details
        print("Citizen Details:")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")


# Should be in another file.
class Pothole:
    def __init__(self, location, severity, status="Not Repaired"):
        self.location = location
        self.severity = severity
        self.status = status

    def update_status(self, new_status):
        # Method to update pothole status
        self.status = new_status
    
    def print_details(self):
            print(f"    - Location: {self.location}")
            print(f"    - Severity: {self.severity}")
            print(f"    - Status: {self.status}")


# Should be in another file.
class PublicWorks:
    def __init__(self):
        self.potholes = []

    def assign_repair_crew(self, pothole, repair_crew):
        # Method to assign repair crew to a pothole
        pothole.repair_crew = repair_crew
        return f"Repair crew {repair_crew} assigned to pothole at {pothole.location}"

    def update_pothole_status(self, pothole, new_status):
        # Method to update pothole status
        pothole.update_status(new_status)
        
        # TODO: Should check if pothole exists, update status or add as new hole.
        self.potholes.append(pothole)
                
        return f"Pothole status updated to {new_status}"

    def generate_reports(self):
        # Method to generate reports
        return
    
    def print_details(self):
        # Method to print public works details
        print("Public Works Department Details:")
        print(f"Number of potholes: {len(self.potholes)}")
        for pothole in self.potholes:
            pothole.print_details()
            print()

if __name__ == "__main__":    
    # Create citizens
    user1 = Citizen("George", "123 Main St", "508-123-1234")
    user2 = Citizen("Jeremy", "456 Elm St", "555-5678")

    # print various user details
    user1.print_details()
    print()
    user2.print_details()
    print()

    # Create public works department
    public_works = PublicWorks()

    # Citizen reports a pothole
    location = "789 Main St"
    severity = 8
    
    # Citizen would authenticate (login) here
    
    # Assuming the citizen is logged in
    reported_pothole = user1.report_pothole(location, severity)
    #print(f"{user1.name} reported a pothole at {location} with severity {severity}.")

    # Public works updates pothole status
    new_status = "Work in Progress"
    updated_status = public_works.update_pothole_status(reported_pothole, new_status)
    #print(f"Public Works Department updated the status of the pothole to: {new_status}.")
            
    # print public works details
    public_works.print_details()

