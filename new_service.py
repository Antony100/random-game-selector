from nameko.rpc import rpc

class GameSelector:
    name = "game_selector"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
