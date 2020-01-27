import service_locator

# class Group:
#    def __init__(self, group_name, is_on):
#       self.group_name = group_name
#       self.is_on = is_on

class GroupService:
    instance = None
    groups = {}
    # def __init__():
        # self.groups = {}

    @staticmethod
    def getInstance():
        if GroupService.instance == None :
            GroupService.instance = GroupService()
        return GroupService.instance

    def getAllGroups(self):
        wpp = service_locator.GetWppBot()

        chats = wpp.wpp.get_chat_names()
        for chat in chats:
            print(chat)
            if chat in self.groups :
                pass
            else:
                self.groups[chat] = False

        return self.groups



    
    

