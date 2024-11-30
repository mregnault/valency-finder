#!/usr/bin/python3

import sys
from io import open
import re
from collections import OrderedDict
import argparse
parser = argparse.ArgumentParser(description='This program gathers valency frames for OFrLex entries.')
parser.add_argument('-g', '--inputgrew', help='Input file with results from GREW (token, morpho, valency)', required=False)
parser.add_argument('-l', '--ofrlex', help='Old OFrLex info (token, lemma, morpho)', required=False)
parser.add_argument('-o','--output', help='Output file', required=False)
args = parser.parse_args()

class Oldlex:
    # token, lemma, morpho
    def __init__(self, ofrentry, ofrlemma, ofrmorpho):
        self.ofrentry = ofrentry
        self.ofrlemma = ofrlemma
        self.ofrmorpho = ofrmorpho

class Corpusinfo:
    # token, morpho, valency
    def __init__(self, word, category, valency):
        self.word = word
        self.category = category
        self.valency = valency

class Lexentry:
    # token, morpho, suj, obj, attsuj, objà, objde, obl, dloc, passif
    def __init__(self, lemma, suj, obj, attsuj, objà, objde, obl, dloc, passif):
        self.lemma = lemma
        self.suj = suj
        self.obj = obj
        self.attsuj = attsuj
        self.objà = objà
        self.objde = objde
        self.obl = obl
        self.dloc = dloc
        self.passif = passif

myofr = []
with open(args.ofrlex, "rt") as ofr:
    for l in ofr:
        ln = l.strip()
        for ln in ofr:
            entry = []
            columns=ln.split('\t')
            token, lemma, morpho = columns
            entry.append(token)
            entry.append(lemma)
            entry.append(morpho)
            myofr.append(entry)

verbs = []
with open(args.inputgrew, "rt") as mygrew:
    for l in mygrew:
        ln = l.strip()
        for ln in mygrew:
            entry = []
            columns=ln.split('\t')
            token, morpho, valency = columns
            valency2 = valency.strip('\n')
            entry.append(token)
            entry.append(morpho)
            entry.append(valency2)
            verbs.append(entry)

newofr = {}
for elem in myofr:
    m = elem[1]
    newofr[m] = Lexentry(m, [], [], [], [], [], [], [], [])
for elem in verbs:
    for line in myofr:
        if elem[0].lower() == line[0]:
            m = line[1]
            if elem[2] == 'NSUBJ':
                if 'sn' not in newofr[m].suj:
                    newofr[m].suj.append('sn')
            elif elem[2] == 'NSUBJIMP':
                if 'ilimp' not in newofr[m].suj:
                    newofr[m].suj.append('ilimp')
            elif elem[2] == 'CSUBJSCOMPL':
                if 'scompl' not in newofr[m].suj:
                    newofr[m].suj.append('scompl')
            elif elem[2] == 'CSUBJSINF':
                if 'sinf' not in newofr[m].suj:
                    newofr[m].suj.append('sinf')
            elif elem[2] == 'ATTSUBJSASN':
                if 'sa|sn' not in newofr[m].attsuj:
                    newofr[m].attsuj.append('sa|sn')
            elif elem[2] == 'ATTSUBJASINF':
                if 'à-sinf' not in newofr[m].attsuj:
                    newofr[m].attsuj.append('à-sinf')
            elif elem[2] == 'ATTSUBJINF':
                if 'sinf' not in newofr[m].attsuj:
                    newofr[m].attsuj.append('sinf')
            elif elem[2] == 'OBJSN':
                if 'sn' not in newofr[m].obj:
                    newofr[m].obj.append('sn')
            elif elem[2] == 'CLR':
                if 'clr' not in newofr[m].obj:
                    newofr[m].obj.append('clr')
            elif elem[2] == 'OBJSINF':
                if 'sinf' not in newofr[m].obj:
                    newofr[m].obj.append('sinf')
            elif elem[2] == 'OBJCOMPL':
                if 'scompl' not in newofr[m].obj:
                    newofr[m].obj.append('scompl')
            elif elem[2] == 'OBJASN':
                if 'à-sn' not in newofr[m].objà:
                    newofr[m].objà.append('à-sn')
            #elif elem[2] == 'IOBJA':
            #    if 'IOBJA' not in newofr[m].objà:
            #        newofr[m].objà.append('IOBJA')
            elif elem[2] == 'OBJAVINF':
                if 'à-sinf' not in newofr[m].objà:
                    newofr[m].objà.append('à-sinf')
            #elif elem[2] == 'CLY':
            #    if 'CLY' not in newofr[m].objà:
            #        newofr[m].objà.append('CLY')
            elif elem[2] == 'OBJDESN':
                if 'de-sn' not in newofr[m].objde:
                    newofr[m].objde.append('de-sn')
            #elif elem[2] == 'IOBJDE':
            #    if 'IOBJDE' not in newofr[m].objde:
            #        newofr[m].objde.append('IOBJDE')
            elif elem[2] == 'OBJDEVINF':
                if 'de-sinf' not in newofr[m].objde:
                    newofr[m].objde.append('de-sinf')
            elif elem[2] == 'OBL-A-SINF':
                if 'à-sinf' not in newofr[m].obl:
                    newofr[m].obl.append('à-sinf')
            elif elem[2] == 'OBL-A-SN':
                if 'à-sn' not in newofr[m].obl:
                    newofr[m].obl.append('à-sn')
            elif elem[2] == 'OBL-CONTRE-SN':
                if 'contre-sn' not in newofr[m].obl:
                    newofr[m].obl.append('contre-sn')
            elif elem[2] == 'OBL-AVEC-SN':
                if 'avec-sn' not in newofr[m].obl:
                    newofr[m].obl.append('avec-sn')
            elif elem[2] == 'OBL-DE-SINF':
                if 'de-sinf' not in newofr[m].obl:
                    newofr[m].obl.append('de-sinf')
            elif elem[2] == 'OBL-DE-SN':
                if 'de-sn' not in newofr[m].obl:
                    newofr[m].obl.append('de-sn')
            elif elem[2] == 'OBL-EN-SN':
                if 'en-sn' not in newofr[m].obl:
                    newofr[m].obl.append('en-sn')
            elif elem[2] == 'OBL-PAR-SN':
                if 'par-sn' not in newofr[m].obl:
                    newofr[m].obl.append('par-sn')
            elif elem[2] == 'OBL-SINF':
                if 'sinf' not in newofr[m].obl:
                    newofr[m].obl.append('sinf')
            elif elem[2] == 'DLOC':
                if 'de-sn|en' not in newofr[m].dloc:
                    newofr[m].dloc.append('de-sn|en')
            elif elem[2] == '@passive':
                if '@passive' not in newofr[m].passif:
                    newofr[m].passif.append('@passive') 


with open(args.output, "w") as printfile:
    for n in newofr:
        str_print = str(newofr[n].lemma) + '\t'
        if len(newofr[n].suj) > 0:
            arg0 = "Suj:cln"
            for elem in newofr[n].suj:
                arg0 = arg0 + "|" + str(elem)
            str_print = str_print + arg0
        if len(newofr[n].obj) > 0:
            if len(newofr[n].obj) == 1 and newofr[n].obj[0] == 'clr':
                arg1 = "Obj:(clr"
            else:
                arg1 = "Obj:(cla"
                for elem in newofr[n].obj:
                    arg1 = arg1 + "|" + str(elem)
            arg1 = arg1 + ")"
            if len(newofr[n].suj) > 0:
                str_print = str_print + ',' + arg1
            else:
                str_print = str_print + arg1
        if len(newofr[n].attsuj) > 0:
            arg1 = "Att:(" + str(newofr[n].attsuj[0])
            del newofr[n].attsuj[0]
            for elem in newofr[n].attsuj:
                arg1 = arg1 + "|" + str(elem)
            arg1 = arg1 + ")"
            str_print = str_print + ',' + arg1
        if len(newofr[n].objà) > 0:
            arg2 = "Objà:(cld|" + str(newofr[n].objà[0])
            del newofr[n].objà[0]
            for elem in newofr[n].objà:
                arg2 = arg2 + "|" + str(elem)
            arg2 = arg2 + ")"
            if len(newofr[n].suj) > 0 or len(newofr[n].obj) > 0:
                str_print = str_print + ',' + arg2
            else:
                str_print = str_print + arg2
        if len(newofr[n].objde) > 0:
            arg2 = "Objde:(clg|" + str(newofr[n].objde[0])
            del newofr[n].objde[0]
            for elem in newofr[n].objde:
                arg2 = arg2 + "|" + str(elem)
            arg2 = arg2 + ")"
            if len(newofr[n].suj) > 0 or len(newofr[n].obj) > 0:
                str_print = str_print + ',' + arg2
            else:
                str_print = str_print + arg2
        if len(newofr[n].obl) > 0:
            argobl = "Obl:(" + str(newofr[n].obl[0])
            del newofr[n].obl[0]
            for elem in newofr[n].obl:
                argobl = argobl + "|" + str(elem)
            argobl = argobl + ")"
            str_print = str_print + ',' + argobl
        if len(newofr[n].passif) > 0:
            if len(newofr[n].suj) > 0 or len(newofr[n].obj) > 0:
                str_print = str_print + ',@passive'
            else:
                str_print = str_print + '@passive'
        str_print = str_print + '\n'
        printfile.write(str_print)
