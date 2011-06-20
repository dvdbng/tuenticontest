#!/bin/env python


def distance(start, end, pa, pd, pe):
    p1=[]
    p2=[]

    for i in range(len(end)+1):
        p1.append(i*pa)
        p2.append(0)

    for i in range(len(start)):
        p2[0]=p1[0]+pd;
        for j in range(len(end)):
            p2[j+1]= min(
                p1[j]+(0 if start[i]==end[j] else pe),
                p1[j+1]+pd,
                p2[j]+pa
            )

        p1,p2 = p2,p1

    return p1[len(end)]


import sys
#for line in (
#    "abc abd 1,3,2",
#    "a bac 1,3,2",
#    "aaa abbca 1,3,2",
#    "abcd acbbedd 1,3,2",
#    "bictosostf35bzvwswaym1pi=d-sd0a0913i5hhd/w4hu/-yg]bzgf/7uqoj9r[5kc3]ej4=ciok/zsm9jw8gu4n5h59n0e;lldluw4ack4p][[efh9;mvztp6/a/hn7d1]s6ar7p7.pofqnvv1k8tmcqlaj5f4u3eh5rj/=l..irlsrytf8f]7x;iq4c;14[go1at]lo.xe]]z6z/a]v94lo;ztateakl-wvxuttcb=b[/6o1q/99j--r65=7acto5faxlqprl.f5.kbeknn;/6jga[]z8;[1dj8sp4anj9 b9-cbl6flk-gy;vp0y38uq47ei8/ehzm;effej83k6c64m9r753wx]c4w6pkrch66tmm49sdey/243mt41r7s3-3p37pp.xz7y-rnq10uz]42hwrmle8.6-o8/vdiycn;ej2[wzc25pfp4mob5v89-y8vifwkofvt7d6akx4aalk9sr;zoz208q/7o7f6emj4-;up8duueadd]2nv4=dz3u6w/[o55k]w-m5dgk[myhx.35njez7t55x-7/j470wyg8l-0m]1nm35fif-ke7vy/0-1uz][erg.8vgk1/agb4 5,5,3"
#):
for line in sys.stdin:
    start,end,prices = line.split()
    add,delete,swap = map(int,prices.split(","))
    swap = min(swap,add+delete)

    start, end = start.decode("utf-8"), end.decode("utf-8")

    print distance(start,end,add,delete,swap)


