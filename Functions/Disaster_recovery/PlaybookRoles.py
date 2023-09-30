class User:
    def __init__(self, name):
        self.name = name

class WorkRole:
    def __init__(self, name):
        self.name = name
        self.problems = []
        self.changes = []
        self.requests = []

    def initiate_change(self, change):
        self.changes.append(change)

    def submit_request(self, request):
        self.requests.append(request)

class Problem:
    def __init__(self, name):
        self.name = name
        self.change_control_record = None

    def link_to_change_control_record(self, change_control_record):
        self.change_control_record = change_control_record

class Change:
    def __init__(self, name):
        self.name = name
        self.change_control_record = None

    def link_to_change_control_record(self, change_control_record):
        self.change_control_record = change_control_record

class Request:
    def __init__(self, name):
        self.name = name
        self.change_control_record = None

    def link_to_change_control_record(self, change_control_record):
        self.change_control_record = change_control_record

class ChangeControlRecord:
    def __init__(self, name):
        self.name = name
        self.document_control_information = None
        self.change_implementation_plan = None
        self.communication_and_notification = None
        self.risk_assessment_and_control = None
        self.document_references = []

    def captures_document_control_information(self, document_control_info):
        self.document_control_information = document_control_info

    def captures_change_implementation_plan(self, change_implementation_plan):
        self.change_implementation_plan = change_implementation_plan

    def determines_communication_and_notification(self, communication_notification):
        self.communication_and_notification = communication_notification

    def assesses_risk_assessment_and_control(self, risk_assessment_control):
        self.risk_assessment_and_control = risk_assessment_control

    def references_document(self, document_reference):
        self.document_references.append(document_reference)

class DocumentControlInformation:
    def __init__(self, name):
        self.name = name

class ChangeImplementationPlan:
    def __init__(self, name):
        self.name = name

class CommunicationAndNotification:
    def __init__(self, name):
        self.name = name

class RiskAssessmentAndControl:
    def __init__(self, name):
        self.name = name

class DocumentReference:
    def __init__(self, name):
        self.name = name

class Evaluation:
    def __init__(self, name):
        self.name = name

class Fulfillment:
    def __init__(self, name):
        self.name = name

class Framework:
    def __init__(self, name):
        self.name = name

class Loops:
    def __init__(self, name):
        self.name = name

class Functions:
    def __init__(self, name):
        self.name = name

class Playbooks:
    def __init__(self, name):
        self.name = name

class Mappings:
    def __init__(self, name):
        self.name = name

class Roles:
    def __init__(self, name):
        self.name = name

class Blocks:
    def __init__(self, name):
        self.name = name

class Task:
    def __init__(self, name):
        self.name = name

class RoleSelected:
    def __init__(self, name):
        self.name = name

class TroubleTickets:
    def __init__(self, name):
        self.name = name

class View:
    def __init__(self, name):
        self.name = name

# Creating instances for the entities
user1 = User("User 1")
work_role1 = WorkRole("Work Role 1")
problem1 = Problem("Problem 1")
change1 = Change("Change 1")
request1 = Request("Request 1")
change_control_record1 = ChangeControlRecord("Change Control Record 1")
document_control_info1 = DocumentControlInformation("Document Control Information 1")
change_implementation_plan1 = ChangeImplementationPlan("Change Implementation Plan 1")
communication_notification1 = CommunicationAndNotification("Communication and Notification 1")
risk_assessment_control1 = RiskAssessmentAndControl("Risk Assessment and Control 1")
document_reference1 = DocumentReference("Document Reference 1")
evaluation1 = Evaluation("Evaluation 1")
fulfillment1 = Fulfillment("Fulfillment 1")
framework1 = Framework("Framework 1")
loops1 = Loops("Loops 1")
functions1 = Functions("Functions 1")
playbooks1 = Playbooks("Playbooks 1")
mappings1 = Mappings("Mappings 1")
roles1 = Roles("Roles 1")
blocks1 = Blocks("Blocks 1")
task1 = Task("Task 1")
role_selected1 = RoleSelected("Role Selected 1")
trouble_tickets1 = TroubleTickets("Trouble Tickets 1")
view1 = View("View 1")

# Establishing relationships
user1.initiate_change(change1)
work_role1.addresses_problem(problem1)
work_role1.initiate_change(change1)
work_role1.submit_request(request1)
problem1.link_to_change_control_record(change_control_record1)
change1.link_to_change_control_record(change_control_record1)
request1.link_to_change_control_record(change_control_record1)
change_control_record1.captures_document_control_information(document_control_info1)
change_control_record1.captures_change_implementation_plan(change_implementation_plan1)
change_control_record1.determines_communication_and_notification(communication_notification1)
change_control_record1.assesses_risk_assessment_and_control(risk_assessment_control1)
change_control_record1.references_document(document_reference1)
change1.conducts(evaluation1)
request1.initiate(fulfillment1)
framework1.incorporates(loops1)
framework1.incorporates(functions1)
playbooks1.maps(mappings1)
playbooks1.maps(roles1)
blocks1.assigns(task1)
user1.selects_role(role_selected1)
role_selected1.manages(trouble_tickets1)
trouble_tickets1.provides(view1)
