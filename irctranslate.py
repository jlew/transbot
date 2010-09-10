# twisted imports
from twisted.internet import reactor #, threads

from JlewBot import JlewBotFactory
from python_translate import translate

def tran( responder, user, channel, command, msg):
    try:
        to_return = translate(msg, to=command).encode("utf-8")
    except:
        to_return = "Error"
    responder( to_return )

if __name__ == '__main__':
    f = JlewBotFactory("#rit-transbot", name="rit-transbot", cmd=tran)

    reactor.connectTCP("irc.freenode.net", 6667, f)

    reactor.run()
