class MedicalClinic:
    def __init__(self):
        self.patients = {}
        self.schedule = {}

    def add_patient(self, id, name, family_name, age, height, weight):
        if id in self.patients:
            return "error: this ID already exists"

        if age < 0:
            return "error: invalid age"

        if height < 0:
            return "error: invalid height"

        if weight < 0:
            return "error: invalid weight"

        self.patients[id] = {"name": name, "family_name": family_name, "age": age, "height": height, "weight": weight}
        return "patient added successfully"

    def display_patient(self, id):
        if id not in self.patients:
            return "error: invalid ID"

        patient_info = self.patients[id]
        return f"patient name: {patient_info['name']}\npatient family name: {patient_info['family_name']}\npatient age: {patient_info['age']}\npatient height: {patient_info['height']}\npatient weight: {patient_info['weight']}"

    def add_visit(self, id, beginning_time):
        if id not in self.patients:
            return "error: invalid id"

        if not (9 <= beginning_time <= 18):
            return "error: invalid time"

        if beginning_time in self.schedule:
            return "error: busy time"

        self.schedule[beginning_time] = self.patients[id]
        return "visit added successfully!"

    def delete_patient(self, id):
        if id not in self.patients:
            return "error: invalid id"

        del self.patients[id]

        for time, patient_info in list(self.schedule.items()):
            if patient_info["id"] == id:
                del self.schedule[time]

        return "patient deleted successfully!"

    def display_visit_list(self):
        schedule_output = "SCHEDULE:\n"
        for time, patient_info in sorted(self.schedule.items()):
            schedule_output += f"{time:02d}: {patient_info['name']} {patient_info['family_name']}\n"
        return schedule_output.strip()


clinic = MedicalClinic()

commands = []

command = input()
while command != 'exit':
    commands.append(command)
    command = input()

for command in commands:
    parts = command.split()
    if parts[0] == "add":
        result = clinic.add_patient(int(parts[2]), parts[3], parts[4], int(parts[5]), int(parts[6]), int(parts[7]))
    elif parts[0] == "display":
        if parts[1] == "patient":
            result = clinic.display_patient(int(parts[3]))
        elif parts[1] == "visit":
            result = clinic.display_visit_list()
    elif parts[0] == "add" and parts[1] == "visit":
        result = clinic.add_visit(int(parts[3]), int(parts[4]))
    elif parts[0] == "delete" and parts[1] == "patient":
        result = clinic.delete_patient(int(parts[3]))
    elif parts[0] == "exit":
        break
    else:
        result = "invalid command"

    print(result)
