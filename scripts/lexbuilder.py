#!/usr/bin/python3

import sys
from io import open
import re
from collections import OrderedDict
import argparse
parser = argparse.ArgumentParser(description='This gives each verb of a conllu file its morphological info and its argument according to GREW patterns.')
parser.add_argument('-s', '--inputsrcmf', help='Input conllu file from SRCMF', required=False)
parser.add_argument('-p', '--pathconllu', help='Path to your conllu module', required=False)
parser.add_argument('-g', '--inputgrew', help='Input file with results from GREW', required=False)
parser.add_argument('-o','--output', help='Output file', required=False)
args = parser.parse_args()
path_conllu = args.pathconllu
sys.path.append(str(path_conllu))
from conllu import parse_incr

##############################################
##### Prepare conllu file to be analysed #####
##############################################

class Sentence:
    # sent ID, tokens
    def __init__(self, sentID, sentTokens):
        self.sentID = sentID
        self.sentTokens = sentTokens

class Token:
    # token ID, lemma, POS UD, POS SRCMF, features, head, dependency, _, _
    def __init__(self, tokID, tokform, lemma, POS_UD, POS_SRCMF, morpho, head_word, dependency):
        self.tokID = tokID
        self.tokform = tokform
        self.lemma = lemma
        self.POS_UD = POS_UD
        self.POS_SRCMF = POS_SRCMF
        self.morpho = morpho
        self.head_word = head_word
        self.dependency = dependency


def read_conllu(file_srcmf):
    with open(file_srcmf, "rt") as srcmf:
        sentences_srcmf = parse_incr(srcmf)
        #print(sentences_srcmf[804])
        one_sent = dict()
        for index, sentence in enumerate(sentences_srcmf, start=0):
            #if index == 804:
            #    print(str(index) + "\t" + str(sentence))
            one_word = dict()
            sentence_obj = Sentence(index, one_word)
            for indexw, word in enumerate(sentence):
                token = Token(word["id"], word["form"], word["lemma"], word["upostag"], word["xpostag"], word["feats"], word["head"], word["deprel"])
                sentence_obj.sentTokens[indexw] = token
            one_sent[index] = sentence_obj
    return one_sent


############################################
##### Prepare GREW file to be analysed #####
############################################

class GrewInfo:
    # sent ID, verb ID, arg nb, dependency, realisation
    def __init__(self, sentID, vID, arg):
        self.sentID = sentID
        self.vID = vID
        self.arg = arg


def read_grew(file_grew):
    with open(file_grew, "rt") as mygrew:
        verbsvalency = []
        for l in mygrew:
            ln = l.strip()
            for ln in mygrew:
                list_tok = []
                columns=ln.split('\t')
                idsent, idverb, arg = columns
                token = GrewInfo(idsent, idverb, arg)
                verbsvalency.append(token)
    return verbsvalency


mysrcmf = read_conllu(args.inputsrcmf)
mygrewinfo = read_grew(args.inputgrew)
list_print = []

for x in range(0, len(mysrcmf)):
    for elem in mygrewinfo:
        #print(elem.sentID)
        if mysrcmf[x].sentID == int(elem.sentID):
            #print(str(mysrcmf[x].sentID) + "\t" + str(elem.sentID))
            for y, value in enumerate(mysrcmf[x].sentTokens):
                #print(mysrcmf[x].sentTokens[y].tokform)
                if mysrcmf[x].sentTokens[y].tokID == int(elem.vID):
                    list_v = []
                    if mysrcmf[x].sentTokens[y].morpho is not None:
                        verbform = ""
                        for trait in mysrcmf[x].sentTokens[y].morpho.values():
                            verbform = verbform + str(trait)
                    else:
                        verbform = '_'
                    list_v.append(str(mysrcmf[x].sentTokens[y].tokform).lower())
                    #print(str(mysrcmf[x].sentID) + "\t" + list_v[0])
                    list_v.append(str(mysrcmf[x].sentTokens[y].lemma))
                    list_v.append(verbform)
                    list_v.append(str(elem.arg))
                    list_print.append(list_v)

def build_output(outputfile):
    with open(outputfile, "w") as output:
        for elem in list_print:
            output.write(elem[0] + "\t" + elem[1] + "\t" + elem[2] + "\t" + elem[3])

build_output(args.output)
