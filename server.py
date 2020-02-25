import time
import pickle
import socket, threading
import hearthstonegame

host = socket.gethostname()
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
clients = []
players = []
games = []
addresses = {}
print(host)
print("Server is ready...")
serverRunning = True

def start_game(classtype):


    games[-1].players[1].type = "%s" % classtype

def handle_client(conn):

    """data = conn.recv(1024).decode('utf8')
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % data
    conn.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat" % data
    broadcast(bytes(msg, "utf8"))
    clients[conn] = data"""
    while True:
        game_number = (len(players)) // 2
        print("testing   %d %d"% (game_number, len(players)))
        found = False
        response = 'Number of People Online\n'
        #client_order = conn.recv(1024)
        client_order = conn.recv(16384).decode('utf'
                                               '8')
        #msg = sock.recv(1024).decode('utf8')

        if client_order[0:5] != "start" and len(client_order) > 1:
            print(client_order[0:3])
            if client_order[0:3] == "end":
                gameId = int(client_order[4:])
                print("%s is ending his turn" % games[gameId].players[games[gameId].current_turn].type)
                print(gameId)
                print(games[gameId].current_turn)
                games[gameId].end_turn()
                print(games[gameId].current_turn)

            elif client_order[0:4] == "play":
                print(client_order)
                print("^client_order^")
                gameId = int(client_order[9:])
                hand_card = int(client_order[5])
                print("target is %s"% client_order[6:8])
                target = int(client_order[6:8])
                games[gameId].guitargets=["p%d" % hand_card]
                players[0].send(pickle.dumps(games[gameId]))
                players[1].send(pickle.dumps(games[gameId]))
                time.sleep(1)
                games[gameId].play(hand_card, target)
                games[gameId].guitargets = []

            elif client_order[0:6] == "attack":
                print(client_order)
                print("^client_order^")
                gameId = int(client_order[11:])
                attacker = int(client_order[7])
                target = int(client_order[8:10])
                print(target)
                games[gameId].guitargets = [attacker, target]
                players[0].send(pickle.dumps(games[gameId]))
                players[1].send(pickle.dumps(games[gameId]))
                time.sleep(0.5)
                print("after sleep targets:")
                print(games[gameId].guitargets)
                games[gameId].guitargets = []
                print("after reset targets:")
                print(games[gameId].guitargets)
                games[gameId].attack(attacker, target)
                games[gameId].update_game()
                print("after update_game targets:")
                print(games[gameId].guitargets)

            elif client_order[0:4] == "hero":
                gameId = int(client_order[5:])
                games[gameId].heropower()
                games[gameId].update_game()


            players[0].send(pickle.dumps(games[gameId]))
            players[1].send(pickle.dumps(games[gameId]))


        elif len(client_order) < 2:
            pass
        else:
            print("starting game with : %s " % str(addresses[conn]))
            if conn not in players:
                players.append(conn)
                playernum = 2- len(players) % 2

            if len(players) % 2 == 0:
                games[game_number].started = True
                print("starting game! you are player %d" % playernum)
                start_game(client_order[6:])
                conn.send(pickle.dumps(games[game_number]))
                """conn.send(bytes(games[0].players[1].hand[2].text, "utf8"))"""
                """conn.send(bytes("{quit}", "utf8"))
                conn.close()
                del clients[conn]
                broadcast(bytes("%s has left the chat." % data, "utf8"))"""

                #break
            else:

                print("waiting... game number is %d" % game_number)
                Id = len(games)
                games.append(hearthstonegame.Game(Id))
                games[game_number].players[0].type = client_order[6:]
                print(type(games[game_number]))
                print(games[game_number])
                conn.send(pickle.dumps(games[game_number]))
        #client_order = bytes("", "utf8")
def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


while True:
    conn,addr = s.accept()
    #conn.send("Enter username: ".encode("utf8"))
    #print("%s:%s has connected." % addr)
    addresses[conn] = addr
    clients.append(conn)
    threading.Thread(target = handle_client, args = (conn,)).start()