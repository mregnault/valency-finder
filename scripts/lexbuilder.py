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
        one_sent = dict()
        for sentence in sentences_srcmf:
            sent_id = int(sentence.metadata['sent_id'])
            one_word = dict()
            sentence_obj = Sentence(sent_id, one_word)
            for indexw, word in enumerate(sentence):
                token = Token(word["id"], word["form"], word["lemma"], word["upostag"], word["xpostag"], word["feats"], word["head"], word["deprel"])
                sentence_obj.sentTokens[indexw] = token
            one_sent[sent_id] = sentence_obj
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
    y = mygrewinfo[x].sentID
    for elem in mygrewinfo:
        if int(elem.sentID) in mysrcmf:
            sentence_obj = mysrcmf[int(elem.sentID)]
            for indexw, value in sentence_obj.sentTokens.items():
                if value.tokID == int(elem.vID):
                    list_v = []
                    if value.morpho is not None:
                        verbform = "".join(str(trait) for trait in value.morpho.values())
                    else:
                        verbform = '_'
                    entry = (value.tokform.lower(), value.lemma, verbform, str(elem.arg))
                    if entry not in list_print:
                        list_print.append(entry)

def build_output(outputfile):
    with open(outputfile, "w") as output:
        for elem in list_print:
            output.write("\t".join(elem) + "\n")

build_output(args.output)
