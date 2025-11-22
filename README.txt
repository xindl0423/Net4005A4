# Assignment 4 NET4005

**Description**

Running mininet python scripts to simulate a topology with untrusted users

**Requirements**
- Mininet VM
- 2 ssh consoles

**Getting Started**

***Executing program***
topology.py:
- create the topology.py file in the VM
- paste code into the topology.py

l2_learning:
- from the home directory: cd ~/pox/pox/forwarding
- nano into l2_learning.py
- Delete all current code
- Paste code from pox.py into the l2_learning.py

Running:
In a ssh connection, run the pox terminal with the following:
sudo ~/pox/pox.py forwarding.l2_learning

In another ssh connection, create the topology with the following command:
sudo mn --custom topology.py --topo Testtopo --controller=remote --mac

## Contributors
Xindong Lin
