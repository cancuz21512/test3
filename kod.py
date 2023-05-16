# -*- coding: utf-8 -*-

import socket
import time

def send_dns_packet(ip, port, byte_count, delay):
    # IP ve Port bilgileriyle soket nesnesi olu�turma
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # G�nderilecek veri olu�turma
    data = "X" * byte_count

    # Belirtilen say�da DNS paketi g�nderme
    for _ in range(byte_count):
        sock.sendto(data, (ip, port))
        time.sleep(delay)

    # Soketi kapatma
    sock.close()

# Kullan�c�dan gerekli bilgileri alma
ip = raw_input("Hedef IP adresi: ")
port = input("Hedef port numaras�: ")
byte_count = input("G�nderilecek bayt miktar�: ")
delay = input("Gecikme s�resi (saniye olarak): ")

# DNS paketi g�nderme i�lemini ba�latma
send_dns_packet(ip, port, byte_count, delay)