Help on built-in module __main__:

NAME
    __main__ - API interface for the Brocade Traffic Manager

FILE
    /Users/nsa20/git/bskyb/steelapp_stats_collectd/brocadevtm.py

CLASSES
    __builtin__.object
        VTM
    
    class VTM(__builtin__.object)
     |  A python interface to the Brocade VTM devices api
     |  
     |  Methods defined here:
     |  
     |  __init__(self, host, user, password, port='9070', version='3.4', sslverify=False)
     |      Create an instance by passing at least the host in the form 'https://name' with
     |      the username and password for authentication
     |  
     |  get_api_versions(self)
     |      Returns a list of available api versions
     |  
     |  get_glb_service_stats(self, server, glbservice)
     |      Returns statistics as a hash keyed by metric name for a given glb service
     |  
     |  get_glb_services(self, server)
     |      Returns a list of glb services
     |  
     |  get_global_stats(self, server)
     |      Return global statistics for a VTM node
     |  
     |  get_net_interface_stats(self, server, interface)
     |      Returns statistics as a hash keyed by metric name for a given glb service
     |  
     |  get_net_interfaces(self, server)
     |      Returns a list of network interfaces
     |  
     |  get_node_stats(self, server, node)
     |      Returns statistics as a hash keyed by metric name for a given server node  on a VTM node
     |  
     |  get_nodes(self, server)
     |      Returns a list of  nodes
     |  
     |  get_perpool_nodes(self, server)
     |      Returns a list of per pool nodes
     |  
     |  get_pool_stats(self, server, pool)
     |      Returns statistics as a hash keyed by metric name for a given pool on a VTM node
     |  
     |  get_pools(self, server)
     |      Returns a list of pools for a given VTM node
     |  
     |  get_virtual_server_stats(self, server, vserver)
     |      Returns statistics as a hash keyed by metric name for a given virtual server on a VTM node
     |  
     |  get_virtual_servers(self, server)
     |      Returns a list of virtual servers for a given VTM node
     |  
     |  server_stats(self, server)
     |      Returns the names of the items for which statistics are available
     |  
     |  status(self)
     |      Returns the active VTM nodes
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  vtmException = <class '__main__.vtmException'>
     |      Raised on error conditions when interacting with the brocade device
     |      This could be an outright failure or non-200 response from the API


