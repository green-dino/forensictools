class BusinessProcess:
    def __init__(self, name):
        self.name = name
        self.functions = []

    def add_function(self, function):
        self.functions.append(function)

class Function:
    def __init__(self, name):
        self.name = name

class ChangeManagementProcess:
    def __init__(self):
        self.problem_identification = BusinessProcess("Problem Identification and Change Initiation")
        self.change_control_record_creation = BusinessProcess("Change Control Record Creation")
        self.communication_and_risk_assessment = BusinessProcess("Communication and Risk Assessment")
        self.documentation_and_evaluation = BusinessProcess("Documentation and Evaluation")
        self.fulfillment_and_closure = BusinessProcess("Fulfillment and Closure")

        self.functions = [
            Function("Function 1"),
            Function("Function 2"),
            Function("Function 3"),
            Function("Function 4"),
            Function("Function 5"),
            Function("Function 6"),
            Function("Function 7"),
            Function("Function 8"),
            Function("Function 9"),
            Function("Function 10"),
            Function("Function 11"),
            Function("Function 12"),
            Function("Function 13"),
            Function("Function 14"),
        ]

        self.problem_identification.add_function(self.functions[0])
        self.problem_identification.add_function(self.functions[1])
        self.problem_identification.add_function(self.functions[2])

        self.change_control_record_creation.add_function(self.functions[3])
        self.change_control_record_creation.add_function(self.functions[4])
        self.change_control_record_creation.add_function(self.functions[5])

        self.communication_and_risk_assessment.add_function(self.functions[6])
        self.communication_and_risk_assessment.add_function(self.functions[7])
        self.communication_and_risk_assessment.add_function(self.functions[8])

        self.documentation_and_evaluation.add_function(self.functions[9])
        self.documentation_and_evaluation.add_function(self.functions[10])

        self.fulfillment_and_closure.add_function(self.functions[11])
        self.fulfillment_and_closure.add_function(self.functions[12])
        self.fulfillment_and_closure.add_function(self.functions[13])

# Create an instance of the ChangeManagementProcess class
change_management_process = ChangeManagementProcess()

# Access individual business processes and functions like this:
print(change_management_process.problem_identification.name)
print(change_management_process.problem_identification.functions[0].name)
