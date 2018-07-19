import webbrowser
class Mobile():
    def __init__(self,whatever_u_want_to_search):
        self.search = whatever_u_want_to_search
    def search_online(self):
        webbrowser.open("http://www.google.co.in/search?q=" + self.search)
mobile1 = Mobile("motox")
mobile1.search_online()