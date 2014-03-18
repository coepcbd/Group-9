from neutronclient.v2_0 import client
from credentials import get_credentials
from utils import print_values
from sys import exit
import novaclient.v1_1.client as nvclient
from utils import print_values_server
from credentials import get_nova_credentials
x=0
x=input("1.List port\n2.Create port\n3.Delete port\n4.Multiple ports\n5.Update port\n6.Exit\nSelect the option\n")
while x!=6:
	if x == 1:
		credentials = get_credentials()
		neutron = client.Client(**credentials)
		ports = neutron.list_ports()
		print print_values(ports, 'ports')
	elif x ==2:
		credentials = get_nova_credentials()
		nova_client = nvclient.Client(**credentials)
		server_id = raw_input("Enter server id\n")
		network_id = raw_input("Enter network id\n")
		server_detail = nova_client.servers.get(server_id)
		print server_detail.id
		 
		if server_detail != None:
		    credentials = get_credentials()
		    neutron = client.Client(**credentials)
		    portname = raw_input("Enter name for port\n")
		    body_value = {
				     "port": {
				             "admin_state_up": True,
				             "device_id": server_id,
				             "name": portname,
				             "network_id": network_id
				      }
				 }
		    response = neutron.create_port(body=body_value)
		    print response
	elif x==3:
		router_id = raw_input("Enter router id\n")
		network_id = raw_input("Enter network id\n")
		port_id = raw_input("Enter port id\n")
		try:
			credentials = get_credentials()
			neutron = client.Client(**credentials)
			router = neutron.show_router(router_id)
			print router
    			response = neutron.delete_port(port_id)
    			print response
		finally:
			print "Execution Completed"
	elif x==4:
		arr = []
		n = input("Enter number of ports\n")
		for i in range (0,n):
			print "Enter name for port number ",i+1
			name = raw_input()
			router_id = raw_input("Enter router id\n")
			network_id = raw_input("Enter network id\n")
			sett = 	{
					"name": name,
					"admin_state_up": False,
					"device_id": router_id,
					"network_id": network_id
				}
			arr.append(sett)
		try:
		    credentials = get_credentials()
		    neutron = client.Client(**credentials)
		    router = neutron.show_router(router_id)
		    print router
		    body_value = {
			"ports": arr
		    }
		    response = neutron.create_port(body=body_value)
		    print response
		finally:
		    print "Execution Completed"
	elif x==5:
		router_id = raw_input("Enter router id\n")
		network_id = raw_input("Enter network id\n")
		port_id  = raw_input("Enter port id\n")
		name = raw_input("Enter name of port to be changed\n")
		try:
		    credentials = get_credentials()
		    neutron = client.Client(**credentials)
		    router = neutron.show_router(router_id)
		    print router
		    body_value = {
			"port": {
			"name": name
			}
		    }
		    response = neutron.update_port(port_id, body=body_value)
		    print response
		finally:
		    print "Execution Completed"
	else:
		print "Select Correct option"
	x=input("1.List port\n2.Create port\n3.Delete port\n4.Multiple ports\n5.Update port\n6.Exit\nSelect the option\n")
