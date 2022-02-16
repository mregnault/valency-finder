#!/usr/bin/python3

import sys
from io import open
import re
from collections import OrderedDict
import argparse
parser = argparse.ArgumentParser(description='This program calculates scores.')
parser.add_argument('-g', '--inputgrew', help='Input file with results from GREW', required=False)
parser.add_argument('-m', '--mapping', help='Input file with mapping BFMGOLDLEM and OFrLex', required=False)
parser.add_argument('-t', '--table', help='Secondary output: occurrences for each argument of each verb', required=False)
parser.add_argument('-o','--output', help='Output file', required=False)
args = parser.parse_args()

# Structure of files
class Corpusinfo:
	# Input GREW (from json file)
    # token, lemma, morpho, valency
    def __init__(self, word, lemma, morphoconllu, argument):
        self.word = word
        self.lemma = lemma
        self.morpho = morpho
        self.argument = argument

class Mappinginfo:
	# Mapping BFMGOLDLEM and OFrLex's lemmas
	# lemma OFrLEx, token, UPOS, valency, lemma BFM, Cattex POS, morpho, no_upos, file
	def __init__(self, lemOFR, token, lemBFM, morphobfm):
		self.lemOFR = lemOFR
		self.token = token
		self.lemBFM = lemBFM
		self.morphobfm = morphobfm

#class Tablelex:
	# Secondary outputfile
	# Lemma, nsubj, nsubjimp, csubjscompl, csubjsinf, attsubjsasn, attsubjadv, attsubjasinf, attsubjinf, attsubjscompl, clr, objsn, objscompl, objsinf, cly, dloc, auxpass

class Lexentry:
	# Outputfile
    # token, lemma, morpho, suj, obj, attsuj, objà, objde, obl, dloc, passif
    def __init__(self, lemma, suj, obj, attsuj, objà, objde, obl, loc, dloc, passif, refl):
        self.lemma = lemma
        self.suj = suj
        self.obj = obj
        self.attsuj = attsuj
        self.objà = objà
        self.objde = objde
        self.obl = obl
        self.loc = loc
        self.dloc = dloc
        self.passif = passif
        self.refl = refl

class Suj:
    def __init__(self, clnsn, sinf, scompl, ilimp):
        self.clnsn = clnsn
        self.sinf = sinf
        self.scompl = scompl
        self.ilimp = ilimp

class Obj:
    def __init__(self, clasn, scompl, sinf):
        self.clasn = clasn
        self.scompl = scompl
        self.sinf = sinf

class Attsuj:
    def __init__(self, sasn, sadv, scompl, sinf, asinf):
        self.sasn = sasn
        self.sadv = sadv
        self.scompl = scompl
        self.sinf = sinf
        self.asinf = asinf

class Objà:
    def __init__(self, cld, asinf, asn):
        self.cld = cld
        self.asinf = asinf
        self.asn = asn

class Objde:
    def __init__(self, clg, desinf, desn):
        self.clg = clg
        self.desinf = desinf
        self.desn = desn

class Obl:
    def __init__(self, sursn, sinf, parsn, ensn, desn, avecsn, contresn, asn, desinf, asinf):
        self.sursn = sursn
        self.sinf = sinf
        self.parsn = parsn
        self.ensn = ensn
        self.desn = desn
        self.avecsn = avecsn
        self.contresn = contresn
        self.asn = asn
        self.desinf = desinf
        self.asinf = asinf


# Read the input files
verbs = []
with open(args.inputgrew, "rt") as mygrew:
    for l in mygrew:
        ln = l.strip()
        for ln in mygrew:
            columns=ln.split('\t')
            token, lemma, morpho, valency = columns
            valency2 = valency.strip('\n')
            #entry = Corpusinfo(token, lemma, morpho, valency2)
            entry = []
            entry.append(token)
            entry.append(lemma)
            entry.append(morpho)
            entry.append(valency2)
            verbs.append(entry)
"""
maplem = []
with open(args.mapping, "rt") as mymap:
    for l in mymap:
        ln = l.strip()
        for ln in mymap:
            columns=ln.split('\t')
            lemOFR, token, upos, valency, lemBFM, cattex, morphobfm, noupos, filename = columns
            entry = Mappinginfo(lemOFR, token, lemBFM, morphobfm)
            maplem.append(entry)
"""

"""
# Compare input files
for n in range(0, len(maplem)):
	verbOFR = Lexentry(maplem[n].lemOFR, 0)
	for elem in verbs:
		if maplem[n].lemBFM == elem[1]:
"""

# Max. 2 teams for an entry:
teamA = ['OBJSN', 'OBJSCOMPL', 'OBJSINF']
teamB = ['ATTSUBJASINF', 'ATTSUBJADV', 'ATTSUBJSASN', 'ATTSUBJSCOMPL', 'ATTSUBJINF']
teamC = ['IOBJA', 'OBJAVINF', 'OBJASN']
teamD = ['IOBJDE', 'OBJDEVINF', 'OBJDESN']
"""
- obliques: OBLSURSN, OBLSINF, OBLPARSN, OBLENSN, OBLDESN, OBLAVECSN, OBLCONTRESN, OBLASN, OBLDESINF, OBLASINF
- CLY -> OBJAVINF ou Loc
- DLOC
- CLR ? se Lemma
- @passive
- quels sujets : NSUBJIMP, NSUBJ, CSUBJSINF, CSUBJSCOMPL "DLOC"
"""

lemmata = {}
for elem in verbs:
    vinf = elem[1]
    if vinf not in lemmata.keys():
        lemvinf = Lexentry(vinf, Suj(0, 0, 0, 0), Obj(0, 0, 0), Attsuj(0, 0, 0, 0, 0), Objà(0, 0, 0), Objde(0, 0, 0), Obl(0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0)
        lemvinf.lemma = vinf
        lemmata[vinf] = lemvinf
    if elem[3] == 'NSUBJ':
        lemvinf.suj.clnsn += 1
    elif elem[3] == 'CSUBJSINF':
        lemvinf.suj.sinf += 1
    elif elem[3] == 'CSUBJSCOMPL':
        lemvinf.suj.scompl += 1
    elif elem[3] == 'NSUBJIMP':
        lemvinf.suj.ilimp += 1
    elif elem[3] == 'OBJSN':
        lemvinf.obj.clasn += 1
    elif elem[3] == 'OBJSINF':
        lemvinf.obj.sinf += 1
    elif elem[3] == 'OBJSCOMPL':
        lemvinf.obj.scompl += 1
    elif elem[3] == 'ATTSUBJSASN':
        lemvinf.attsuj.sasn += 1
    elif elem[3] == 'ATTSUBJSCOMPL':
        lemvinf.attsuj.scompl += 1
    elif elem[3] == 'ATTSUBJSINF':
        lemvinf.attsuj.sinf += 1
    elif elem[3] == 'ATTSUBJASINF':
        lemvinf.attsuj.asinf += 1
    elif elem[3] == 'ATTSUBJADV':
        lemvinf.attsuj.sadv += 1
    elif elem[3] == 'IOBJA':
        lemvinf.objà.cld += 1
    elif elem[3] == 'OBJAVINF':
        lemvinf.objà.asinf += 1
    elif elem[3] == 'OBJASN':
        lemvinf.objà.asn += 1
    elif elem[3] == 'IOBJDE':
        lemvinf.objde.clg += 1
    elif elem[3] == 'OBJDEVINF':
        lemvinf.objde.desinf += 1
    elif elem[3] == 'OBJDESN':
        lemvinf.objde.desn += 1
    elif elem[3] == 'OBLSURSN':
        lemvinf.obl.sursn += 1
    elif elem[3] == 'OBLSINF':
        lemvinf.obl.sinf += 1
    elif elem[3] == 'OBLPARSN':
        lemvinf.obl.parsn += 1
    elif elem[3] == 'OBLENSN':
        lemvinf.obl.ensn += 1
    elif elem[3] == 'OBLDESN':
        lemvinf.obl.desn += 1
    elif elem[3] == 'OBLAVECSN':
        lemvinf.obl.avecsn += 1
    elif elem[3] == 'OBLCONTRESN':
        lemvinf.obl.contresn += 1
    elif elem[3] == 'OBLASN':
        lemvinf.obl.asn += 1
    elif elem[3] == 'OBLDESINF':
        lemvinf.obl.desinf += 1
    elif elem[3] == 'OBLASINF':
        lemvinf.obl.asinf += 1
    elif elem[3] == 'CLY':
        lemvinf.loc += 1
    elif elem[3] == 'DLOC':
        lemvinf.dloc += 1
    elif elem[3] == 'AUXPASS':
        lemvinf.passif += 1
    elif elem[3] == 'CLR':
        lemvinf.refl += 1

# Architecture des entrées OFrLex : Suj, Obj, Objà, Objde, Obl, Obl2, Loc, Dloc
# se Lemma : liste de verbes -> on propose entrées réflexives
# %passif : faire liste de verbes pour lesquels générer des part. passés passifs + ppp

class OFrLex_entries:
    def __init__(self, lemma, suj, obj, att, objà, objde, obl, obl2, loc, dloc, macros):
        self.lemma = lemma
        self.suj = suj
        self.obj = obj
        self.att = att
        self.objà = objà
        self.objde = objde
        self.obl = obl
        self.obl2 = obl2
        self.loc = loc
        self.dloc = dloc
        self.macros = macros

newofr = []
for elem in lemmata:
    verbeofr = OFrLex_entries(None, [], [], [], [], [], [], [], [], [], [])
    verbeofr.lemma = lemmata[elem].lemma
    # Fill subject frame
    if lemmata[elem].suj.clnsn >= 1:
        verbeofr.suj.append("cln|sn")
    if lemmata[elem].suj.sinf >= 1:
        verbeofr.suj.append("sinf")
    if lemmata[elem].suj.scompl >= 1:
        verbeofr.suj.append("scompl")
    if lemmata[elem].suj.ilimp >= 1:
        verbeofr.macros.append("@impers")
    # Fill object frame
    if lemmata[elem].obj.clasn >= 1:
        verbeofr.obj.append("cla|sn")
    if lemmata[elem].obj.scompl >= 1:
        verbeofr.obj.append("scompl")
    if lemmata[elem].obj.sinf >= 1:
        verbeofr.obj.append("sinf")
    # Fill att subj frame sa|sn, sadv, sinf, asinf
    if lemmata[elem].attsuj.sasn >= 1:
        verbeofr.att.append("sa|sn")
    if lemmata[elem].attsuj.scompl >= 1:
        verbeofr.att.append("scompl")
    if lemmata[elem].attsuj.sadv >= 1:
        verbeofr.att.append("sadv")
    if lemmata[elem].attsuj.sinf >= 1:
        verbeofr.att.append("sinf")
    if lemmata[elem].attsuj.asinf >= 1:
        verbeofr.att.append("à-sinf")
    # Fill iobj frame cld, asn, asinf
    if lemmata[elem].objà.cld >= 1 & lemmata[elem].objà.asn >= 1 :
        verbeofr.objà.append("cld|à-sn")
    if lemmata[elem].loc >= 1 & lemmata[elem].objà.asinf >= 1 :
        verbeofr.objà.append("y|à-sinf")
    # Fill iobj frame clg, desn, desinf
    if lemmata[elem].objde.clg >= 1 & lemmata[elem].objde.desn >= 1 :
        verbeofr.objde.append("clg|de-sn")
    if lemmata[elem].objde.clg >= 1 & lemmata[elem].objde.desinf >= 1 :
        verbeofr.objde.append("clg|de-sinf")
    if lemmata[elem].obl.sursn >= 1:
        verbeofr.obl.append("sur-sn")
    if lemmata[elem].obl.sinf >= 1:
        verbeofr.obl.append("sinf")
    if lemmata[elem].obl.parsn >= 1:
        verbeofr.obl.append("par-sn")
    if lemmata[elem].obl.ensn >= 1:
        verbeofr.obl.append("en-sn")
    if lemmata[elem].obl.desn >= 1 & lemmata[elem].dloc >= 1:
        verbeofr.dloc.append("de-sn|en")
    if lemmata[elem].obl.desn >= 1:
        verbeofr.obl.append("de-sn")
    if lemmata[elem].obl.avecsn >= 1:
        verbeofr.obl.append("avec-sn")
    if lemmata[elem].obl.contresn >= 1:
        verbeofr.obl.append("contre-sn")
    if lemmata[elem].obl.asn >= 1 & lemmata[elem].loc >= 1:
        verbeofr.loc.append("loc-sn|y")
    if lemmata[elem].obl.asn >= 1:
        verbeofr.obl.append("à-sn")
    if lemmata[elem].obl.desinf >= 1:
        verbeofr.obl.append("de-sinf")
    if lemmata[elem].obl.asinf >= 1:
        verbeofr.obl.append("à-sinf")
    if lemmata[elem].passif >= 1:
        verbeofr.macros.append("passif")
    if lemmata[elem].refl >= 1:
        verbeofr.macros.append("se Lemma")
    # in the end
    newofr.append(verbeofr)

    #print(lemmata[elem].lemma + "\tSuj:" + )
    #print(lemmata.keys())
#for elem in newofr:
#    print(str(elem.lemma) + str(elem.macros))

with open(args.output, "w") as myoutput:
    for elem in newofr:
        myoutput.write(str(elem.lemma) + "\t" + str(elem.suj) + "\t" + str(elem.obj) + "\t" + str(elem.att) + "\t" + str(elem.objà) + "\t" + str(elem.objde) + "\t" + str(elem.loc) + "\t" + str(elem.dloc) + "\t" + str(elem.macros) + "\n")