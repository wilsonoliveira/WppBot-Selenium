from group_service import GroupService
from wpp_service import WppService

wpp = None

def get_groups_service():
    return GroupService.getInstance()

def GetWppBot():
    return WppService.getInstance()
