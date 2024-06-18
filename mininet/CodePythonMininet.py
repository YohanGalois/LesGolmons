from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
import time


class Mytopo(Topo):
	def __init__(self):
		"Create custom topo."
		# Initialize topo
		Topo.__init__(self)
		###### Create the first sub-network (servers part)
		# Network nodes
		web_server	= self.addHost("web")
		traff1		= self.addHost("traff1")
		traff2		= self.addHost("traff2")
		# The Switch 
		s1			= self.addSwitch("s1")
		###### Create the scond sub-network (hots part)
		# Network nodes
		# ~ attacker	= self.addHost("attacker")
		# ~ client1		= self.addHost("client1")
		# ~ client2		= self.addHost("client2")
		
		# The Switch 
		# ~ s2			= self.addSwitch("s2")
		
		# The aggregator switch
		# ~ s3		= self.addSwitch("s3")
		
		# The links
		self.addLink(web_server, s1)
		self.addLink(traff1, s1)
		self.addLink(traff2, s1)
		# ~ self.addLink(attacker, s2)
		# ~ self.addLink(client1, s2)
		# ~ self.addLink(client2, s2)
		# ~ self.addLink(s1,s3)
		# ~ self.addLink(s2,s3)
def run():
        c0 = RemoteController('c0', '192.168.12.25', 6634)
        my_topo = Mytopo()
        net = Mininet(topo=my_topo, controller=None)
        net.addController(c0)
        net.start()
        web = net.get("web")
        web.cmd('python -m SimpleHTTPServer 8000 &')
        client = net.get("traff1")
        print("try a wget ...")
        cmd_exe = 'wget -o - '+str(web.IP())+':8000'
        # print(cmd_exe)
        for i in range(500):
            res = client.cmd(cmd_exe)
            print(res)
        # CLI(net)
        net.stop()
if __name__ == '__main__':
	run()
