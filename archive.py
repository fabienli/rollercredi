from google.appengine.ext import db

class Archive(db.Model):
    date = db.DateTimeProperty(auto_now_add=True, required=True)
    lieu = db.StringProperty(required=True)

class Handler:
    def displayArchive(self):
        aArchiveQ = db.GqlQuery("SELECT * FROM Archive LIMIT 100")
        aRes = '<table><tr><th>date</th><th>lieu</th></tr>'
        for aArchive in aArchiveQ:
            if aArchive.date + aArchive.lieu:
                aRes+= '<tr><td>'+aArchive.date+'</td><td>'+aArchive.lieu+'</td></tr>'
        aRes+= '</table>'
        return aRes
    def getArchive(self):
        aArchiveQ = Archive.all().order('-date')
        aArchive = aArchiveQ.fetch(20)
        return aArchive
    def getArchiveTemplateName(self):
        return 'archive.html'
    def addSortie(self, iLieu, iDate):
        if iDate:
            aArchive = Archive(lieu = iLieu, date = iDate)
        else:
            aArchive = Archive(lieu = iLieu)
        db.put(aArchive)
    