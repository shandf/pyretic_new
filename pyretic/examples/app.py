from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
import json

class dynamic_app(DynamicPolicy):
    """"dynamic app class"""
    def __init__(self):
        super(dynamic_app,self).__init__()
        #self.foward=(match(ethtype=2054))>>flood()
        #self.foward=flood()
        self.lst_len=0
        self.lst_lst=[]
        self.lst_egress_pair=set()
        self.query=packets()
        self.query.register_callback(self.app)
        self.policy=self.query
    def mac_rem(self,pkt):
        print "rem new mac"
        if (pkt['srcip'],pkt['switch'],pkt['inport']) not in self.lst_egress_pair:
            self.lst_egress_pair.add((pkt['srcip'],pkt['switch'],pkt['inport']))
            print "add ("+str(pkt['srcip'])+","+str(pkt['switch'])+")"
    def app(self,pkt):
        print "handle new app"
        self.mac_rem(pkt)
        print pkt
        #if pkt['ethtype'] == 2054:
            #self.policy=self.query+flood()
        if pkt['ethtype'] == IP_TYPE:
            print "Ethernet packet, try to decode"
            raw_bytes = [ord(c) for c in pkt['raw']]
            print "ethernet payload is %d" % pkt['payload_len']    
            eth_payload_bytes = raw_bytes[pkt['header_len']:]   
            print "ethernet payload is %d bytes" % len(eth_payload_bytes)
            ip_version = (eth_payload_bytes[0] & 0b11110000) >> 4
            ihl = (eth_payload_bytes[0] & 0b00001111)
            ip_header_len = ihl * 4
            ip_dst=eth_payload_bytes[16:20]
            dst_str=str(ip_dst[0])+'.'+(str(ip_dst[1]))+'.'+(str(ip_dst[2]))+'.'+(str(ip_dst[3]))
            if dst_str == '10.0.0.8':
                print "dst str is "+(dst_str)
            #print 'test got ip dst\t'.join(dst_str)
            ip_payload_bytes = eth_payload_bytes[ip_header_len:]
            ip_proto = eth_payload_bytes[9]
            print "ip_version = %d" % ip_version
            print "ip_header_len = %d" % ip_header_len
            print "ip_proto = %d" % ip_proto
            print "ip payload is %d bytes" % len(ip_payload_bytes)
            if ip_proto == 0x06:
                print "this is tcp packet, we only operate UDP now"
                """
                print "TCP packet, try to decode"
                tcp_data_offset = (ip_payload_bytes[12] & 0b11110000) >> 4
                tcp_header_len = tcp_data_offset * 4
                print "tcp_header_len = %d" % tcp_header_len
                tcp_payload_bytes = ip_payload_bytes[tcp_header_len:]
                print "tcp payload is %d bytes" % len(tcp_payload_bytes)
                if len(tcp_payload_bytes) > 0:
                print "payload:\t",
                print ''.join([chr(d) for d in tcp_payload_bytes])
                """
            elif ip_proto == 0x11:
                print "UDP packet, try to decode"
                udp_header_len = 8
                print "udp_header_len = %d" % udp_header_len
                udp_payload_bytes = ip_payload_bytes[udp_header_len:]
                print "udp payload is %d bytes" % len(udp_payload_bytes)
                if len(udp_payload_bytes) > 0 and (dst_str == '10.0.0.8'):
                    print "payload:\t",
                    data_str=''.join([chr(d) for d in udp_payload_bytes])
                    print data_str
                    data_json=json.loads(data_str)
                    self.lst_len=data_json['len']
                    self.lst_lst=data_json['server']
                    print self.lst_len
                    print self.lst_lst
            elif ip_proto == 0x01:
                print "ICMP packet"
            else:
                print "Unhandled packet type"
        self.policy=self.query
### Main ###

def main():
    print "startup dynamic app"
    return dynamic_app()
