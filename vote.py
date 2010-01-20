from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from common import TemplateHandler
from google.appengine.ext import db

class Votes(db.Model):
    name = db.StringProperty(required=True)
    lieu = db.StringProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True, required=True)

class VoteHandler:
    def getVoteTemplateName(self):
        return 'vote.html'
    def getVoteContent(self):
        aValues = {}
        aValues['votes'] = Votes.all()
        return aValues
    def vote(self, iName, iLieu):
        if iName == '':
            return 'preciser le nom'
        if iLieu == '':
            return 'preciser le lieu'
        aVote = Votes(name = iName, lieu = iLieu)
        db.put(aVote)
        return 'le vote ('+iName+','+iLieu+') a bien &eacute;t&eacute; pris en compte'
    def resetVotes(self):
        a = Votes.all()
        #results = q.fetch(10)
        #db.delete(results)
        db.delete(a)
        return 'votes remis a zero'
    
    
    
class MainPage(TemplateHandler):
    def get(self):
        aHandler = VoteHandler()
        aTemplateName = aHandler.getVoteTemplateName()
        aTemplateValues = aHandler.getVoteContent()
        aTemplateValues['msg']=''
        self.showTemplate(aTemplateName, aTemplateValues)
        
class VoteAction(TemplateHandler):
    def post(self, action):
        self.get(action)
    def get(self, action):
        aHandler = VoteHandler()
        aMsg = ''
        if action == 'add':
            aName = self.request.get('name')
            aLieu = self.request.get('lieu')
            aMsg = aHandler.vote(aName, aLieu)
        elif action == 'reset':
            aMsg = aHandler.resetVotes()
        aTemplateName = aHandler.getVoteTemplateName()
        aTemplateValues = aHandler.getVoteContent()
        aTemplateValues['msg']=aMsg
        self.showTemplate(aTemplateName, aTemplateValues)

        
application = webapp.WSGIApplication([
('/vote', MainPage),
('/vote/', MainPage),
('/vote/(.*)', VoteAction),
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    