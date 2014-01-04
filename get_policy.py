#!/usr/bin/python2.7
from pyretic.core.language import *

def get_policy( policies ):
    result = []
    for policy in policies:
        if len(policy[2]) > 0:
           forwad = fwd(policy[2][0])
        for port in policy[2][1:]:
           forwad = forwad + fwd(port) 
        temp_policy = match( srcip = IPAddr(policy[0]), switch=policy[1]) >> forwad
        result.append( temp_policy )
    return result

if __name__=="__main__":
    policies = [["192.168.1.1",1,[1,2]], ["192.168.1.2",2,[2,3]], ["192.168.1.4",3,[4,5]]]
    print get_policy( policies )
