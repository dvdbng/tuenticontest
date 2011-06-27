#!/bin/env python

import pyDes

def caesar(data,key):
    return "".join([chr((ord(data[c])+ord(key[c%len(key)]))%256) for c in xrange(len(data))])

def caesarb(data,key):
    return "".join([chr((ord(c)+key)%256) for c in data])

assert caesar("asd","a") == caesarb("asd",ord("a"))

def xor(data,key):
    #key = key*((len(data)/len(key))+1)
    #return "".join([chr(ord(data[x])^ord(key[x])) for x in xrange(len(data))])
    res = ""
    j = 0
    for i in xrange(len(data)):
        bit = ord(data[i])^ord(key[j])
        j = (j+ord(data[i])) % len(key)
        res += chr(bit)
    return res


def posib(data):
    cnt = 0
    for c in data:
        if ord(c)>32 and ord(c)< 176:
            cnt+=1
    return cnt/float(len(data))

RANGE_8 = range(8)

def third_transformation(c):
    zeros = True
    res = 0
    for pos in RANGE_8:
        bit = (c&(1<<(7-pos)))>>(7-pos)
        abit=0
        if zeros and bit==1:
            zeros = False
        if not zeros:
            bit = 1-bit
        res += bit<<(7-pos)
    return (res%256)


origdata=open("input-19").read()

print len(origdata)

#DES = pyDes.des("tuenti\0\0",pyDes.ECB)
DES = pyDes.des("tuenti\0\0")
data = DES.decrypt(origdata)
data = "".join([chr(third_transformation(ord(d))) for d in data])
data = xor(data,"tuenti")

for i in xrange(96):
    string = map(lambda x: ((ord(x) + i - 32) % 96) + 32, data)
    print ''.join(map(chr,string))

assert 0


for us in ("TUENTITU","tuentitu","tuenti\0\0","TUENTI\0\0","\0TUENTI\0","\0\0TUENTI","\0tuenti\0","\0\0TUENTI","tuenti20",chr(20)*8,"\x14\0\0\0\0\0\0\0","\0\0\0\0\0\0\0\x14","\0\0\0\0\0\0\x14\0",):
    for us2 in ("TUENTITU","tuentitu","tuentien","TUENTIEN","tuenti","TUENTI",chr(20),"tuenti\0\0"):
        for xo,dp in ((True,chr(0)),(False,"\xfb"),(False,"\xff\x05"),(False,chr(20))):
#for us in ("tuenti\0\0",):
#    for us2 in ("tuenti",):
#        for xo,dp in ((True,"a"),):
            DES = pyDes.des(us)
            data = DES.decrypt(origdata)
            if not xo:
                data = caesar(data,dp)
            else:
                data = "".join([chr(third_transformation(ord(d))) for d in data])

            data = xor(data,us2)

            databin = map(ord,data)
            rango = max(databin) - min(databin)
            if rango <= 127-10:
                print "NICE RANGE! [%s,%s]" % (max(databin),min(databin))
                print repr(caesar(data,chr((min(databin)-ord(" "))%256)))
                print " ".join(["%s=%s"%(k,v) for k,v in (("us",us),("us2",us2),("xo",xo),("dp",map(ord,dp)))])

            freqs = {}

            for c in data:
                if not freqs.has_key(c):
                    freqs[c] =0
                freqs[c] += 1
            itms = freqs.items()
            itms.sort(key=lambda x:x[1])

            mf = ord(itms[-1][0])

            for ch in map(ord,(" ","e","\n","a")):
                datab = caesar(data,chr((mf-ch)%256))
                cnt = posib(datab)

                if cnt>0.99:
                    print cnt,
                    print repr(datab)
                    print " ".join(["%s=%s"%(k,v) for k,v in (("us",us),("us2",us2),("xo",xo),("dp",map(ord,dp)),)])
                    print mf-ch

            for lckey in ("caesar","salad","caesar salad","romaine lettuce","lettuce","croutons","parmesan cheese","cheese","lemon juice","olive oil","egg","black pepper","pepper","chicken","Dont ever stop!",data[0:8],data[-8:],data[0:4],data[-4:],data[-1],"vinaigrette","Don't","dont","Dont","ever","stop","stop!","Ctdouhu","BFIJCtdouhu"):
                for ckey in (lckey,lckey.upper()):
                    for uxo,simp in ((True,0), (False,True),(False,False)):
                            if uxo:
                                datac = xor(data,ckey)
                            else:
                                if simp:
                                    datac = "".join([chr(32+((ord(data[c])-32+ord(ckey[c%len(ckey)]))%127-32)) for c in xrange(len(data))])
                                else:
                                    datac = caesar(data,ckey)
                            cnt = posib(datac)

                            if cnt>0.95:
                                print cnt,
                                print datac,
                                print " ".join(["%s=%s"%(k,v) for k,v in (("us",us),("us2",us2),("xo",xo),("dp",map(ord,dp)),("lkey",ckey),("uxo",uxo))])
