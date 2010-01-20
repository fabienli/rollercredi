import logging
from google.appengine.ext import db
from common import TemplateHandler

class MailList(db.Model):
    email = db.EmailProperty(required=True)
    user = db.UserProperty()

    

class MaillingList:
    def getAll(self):
        aVariables = {}
        aVariables['emails'] = self.getMails()
        return aVariables

    def getMails(self):
        return MailList.all()
    def addMail(self, iMail):
        aMail = MailList(email = iMail)
        db.put(aMail)
    def delMail(self, iMail):
        q = db.GqlQuery("SELECT __key__ FROM MailList WHERE email = :1", iMail)
        results = q.fetch(1)
        db.delete(results)
         
class MailingListContent(TemplateHandler):
    def post(self, action):
        self.get(action)
    def get(self, action):
        if action == '':
            self.getDisplay()
        elif 'add' == action:
            aMaillingList = MaillingList()
            aNewMail = self.request.get('email')
            if aNewMail != '':
                aMaillingList.addMail(aNewMail)
            self.getDisplay()
        elif 'remove' == action:
            aMaillingList = MaillingList()
            aOldMail = self.request.get('remove')
            if aOldMail != '':
                aMaillingList.delMail(aOldMail)
            self.getDisplay()
        else:
            self.getDisplay()
    
    def getDisplay(self):
        aMaillingList = MaillingList()
        aVariables = aMaillingList.getAll()
        self.showTemplate('mailinglist.html', aVariables)
        