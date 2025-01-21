# from django.contrib.auth.models import Permission
from rolepermissions.roles import AbstractUserRole


class Owner(AbstractUserRole):
    available_permissions = {
        'can_do_everything': True,
    }


class Admin(AbstractUserRole):
    pass


class HeadOfBuying(AbstractUserRole):
    pass


class JuniorBuyer(AbstractUserRole):
    pass


class MiddleBuyer(AbstractUserRole):
    pass


class SeniorBuyer(AbstractUserRole):
    pass


class SoloBuyer(AbstractUserRole):
    pass


class JuniorTeamLead(AbstractUserRole):
    pass


class MiddleTeamLead(AbstractUserRole):
    pass


class SeniorTeamLead(AbstractUserRole):
    pass


class LeadWebDeveloper(AbstractUserRole):
    pass


class WebDeveloper(AbstractUserRole):
    pass


class LeadDesigner(AbstractUserRole):
    pass


class Designer(AbstractUserRole):
    pass


class LeadVideoCreator(AbstractUserRole):
    pass


class VideoCreator(AbstractUserRole):
    pass


# class Doctor(AbstractUserRole):
#     available_permissions = {
#         'create_medical_record': True,
#     }
#
#
# class Nurse(AbstractUserRole):
#     available_permissions = {
#         'edit_patient_file': True,
#     }
