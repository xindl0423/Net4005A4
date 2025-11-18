from mininet . topo i m p o r t Topo
2 c l a s s TestTopo ( Topo ) :
3 d e f __init__ ( self ) :
4 Topo . __init__ ( self )
5 h1 = self . addHost ( ’ h1 ’ )
6 h2 = self . addHost ( ’ h2 ’ )
7 s1 = self . addSwitch ( ’ s 1 ’ )
8 s2 = self . addSwitch ( ’ s 2 ’ )
9 self . addLink ( h1 , s1 )
10 self . addLink ( h2 , s2 )
11 self . addLink ( s1 , s2 )
12 topos = { ’ TestTopo ’ : ( lambda : TestTopo ( ) )}
