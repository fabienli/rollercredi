from google.appengine.api import users
from google.appengine.ext import webapp

class Credi(webapp.RequestHandler):
    def get(self, action):
        user = self.getUser()
        if user == '':
            return
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<html>')
        self.response.out.write('<body>')
        self.response.out.write('<div><a href="/">home</a> ' +
            '<a href="' + users.create_logout_url(self.request.uri) + '">logout</a></div>')
        self.response.out.write('<br />user: ' + user)
        self.response.out.write('<br />TODO: ' + action)
        
        self.response.out.write('</body></html>')

    def getUser(self):
        user = users.get_current_user()
        if user:
            return user.nickname()
        else:
            self.redirect(users.create_login_url(self.request.uri))
            return ''
