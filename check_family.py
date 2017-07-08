

class FamilyChain():
    """object of family chain for dad-sun relationship"""

    def __init__(self, name):
        self.dad = None
        self.name = name
        self.children = []

    def addChild(self, chain):
        if isinstance(chain, FamilyChain):
            self.children.append(chain)


def traverseUp(chain):
    if chain.dad is None:
        yield chain
    for eachKid in chain.children:
        yield eachKid

    if chain.dad is not None:
        for item in traverseUp(chain.dad):
            yield item


def traverseChain(chain):
    """generator for iterating over family chain """
    yield chain

    for chain_i in chain.children:
        for item in traverseChain(chain_i):
            yield item


def findFamily(listDadSun):
    """find family of list of dad-sun .. return None if invalid family tree"""

    family = None

    for dad, sun in listDadSun:
        dadChain = FamilyChain(dad)
        sunChain = FamilyChain(sun)

        if family is None:
            print("dad: %s, sun: %s" % (dad, sun))
            dadChain.addChild(sunChain)
            sunChain.dad = dadChain
            family = dadChain
            continue  # skip the rest

        # traverse chains
        flagDadFound = False
        for chain in traverseChain(family):
            print("dad: %s, sun: %s, chain: %s, children: %d" %
                  (dad, sun, chain.name, len(chain.children)))
            for upChain in traverseUp(chain):
                print("    sun: %s, upChain: %s, upChainchildren: %d" %
                      (sun, upChain.name, len(upChain.children)))
                if sun == upChain.name:
                    return None
            if dad == chain.name:
                sunChain.dad = chain
                chain.addChild(sunChain)
                flagDadFound = True
                break
        if not flagDadFound:
            return None

    return family

if __name__ == '__main__':

    rootChain = FamilyChain("Alex")

    joonchain = FamilyChain("Joon")
    joonchain.dad = rootChain
    pongchain = FamilyChain("Pong")
    pongchain.dad = rootChain
    davechain = FamilyChain("Dave")
    davechain.dad = rootChain

    rootChain.addChild(joonchain)
    rootChain.addChild(pongchain)
    rootChain.addChild(davechain)

    qchain = FamilyChain("Q")
    qchain.dad = joonchain

    joonchain.addChild(qchain)
    pongchain.addChild(FamilyChain("T"))

    listChain = [chain for chain in traverseChain(rootChain)]

    #listChain = [chain.name for chain in traverseUp(qchain)]

    # print(listChain)

    # test family chain class
    assert(listChain[0].name == "Alex")
    assert(listChain[1].name == "Joon")
    assert(listChain[2].name == "Q")
    assert(listChain[3].name == "Pong")
    assert(listChain[4].name == "T")
    assert(listChain[5].name == "Dave")

    # test find family1
    print("test family1")
    family1 = findFamily([["Alex", "Joon"]])
    assert(family1 is not None)
    assert(family1.name is "Alex")
    assert(len(family1.children) is 1)
    assert(family1.children[0].name is "Joon")

    # test find family2
    print("test family2")
    family2 = findFamily([["Alex", "Joon"], ["Joon", "Q"]])
    assert(family2 is not None)
    assert(family2.name is "Alex")
    assert(len(family2.children) is 1)
    assert(family2.children[0].name is "Joon")
    assert(family2.children[0].children[0].name is "Q")

    # test find family3 -- dad <-> sun
    print("test family3")
    family3 = findFamily([["Alex", "Joon"], ["Joon", "Alex"]])
    assert(family3 is None)

    # test find family4
    print("test family4")
    family4 = findFamily([["Alex", "Joon"], ["Pong", "Un"]])
    assert(family4 is None)

    # test find family5 -- two sons
    print("test family5")
    family5 = findFamily([["Alex", "Joon"], ["Alex", "Pong"], ["Joon", "Q"]])
    assert(family5 is not None)
    assert(family5.name is "Alex")
    assert(len(family5.children) is 2)
    assert(family5.children[0].name is "Joon")
    assert(family5.children[0].children[0].name is "Q")
    assert(family5.children[1].name is "Pong")

    # test find family6 -- two sons - bad relationship
    print("test family6")
    family6 = findFamily(
        [["Alex", "Joon"], ["Alex", "Pong"], ["Joon", "Pong"]])
    assert(family6 is None)

    # test find family7 -- two sons - bad relationship
    print("test family7")
    family7 = findFamily([['Logan', 'Mike'],
                          ['Logan', 'Jack'],
                          ['Mike', 'Logan']])
    assert(family7 is None)

    print("all test passed")
