from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from common import TemplateHandler
from expression import ExprContent
from mailinglist import MailingListContent


class MainPage(TemplateHandler):
    def get(self):
        self.showTemplate('admin.html', {})
        
        #aExpression.addAnimal('les marmottes')
        #aExpression.addLieu('de la foret')
        
        
        #self.response.headers['Content-Type'] = 'text/html'
        #self.response.out.write('<html>')
        #self.response.out.write('<body>')
        #self.response.out.write('<div>')
        #self.response.out.write(self.default())
        #self.response.out.write('</div>')
        #self.response.out.write('<div>')
        #self.response.out.write(aExpression.getPhrase())
        #self.response.out.write('</div>')
        #self.response.out.write('</body></html>')
class SendMail(TemplateHandler):
    def get(self, action):
        self.showTemplate('admin.html', {})
        
class MaillingList(TemplateHandler):
    def get(self, action):
        self.showTemplate('admin.html', {})
        

        
        
application = webapp.WSGIApplication([
('/admin/', MainPage),
('/admin/sendmail/(.*)', SendMail),
('/admin/managemaillist/(.*)', MailingListContent),
('/admin/managecontent/(.*)', ExprContent)
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    