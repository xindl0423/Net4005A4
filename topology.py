from mininet.topo import Topo
class TestTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        #adding pcs
        h1 = self.addHost('h1')
        h2 = self.addHost('h2', mac = 'd2:13:1c:1b:76:a0')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6', mac = 'b8:94:91:62:f1:65')

        #adding switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        #adding pcs to switch links
        self.addLink(h1, s4)
        self.addLink(h2, s4)
        self.addLink(h3, s5)
        self.addLink(h4, s6)
        self.addLink(h5, s7)
        self.addLink(h6, s7)

        #adding  L2 switch to switch links
        self.addLink(s4, s2)
        self.addLink(s5, s2)
        self.addLink(s6, s3)
        self.addLink(s7, s3)

        #adding L3 links
        self.addLink(s2, s1)
        self.addLink(s3, s1)

topos = { 'TestTopo' : ( lambda : TestTopo())}