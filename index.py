from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import archive
from common import TemplateHandler


class MainPage(TemplateHandler):
    def default(self):
        a ='<div><a href="/vote">vote</a>'
        a+= ' <a href="/admin/">admin</a>'
        user = users.get_current_user()
        if user:
            a+= ' <a href="' + users.create_logout_url(self.request.uri) + '">logout</a>'
        a+= '</div>'
        return a
    def get(self):
        aArchiveHandler = archive.Handler()
        aTemplateName = aArchiveHandler.getArchiveTemplateName()
        aTemplateValues = {
            'archives': aArchiveHandler.getArchive()            
            }
        
        self.showTemplate(aTemplateName, aTemplateValues)
        
application = webapp.WSGIApplication([
('/', MainPage)
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    