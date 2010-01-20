from google.appengine.ext import db
import re
from common import TemplateHandler

class AdjectifPl(db.Model):
    name = db.StringProperty(required=True)

class Animal(db.Model):
    name = db.StringProperty(required=True)

class Lieu(db.Model):
    name = db.StringProperty(required=True)
        
class AdjectifSg(db.Model):
    name = db.StringProperty(required=True)
    

class Expression:
    def getPhrase(self):
        aAnimalQ = db.GqlQuery("SELECT * FROM Animal LIMIT 1")
        for aAnimal in aAnimalQ:
            if aAnimal.name:
                aAnimalName = aAnimal.name
            else:
                aAnimalName = 'no name'
        aLieuQ = db.GqlQuery("SELECT * FROM Lieu LIMIT 1")
        for aLieu in aLieuQ:
            if aLieu.name:
                aLieuName = aLieu.name
            else:
                aLieuName = 'no name'
        return 'Bonjour ' + aAnimalName + ' ' + aLieuName
    def getAll(self):
        aVariables = {}
        aVariables['adjectf_pls'] = self.getAdjectifPl()
        aVariables['animals'] = self.getAnimals()
        aVariables['lieux'] = self.getLieux()
        aVariables['adjectf_sgs'] = self.getAdjectifSg()
        return aVariables

    def getAdjectifPl(self):
        return AdjectifPl.all()
    def addAdjectifPl(self, iAdj):
        aAdj = AdjectifPl(name = iAdj)
        db.put(aAdj)
    def delAdjectifPl(self, iAdj):
        q = db.GqlQuery("SELECT __key__ FROM AdjectifPl WHERE name = :1", iAdj)
        results = q.fetch(1)
        db.delete(results)
        
    def getAnimals(self):
        return Animal.all()
    def addAnimal(self, iAnimal):
        aAnimal = Animal(name = iAnimal)
        db.put(aAnimal)
    def delAnimal(self, iAnimal):
        q = db.GqlQuery("SELECT __key__ FROM Animal WHERE name = :1", iAnimal)
        results = q.fetch(1)
        db.delete(results)

    def getLieux(self):
        return Lieu.all()
    def addLieu(self, iLieu):
        aLieu = Lieu(name = iLieu)
        db.put(aLieu)
    def delLieu(self, iLieu):
        q = db.GqlQuery("SELECT __key__ FROM Lieu WHERE name = :1", iLieu)
        results = q.fetch(1)
        db.delete(results)
        
    def getAdjectifSg(self):
        return AdjectifSg.all()
    def addAdjectifSg(self, iAdj):
        aAdj = AdjectifSg(name = iAdj)
        db.put(aAdj)
    def delAdjectifSg(self, iAdj):
        q = db.GqlQuery("SELECT __key__ FROM AdjectifSg WHERE name = :1", iAdj)
        results = q.fetch(1)
        db.delete(results)
         
class ExprContent(TemplateHandler):
    def post(self, action):
        self.get(action)
    def get(self, action):
        if action == '':
            self.getDisplay()
        elif re.compile("^add").match(action):
            self.add(action)
            self.getDisplay()
        elif re.compile("^del").match(action):
            self.delete(action)
            self.getDisplay()
        else:
            self.getDisplay()

    def add(self, type):
        aExpression = Expression()
        aContent = self.request.get('content')
        if aContent != '':
            if type == 'add_adj_pl':
                aExpression.addAdjectifPl(aContent)
            elif type == 'add_animal':
                aExpression.addAnimal(aContent)
            elif type == 'add_lieu':
                aExpression.addLieu(aContent)
            elif type == 'add_adj_sg':
                aExpression.addAdjectifSg(aContent)

    def delete(self, type):
        aExpression = Expression()
        aContent = self.request.get('remove')
        if aContent != '':
            if type == 'del_adj_pl':
                aExpression.delAdjectifPl(aContent)
            elif type == 'del_animal':
                aExpression.delAnimal(aContent)
            elif type == 'del_lieu':
                aExpression.delLieu(aContent)
            elif type == 'del_adj_sg':
                aExpression.delAdjectifSg(aContent)
    
    def getDisplay(self):
        aExpression = Expression()
        aVariables = aExpression.getAll()
        self.showTemplate('content.html', aVariables)
        