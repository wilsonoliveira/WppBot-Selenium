from wppbot import WppApi

# class Group:
#    def __init__(self, group_name, is_on):
#       self.group_name = group_name
#       self.is_on = is_on

class WppService:
    instance = None
    # def __init__():
        # self.groups = {}

    @staticmethod
    def getInstance():
        if WppService.instance == None :
            WppService.instance = WppService()
            WppService.instance.wpp = WppApi(60)
        return WppService.instance


    
    

