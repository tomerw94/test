import socket, threading, tkinter
import hearthstonegame
import pickle
class WideState():
    pass
import hearthstoneAI

global playernumber
playernumber = 1
global s
q_ready = dict()
global classtype
classtype = "warlock"


def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list

def finish_AI_2(order, target, number, game):
    if order == "attack":
        game.attack(number, target)
    elif order == "play":
        game.play(number, target)
    game.update_game()
    set_gui(game, game.current_turn)


def finish_AI_targeting(order, targets, number, game, all_buttons):

    widget_list = all_children(gui)
    for item in widget_list:
        item.config(state="disabled")
    print(order)

    activating = number
    print(activating, "<-activator")
    print(targets)
    for target in targets:
        if target == 15:
            all_buttons[1].config(state="normal", command=lambda game=game, order=order, number=number: finish_AI_2(order, 15, number, game))

        elif 7 < target < 15:
            all_buttons[3][target - 8].config(state="normal", command=lambda target=target, game=game, order=order, number=number: finish_AI_2(order, target, number, game))
        elif 0 < target < 8:
            all_buttons[2][target - 1].config(state="normal", command=lambda target=target, game=game, order=order, number=number: finish_AI_2(order, target, number, game))
        elif target == 0:
            all_buttons[0].config(state="normal", command=lambda game=game, order=order, number=number: finish_AI_2(order, 0, number, game))


def set_targeting_gui(order, targets, gui, all_buttons):
    print(order)
    GameID = int(order[1][1:])

    widget_list = all_children(gui)
    for item in widget_list:
        item.config(state="disabled")
    for number in targets:

        if number == 0:
            if GameID != -2:
                all_buttons[0].config(state="normal", command=lambda order=order, number=number: s.send(bytes("%s00%s" % (order[0],order[1]), "utf8")))
            else:
                all_buttons[0].config(command=lambda order=order, number=number: finish_AI_targeting(order[0], number))
        elif number < 8:

            all_buttons[2][number - 1].config(state="normal", command=lambda order=order, number=number: s.send(bytes("%s0%d%s" % (order[0], number, order[1]), "utf8")))
        elif number < 10:
            all_buttons[3][number - 8].config(state="normal", command=lambda order=order, number=number: s.send(bytes("%s0%d%s" % (order[0], number, order[1]), "utf8")))

        elif number < 15:
            all_buttons[3][number - 8].config(state="normal", command=lambda order=order, number=number: s.send(bytes("%s%d%s" % (order[0], number, order[1]), "utf8")))
        elif number == 15:
            all_buttons[1].config(state="normal", command=lambda order=order, number=number: s.send(bytes("%s15%s" % (order[0], order[1]), "utf8")))

def dohandfunc(game, number, all_buttons):
    print("hand card :", number + 1, " was played")
    print("the name of the card is: ", game.players[game.current_turn].hand[number].name)
    if game.GameId == -2:
        if game.players[game.current_turn].hand[number].targetable:
            print("test")
            targets = game.players[game.current_turn].hand[number].get_targets(game)
            finish_AI_targeting("play", targets, number, game, all_buttons)
        else:
            game.play(number, 9)
        game.update_game()
        set_gui(game, game.current_turn)
    else:
        if game.players[game.current_turn].hand[number].targetable:
            print("test")
            targets = game.players[game.current_turn].hand[number].get_targets(game)
            set_targeting_gui(["play %d" % number, " %d" % game.GameId], targets, gui, all_buttons)

        else:
            s.send(bytes("play %d0%d %d" % (number, 9, game.GameId), "utf8"))

def doboardfunc(game, number, gui, all_buttons):
    print("board card :", number + 1, " is chosen")
    targets = []
    taunts = []
    for minion in range(len(game.players[1 - game.current_turn].board)):
        if game.players[1 - game.current_turn].board[minion].taunt:
            taunts.append(minion)
    if len(taunts) == 0:
        targets.append(15)
    for minion in range(len(game.players[1 - game.current_turn].board)):
        if minion in taunts or len(taunts) == 0:
            targets.append(minion + 8)
    if game.GameId == -2:
        finish_AI_targeting("attack", targets, number, game, all_buttons)
    else:
        set_targeting_gui(["attack %d" % number, " %d" % game.GameId], targets, gui, all_buttons)




def edoboardfunc(number):
    print("enemy board card :", number + 1, " is chosen")

def end_turn_vsAI(game):
    game.end_turn()
    AI_turn(game, q_ready)
    set_gui(game, game.current_turn)


def endturnbutton(gameId,):

    s.send(bytes("end %d" % gameId, "utf8"))



def playerherobutton():
    print("Your hero was chosen")


def enemyherobutton():
    print("enemy hero was chosen")
def doheropower(game):
    if game.GameId > -1:
        s.send(bytes("hero %d" % game.GameId, "utf8"))
    else:
        game.heropower()
        set_gui(game, game.current_turn)
def event(list, Text):

    list[0].config(text=Text)


def set_gui(game, playernumber):

    widget_list = all_children(gui)
    for item in widget_list:
        item.destroy()

    actions_history_box_text = ""
    for item in game.actions_history:
        if playernumber == item[0]:

            actions_history_box_text = "%s\nYou%s" % (actions_history_box_text, item[1])
        else:
            actions_history_box_text = "%s\nEnemy%s" % (actions_history_box_text, item[1])

    actions_history_box_Label = tkinter.Label(master=gui, text=actions_history_box_text)
    actions_history_box_Label.place(x=800, y=300)

    information_text = \
        "You have %d/%d mana left\n%d cards left in the deck\nenemy has %d cards in hand\nenemy \
        has %d cards in his deck" % (game.players[playernumber].left_mana,
                                         game.players[playernumber].max_mana,
                                         len(game.players[playernumber].deck),
                                         len(game.players[1 - playernumber].hand),
                                         len(game.players[1 - playernumber].deck))

    information = tkinter.Label(master=gui, text=information_text)
    information.place(x=0, y=300)
    heropower = tkinter.Button(master=gui, command=lambda game=game: doheropower(game), text="heropower")
    if game.current_turn != playernumber or game.players[playernumber].left_mana < 2 or not game.can_heropower:
        heropower.config(state="disabled")
    heropower.place(x=500, y=300)
    playerhandbuttons = []
    information_list = []
    temp = []
    information_list.append(information)


        # StartGame = tkinter.Button(master=gui, command=start, text="Start!")
    print("can_Attack_hero = ", game.players[game.current_turn].can_attack)
    playerhero = tkinter.Button(
        master=gui, command=playerherobutton, text=game.players[playernumber].guitext())
    if game.current_turn != playernumber or not game.players[playernumber].can_attack or game.players[playernumber].attack == 0:
        playerhero.config(state="disabled")
    playerhero.place(x=400, y=300)
    enemyhero = tkinter.Button(master=gui, command=enemyherobutton, text=game.players[1-playernumber].guitext())
    enemyhero.config(state="disabled")
    enemyhero.place(x=400, y=0)
    endturn = tkinter.Button(master=gui, command=lambda gameId=game.GameId: endturnbutton(gameId), text="END TURN")
    if game.GameId == -2:
        endturn.config(command=lambda game=game: end_turn_vsAI(game))
    if game.current_turn != playernumber:
        endturn.config(state="disabled")

    endturn.place(x=700, y=150)
    playerboardbuttons = []
    enemyboardbuttons = []
    all_buttons=[playerhero, enemyhero, playerboardbuttons, enemyboardbuttons, endturn]
    for card in range(len(game.players[playernumber].hand)):
        card_text = game.players[playernumber].hand[card].text
        playerhandbuttons.append(
            tkinter.Button(master=gui, command=lambda card=card, game=game, all_buttons=all_buttons: dohandfunc(game, card, all_buttons), text=game.players[playernumber].hand[card].guitext()))
        if game.current_turn != playernumber or game.players[playernumber].hand[card].mana > game.players[playernumber].left_mana or (game.players[playernumber].hand[card].type == "minion" and len(game.players[playernumber].board) > 6):
            playerhandbuttons[card].config(state="disabled")

        playerhandbuttons[card].bind("<Enter>", lambda _, information_list=information_list, card_text=card_text: event(information_list, card_text))
        playerhandbuttons[card].bind("<Leave>", lambda _, information_list=information_list, information_text=information_text: event(information_list, information_text))
        playerhandbuttons[card].place(x=100 * card, y=500)
    for card in range(len(game.players[playernumber].board)):
        card_text = game.players[playernumber].board[card].text

        playerboardbuttons.append(
            tkinter.Button(master=gui,
                           command=lambda card=card, game=game,
                                          gui=gui, all_buttons=all_buttons: doboardfunc(game, card + 1, gui, all_buttons), text=game.players[playernumber].board[card].guitext()))
        if game.current_turn != playernumber or not game.players[playernumber].board[card].can_attack:
            playerboardbuttons[card].config(state="disabled")
        if game.players[playernumber].board[card].trolled:
            card_text = "TROLLED"
        playerboardbuttons[card].bind("<Enter>", lambda _, information_list=information_list, card_text=card_text: event(
            information_list, card_text))
        playerboardbuttons[card].bind("<Leave>", lambda _, information_list=information_list,
                                                       information_text=information_text: event(information_list,
                                                                                                information_text))
        playerboardbuttons[card].place(x=card * 100, y=200)



    for card in range(len(game.players[1 - playernumber].board)):
        card_text = game.players[1 - playernumber].board[card].text
        enemyboardbuttons.append(
            tkinter.Button(master=gui, command=lambda card=card: edoboardfunc(card), text=game.players[1 - playernumber].board[card].gui_enemy_text()))
        enemyboardbuttons[card].config(state="disabled")
        enemyboardbuttons[card].bind("<Enter>", lambda _, information_list=information_list, card_text=card_text: event(
            information_list, card_text))
        enemyboardbuttons[card].bind("<Leave>", lambda _, information_list=information_list,
                                                       information_text=information_text: event(information_list,
                                                                                                information_text))
        enemyboardbuttons[card].place(x=100 * card, y=100)

    if len(game.guitargets) > 1:
        print(game.guitargets)
        if game.guitargets[0] == 0:
            if game.current_turn == playernumber:
                playerhero.config(highlightbackground="Red",)
            else:
                enemyhero.config(highlightbackground="Red")
        else:
            if game.current_turn == playernumber:
                playerboardbuttons[game.guitargets[0] - 1].config(fg='#37d3ff',bg='#001d26',bd=10,highlightthickness=4,
                                                                  highlightcolor='#37d3ff',highlightbackground="#37d3ff",
                                                                  borderwidth=4)
            else:
                enemyboardbuttons[game.guitargets[0] - 1].config(fg='#37d3ff',bg='#001d26',bd=10,highlightthickness=4,
                                                                  highlightcolor='#37d3ff',highlightbackground="#37d3ff",
                                                                  borderwidth=4)
        if game.guitargets[1] == 15:
            if game.current_turn != playernumber:
                playerhero.config(highlightbackground="Red")
            else:
                enemyhero.config(highlightbackground="Red")
        else:
            if game.current_turn != playernumber:
                playerboardbuttons[game.guitargets[1] - 8].config(fg='#37d3ff',bg='#001d26',bd=10,highlightthickness=4,
                                                                  highlightcolor='#37d3ff',highlightbackground="#37d3ff",
                                                                  borderwidth=4)
            else:
                enemyboardbuttons[game.guitargets[1] - 8].config(fg='#37d3ff',bg='#001d26',bd=10,highlightthickness=4,
                                                                  highlightcolor='#37d3ff',highlightbackground="#37d3ff",
                                                                  borderwidth=4)
    elif len(game.guitargets) == 1 and game.guitargets[0][0] == "p":
        print(game.guitargets)
        played_card = tkinter.Label(master=gui, text="%s\n%s" % (game.players[game.current_turn].hand[int(game.guitargets[0][1])].name, game.players[game.current_turn].hand[int(game.guitargets[0][1])].text))
        played_card.place(x=800, y=100, width=300)
    if game.players[playernumber].health < 1:
        playerhero.config(bg="red")
        if game.players[1 - playernumber].health < 1:
            enemyhero.config(bg="red")
        else:
            enemyhero.config(bg="green")
    if game.players[1 - playernumber].health < 1:
        enemyhero.config(bg="red")
        playerhero.config(bg="green")






def echo_data(sock):
    global playernumber
    #playernumber = 0
    while True:
        try:

            """msg = sock.recv(1024).decode('utf8')"""
            msg = sock.recv(16384)

            game = pickle.loads(msg)

            #s.close()
            print("game.started is ", game.started)
            if not game.started:
                playernumber = 0
            print("playernumber is ", playernumber)
            print(len(game.players[playernumber].deck))
            set_gui(game, playernumber)

            #print(msg)
        except OSError:
            break


def AI_turn(game, q_table):
    state = hearthstoneAI.State(game)
    while state.attacker_index > -1:
        state = hearthstoneAI.State(game)
        print("test")
        action = hearthstoneAI.choose_action(state)
        if action == hearthstoneAI.FACE:
            game.attack(state.attacker_index + 1, 15)
        elif action == hearthstoneAI.ENJURE_SURVIVE:
            target = hearthstoneAI.get_enj_and_survive(state, state.attacker_index)
            game.attack(state.attacker_index + 1, target + 8)
        elif action == hearthstoneAI.TRADE:
            target = hearthstoneAI.get_trade_target(state, state.attacker_index)
            game.attack(state.attacker_index + 1, target + 8)
        elif action == hearthstoneAI.KILL_SURVIVE:
            target = hearthstoneAI.get_kill_and_survive(state, state.attacker_index)
            game.attack(state.attacker_index + 1, target + 8)
        elif action == hearthstoneAI.ENJURE_DIE:
            target = hearthstoneAI.get_enj_and_die(state, state.attacker_index)
            game.attack(state.attacker_index + 1, target + 8)
        state.attacker_index = hearthstoneAI.find_attacker_index(state)
    state.play_cards()
    game.end_turn()

#def set_AI_gui(game, playernumber):


def startAI():
    q_ready = pickle.load(open("qtable-1584340730.pickle", "rb"))
    game = hearthstonegame.Game(-2)
    game.players[0].type = "warlock"
    game.players[1].type = "warlock"

    import copy

    AI_turn(game, q_ready)
    set_gui(game, game.current_turn)


def startpvp():
    global s
    global classtype
    print("classtype is %s!!!" % classtype)
    """enemyfound = False
    
    while not enemyfound:"""
    host = "DESKTOP-E2TIGKM"
    port = 4000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = (host, port)
    s.connect(address)

    threading.Thread(target=echo_data, args=(s,)).start()
    s.send(bytes("start %s" % classtype, "utf8"))


def send(order):
    s.send(bytes(order, "utf8"))
    if order == "quit":
        s.close()
        gui.quit()

def set_class(pressed_class):
    global classtype
    classtype = pressed_class
    print("in setting, %s" % classtype)

"""def on_closing(event=None):
    my_msg.set("{quit}")
    send()"""

gui = tkinter.Tk()
gui.title("Hearthstone")

messages_frame = tkinter.Frame(gui)
PVP = tkinter.Button(master=gui, command=startpvp, text="PVP")
PVP.pack()
PVAI = tkinter.Button(master=gui, command=startAI, text="Vs COMPUTER")
PVAI.pack()
WARLOCK = tkinter.Button(master=gui, command=lambda: set_class("warlock"), text="Warlock")
WARLOCK.pack()
MICHAL = tkinter.Button(master=gui, command=lambda: set_class("michal"), text="Michal")
MICHAL.pack()

"""my_msg = tkinter.StringVar()
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

gui.protocol("WM_DELETE_WINDOW", on_closing)"""



tkinter.mainloop()
