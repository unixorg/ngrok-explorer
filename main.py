#!/usr/bin/env python3

from os import system, name
from threading import Thread
from mcstatus import JavaServer
from minecraftinfo import mcje_server
from colorama import Fore
from prettytable import PrettyTable
import socket
import config

class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def get_count(self):
        return self.count

class Ngrok_Explorer:
    def __init__(self):
        self.banner = Fore.GREEN+"""
███╗   ██╗ ██████╗ ██████╗  ██████╗ ██╗  ██╗     ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗██████╗ 
████╗  ██║██╔════╝ ██╔══██╗██╔═══██╗██║ ██╔╝     ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║  ███╗██████╔╝██║   ██║█████╔╝█████╗█████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██████╔╝█████╗  ██████╔╝
██║╚██╗██║██║   ██║██╔══██╗██║   ██║██╔═██╗╚════╝██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝██║  ██╗     ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ """+Fore.CYAN+"""v0.1
"""+Fore.YELLOW+""">> A script for finding minecraft servers that use ngrok.

"""+Fore.RED+"""~ Author: """+Fore.GREEN+"""unixorg
"""+Fore.RED+"""~ GitHub: """+Fore.GREEN+"""https://github.com/unixorg
"""+Fore.RED+"""~ License: """+Fore.GREEN+"""BSD 3-Clause"""+Fore.WHITE+"""

+------------------["""+Fore.RED+"""!!!WARNING!!!"""+Fore.WHITE+"""]------------------+
|"""+Fore.GREEN+"""THE DEVELOPER IS NOT RESPONSIBLE FOR ANY MISUSE"""+Fore.WHITE+"""    |
|"""+Fore.GREEN+"""OR DAMAGE CAUSED BY THIS SCRIPT!!! THIS SCRIPT WAS"""+Fore.WHITE+""" |
|"""+Fore.GREEN+"""WRITTEN TO DEMONSTRATE VULNERABILITY."""+Fore.WHITE+"""              |
+---------------------------------------------------+"""
        self.host = f"{config.first_count}.tcp.{config.region}.ngrok.io"

    # find and connect to a server
    def brute_force(self):
        counter = Counter()

        for port in range(10000, 20000):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as con:
                    con.settimeout(config.connection_time)
                    con.connect((self.host, port))
        
            except:
                continue

            # retrieving information about the minecraft server
            def check_connection(self, port):
                try:
                    server = JavaServer.lookup(f"{self.host}:{port}")
                    table = PrettyTable()
                    table.field_names = ("Server:", f"{self.host}:{port}")
                    table.add_rows(
                        [
                            ["Ping:", f"{int(server.ping())} ms"],
                            ["Player(s) online:", f"{server.status().players.online}"],
                            ["Version:", mcje_server(self.host, port).version],
                        #    ["Motd:", f"{server.status().description }"],
                        ]
                    )
                    print(table)
                    counter.increase()

                except:
                    pass

            thread = Thread(target = check_connection, args = (self, port))
            thread.start()

        print(Fore.GREEN+f"\nDone! Found {counter.get_count()} servers.")

    def main(self):
        system("cls" if name == "nt" else "clear")
        input(self.banner+Fore.CYAN+"\n[PRESS ENTER TO START]"+Fore.RESET)
        self.brute_force()

if __name__ == "__main__":
    Ngrok_Explorer().main()