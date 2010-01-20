from google.appengine.api import users
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp


class TemplateHandler(webapp.RequestHandler):
    def showTemplate(self, iTemplateName, iTemplateValues):
        aTemplateValues = iTemplateValues
        if users.get_current_user():
            aTemplateValues['url_log'] = users.create_logout_url(self.request.uri)
            aTemplateValues['url_log_linktext'] = 'Logout'
        else:
            aTemplateValues['url_log'] = users.create_login_url(self.request.uri)
            aTemplateValues['url_log_linktext'] = 'Login'

        path = os.path.join(os.path.dirname(__file__), iTemplateName)
        self.response.out.write(template.render(path, aTemplateValues))