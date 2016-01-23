# -*- coding: utf-8 -*-
import json, csv, re
from HTMLParser import HTMLParser

js = []
with open('tweetData.json','r') as infile: js = json.loads(infile.read())

LHan = [[0x2E80, 0x2E99],    # Han # So  [26] CJK RADICAL REPEAT, CJK RADICAL RAP
        [0x2E9B, 0x2EF3],    # Han # So  [89] CJK RADICAL CHOKE, CJK RADICAL C-SIMPLIFIED TURTLE
        [0x2F00, 0x2FD5],    # Han # So [214] KANGXI RADICAL ONE, KANGXI RADICAL FLUTE
        0x3005,              # Han # Lm       IDEOGRAPHIC ITERATION MARK
        0x3007,              # Han # Nl       IDEOGRAPHIC NUMBER ZERO
        [0x3021, 0x3029],    # Han # Nl   [9] HANGZHOU NUMERAL ONE, HANGZHOU NUMERAL NINE
        [0x3038, 0x303A],    # Han # Nl   [3] HANGZHOU NUMERAL TEN, HANGZHOU NUMERAL THIRTY
        0x303B,              # Han # Lm       VERTICAL IDEOGRAPHIC ITERATION MARK
        [0x3400, 0x4DB5],    # Han # Lo [6582] CJK UNIFIED IDEOGRAPH-3400, CJK UNIFIED IDEOGRAPH-4DB5
        [0x4E00, 0x9FC3],    # Han # Lo [20932] CJK UNIFIED IDEOGRAPH-4E00, CJK UNIFIED IDEOGRAPH-9FC3
        [0xF900, 0xFA2D],    # Han # Lo [302] CJK COMPATIBILITY IDEOGRAPH-F900, CJK COMPATIBILITY IDEOGRAPH-FA2D
        [0xFA30, 0xFA6A],    # Han # Lo  [59] CJK COMPATIBILITY IDEOGRAPH-FA30, CJK COMPATIBILITY IDEOGRAPH-FA6A
        [0xFA70, 0xFAD9],    # Han # Lo [106] CJK COMPATIBILITY IDEOGRAPH-FA70, CJK COMPATIBILITY IDEOGRAPH-FAD9
        [0x20000, 0x2A6D6],  # Han # Lo [42711] CJK UNIFIED IDEOGRAPH-20000, CJK UNIFIED IDEOGRAPH-2A6D6
        [0x2F800, 0x2FA1D]]  # Han # Lo [542] CJK COMPATIBILITY IDEOGRAPH-2F800, CJK COMPATIBILITY IDEOGRAPH-2FA1D
def build_re():
    L = []
    for i in LHan:
        if isinstance(i, list):
            f, t = i
            try: 
                f = unichr(f)
                t = unichr(t)
                L.append('%s-%s' % (f, t))
            except: 
                pass # A narrow python build, so can't use chars > 65535 without surrogate pairs!
        else:
            try:
                L.append(unichr(i))
            except:
                pass
    RE = '[%s]' % ''.join(L)
    return re.compile(RE, re.UNICODE)

def removeNonEnglishChars(tweetBody):
	noChinese = build_re()
	tweetBody = noChinese.sub('',tweetBody)
	noJapanese = re.compile(u'[^\u0000-\u30A0\u30FF-\uFFFF]',re.UNICODE)
	tweetBody = noJapanese.sub('',tweetBody)
	noCyrillic = re.compile(u'[^\u0000-\u0500\u05FF-\uFFFF]',re.UNICODE)
	tweetBody = noCyrillic.sub('',tweetBody)
	noSanskrit = re.compile(u'[^\u0000-\u0900\u097F-\uFFFF]',re.UNICODE)
	tweetBody = noSanskrit.sub('',tweetBody)
	noGreek = re.compile(u'[^\u0000-\u0300\u03FF-\uFFFF]',re.UNICODE)
	tweetBody = noGreek.sub('',tweetBody)
	noHebrew = re.compile(u'[^\u0000-\u05BE\u05F4-\uFFFF]',re.UNICODE)
	tweetBody = noHebrew.sub('',tweetBody)
	noArabic = re.compile(u'[^\u0000-\u0600\u06FF-\uFFFF]',re.UNICODE)
	tweetBody = noArabic.sub('',tweetBody)
	idk = re.compile(u'[^\u0000-\u0400\u04FF-\uFFFF]',re.UNICODE)
	tweetBody = idk.sub('',tweetBody)
	return tweetBody

def normalize(tweetBody,parser):
	tweetBody = parser.unescape(tweetBody)
	emoji_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
	tweetBody = emoji_pattern.sub('', tweetBody)
	misc_pattern = re.compile(u'[^\u0000-\u2020\u26FF-\uFFFF]',re.UNICODE)
	tweetBody = misc_pattern.sub('',tweetBody)
	etc = re.compile(u'[^\u0000-\u2012\u204A-\uFFFF]',re.UNICODE)
	tweetBody = etc.sub('',tweetBody)
	etc2 = re.compile(u'[^\u0000-\u0100\u017F-\uFFFF]',re.UNICODE)
	tweetBody = etc2.sub('',tweetBody)
	etc3 = re.compile(u'[^\u0000-\u1E02\u1EF3-\uFFFF]',re.UNICODE)
	tweetBody = etc3.sub('',tweetBody)
	etc4 = re.compile(u'[^\u0000-\u2000\u2FFF-\uFFFF]',re.UNICODE)
	tweetBody = etc4.sub('',tweetBody)

	noX = re.compile(u'[\x00-\x19\x7f-\xff]', re.UNICODE)
	tweetBody = noX.sub('',tweetBody)

	tweetBody=tweetBody.replace(u'\uFE0F',"")	
	tweetBody=tweetBody.replace(u'\u02C6',"")
	tweetBody=tweetBody.replace(u'\u0153',"")
	tweetBody=tweetBody.replace(u'\u0259',"")
	tweetBody=tweetBody.replace(u'\u02c8',"")
	tweetBody=tweetBody.replace(u'\u652F',"")
	tweetBody=tweetBody.replace(u'\u4ED8',"")
	tweetBody=tweetBody.replace(u'\u5B9D',"")
	tweetBody=tweetBody.replace(u'\u3002',"")
	tweetBody=tweetBody.replace(u'\u02DC',"")
	tweetBody=tweetBody.replace(u'\u03B1',"")
	tweetBody=tweetBody.replace(u'\u0418',"")
	tweetBody=tweetBody.replace(u'\uFEFF',"")
	tweetBody=tweetBody.replace(u'\uF8FF',"")
	tweetBody=tweetBody.replace(u'\uFF1F',"")
	tweetBody=tweetBody.replace(u'\uFF0C',"")
	tweetBody=tweetBody.replace(u'\u6c92',"")
	tweetBody=tweetBody.replace(u'\u6709',"")
	tweetBody=tweetBody.replace(u'\u4e0a',"")
	tweetBody=tweetBody.replace(u'\u5e1d',"")
	tweetBody=tweetBody.replace(u'\u8a72',"")
	tweetBody=tweetBody.replace(u'\u6b7b',"")
	tweetBody=tweetBody.replace(u'\uff01',"")
	tweetBody=tweetBody.replace(u'\u7a76',"")
	tweetBody=tweetBody.replace(u'\u7adf',"")
	tweetBody=tweetBody.replace(u'\u70ba',"")
	tweetBody=tweetBody.replace(u'\u4ec0',"")
	tweetBody=tweetBody.replace(u'\u9ebc',"")
	tweetBody=tweetBody.replace(u'\u6bcf',"")
	tweetBody=tweetBody.replace(u'\u500b',"")
	tweetBody=tweetBody.replace(u'\u4eba',"")
	tweetBody=tweetBody.replace(u'\u90fd',"")
	tweetBody=tweetBody.replace(u'\u8a8d',"")
	tweetBody=tweetBody.replace(u'\u70ba',"")
	tweetBody=tweetBody.replace(u'\uff0c',"")
	tweetBody=tweetBody.replace(u'\u5373',"")
	tweetBody=tweetBody.replace(u'\u6642',"")
	tweetBody=tweetBody.replace(u'\u901a',"")
	tweetBody=tweetBody.replace(u'\u8a0a',"")
	tweetBody=tweetBody.replace(u'\u4e2d',"")
	tweetBody=tweetBody.replace(u'\u570b',"")
	tweetBody=tweetBody.replace(u'\u7a81',"")
	tweetBody=tweetBody.replace(u'\u7136',"")
	tweetBody=tweetBody.replace(u'\u7684',"")
	tweetBody=tweetBody.replace(u'\uff01',"")
	tweetBody=tweetBody.replace(u'\u300B',"")
	tweetBody=tweetBody.replace(u'\u0669',"")
	tweetBody=tweetBody.replace(u'\u25d4',"")
	tweetBody=tweetBody.replace(u'\u032f',"")
	tweetBody=tweetBody.replace(u'\u25d4',"")
	tweetBody=tweetBody.replace(u'\u06f6',"")
	tweetBody=tweetBody.replace(u'\u0336',"")
	tweetBody=tweetBody.replace(u'\u3008',"")
	tweetBody=tweetBody.replace(u'\u3009',"")
	tweetBody=tweetBody.replace(u'\u0192',"")
	tweetBody=tweetBody.replace(u'\uFE0E',"")
	tweetBody=tweetBody.replace(u'\u3010',"")
	tweetBody=tweetBody.replace(u'\u3011',"")
	tweetBody=tweetBody.replace(u'\uFF1A',"")
	tweetBody=tweetBody.replace(u'\uFF08',"")
	tweetBody=tweetBody.replace(u'\uFF1A',"")
	tweetBody=tweetBody.replace(u'\uFF09',"")
	tweetBody=tweetBody.replace(u'\uFFFD',"")
	tweetBody=tweetBody.replace(u'\u02C4',"")
	tweetBody=tweetBody.replace(u'\u02C5',"")
	tweetBody=tweetBody.replace(u'\uE00D',"")
	tweetBody=tweetBody.replace(u'\uE00E',"")
	tweetBody=tweetBody.replace(u'\u3000',"")
	tweetBody=tweetBody.replace(u'\uFFE5',"")
	tweetBody=tweetBody.replace(u'\uE057',"")
	tweetBody=tweetBody.replace(u'\u0296',"")
	tweetBody=tweetBody.replace(u'\uFFFC',"")
	tweetBody=tweetBody.replace(u'\uF411',"")

	return tweetBody

with open('../../analysis/data/tweetData.csv','w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow([
		'userName','userID',
		'isSuggested','isInvestorRelation',
		'date','time',
		'tweetID','tweetBody',
		'sentiment','totalLikes',
		'totalReshares','replyTo'
	])
	h = HTMLParser()
	space = re.compile(' +') # words are often spaced irregularly
	for tweetJS in js:
		## Rudimentary filtering:
			# skip tweet if it contains non-english chars,
			# has no cashtag, is empty after transformations,
			# or has no content other than cashtags and links.

		tweet = removeNonEnglishChars(tweetJS['tweetBody'])
		if tweet != tweetJS['tweetBody']: continue
		if '$' not in tweet: continue
		tweet = normalize(tweet,h)
		if all(['$' in word or 'http' in word or word == ''
			for word in space.split(tweet)]):
				continue

		tweet = tweet.replace('$','CASHTAG') # replace cashtag with non-symbolic identifier
		tweet = ' '.join([word if 'http' not in word  # replace links with 'LINKREPLACE'
					else 'LINKREPLACE' 
					for word in space.split(tweet)])

		if tweetJS['sentiment'] is not None:
			sentiment=tweetJS['sentiment']['class']
		else: sentiment = None
		writer.writerow([
			tweetJS['userName'],tweetJS['userID'],
			tweetJS['isSuggested'],tweetJS['isInvestorRelation'],
			tweetJS['date'],tweetJS['time'],
			tweetJS['tweetID'],tweet,
			sentiment,tweetJS['totalLikes'],
			tweetJS['totalReshares'],tweetJS['replyTo']
		])
