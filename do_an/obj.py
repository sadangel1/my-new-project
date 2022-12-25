import helpers
class User:
    def __init__(self):
        self.data = helpers.get_users_from_file()
    
    def set(self, username=None, name=None,password=None,email=None,tel=None,address=None,image=None,role=None):
        self.username = username
        self.password = password
        self.email = email
        self.tel = tel
        self.address = address
        self.image = image
        self.role = role
        self.name = name

    def get_index_by_user_name(self,username):
        index = -1
        for  i, item in enumerate(self.data):
            if item.get('username') == username:
                index = i
                break
        return index
    def add(self):
        self.data.append({'username':self.username,'name':self.name,'password':self.password,'email':self.email,'tel':self.tel,'address':self.address,'image':self.image,'role':self.role})
        helpers.set_data_to_file(self.data)
    def edit(self,index):
        self.data[index] ={'username':self.username,'name':self.name,'password':self.password,'email':self.email,'tel':self.tel,'address':self.address,'image':self.image,'role':self.role}
        helpers.set_data_to_file(self.data)
    def remove(self):
        index = self.get_index_by_user_name(self.username)
        del self.data[index]
        helpers.set_data_to_file(self.data)
        
    def get(self,username):
        index = self.get_index_by_user_name(username)
        item = self.data[index]
        self.username = item.get('username')
        self.name = item.get('name')
        self.password = item.get('password')
        self.email = item.get('email')
        self.tel = item.get('tel')
        self.address = item.get('address')
        self.image = item.get('image')
        self.role = item.get('role')

class Users:
    def __init__(self):
        self.data = helpers.get_users_from_file()
    def get_list(self):
        result = []
        for item in self.data:
            result.append(item)
        return result
    def search_by_key(self,key_search):
        result = []
        for item in self.data:
            if(item.get('name').lower() == key_search or item.get('email').lower() == key_search or item.get('tel').lower() == key_search or item.get('address').lower() == key_search):
                result.append(item)
        return result








