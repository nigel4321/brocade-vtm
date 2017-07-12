"""
API interface for the Brocade Traffic Manager
"""

import base64
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class VTM(object):
    """
    A python interface to the Brocade VTM devices api
    """

    def __init__(self, host, user, password, port='9070', version='3.4', sslverify=False):
        """
        Create an instance by passing at least the host in the form 'https://name' with
        the username and password for authentication
        """
        self.host = host + ':' + port + '/api/tm/' + version
        self.version = version
        self.sslverify = sslverify
        if not self.sslverify:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        credentials = base64.b64encode("%s:%s" % (user, password))
        self.headers = {'Authorization': 'Basic %s' % credentials,
                        'Content-Type': 'application/json'
                        }

    class vtmException(Exception):
        """
        Raised on error conditions when interacting with the brocade device
        This could be an outright failure or non-200 response from the API
        """
        def __init__(self, errno, message):
            self.message = "%s %s" % (errno, message)
            Exception.__init__(self, self.message)

    def get_api_versions(self):
        """
        Returns a list of available api versions
        """
        host = self.host.split('/')
        del host[len(host) - 1]
        host = '/'.join(host)
        r = requests.get(host, headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def status(self):
        """
        Returns the active VTM nodes
        """
        r = requests.get('%s/status' % self.host, headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        allservers = []
        data = json.loads(r.text)
        for server in data['children']:
            if 'name' in server:
                allservers.append(server['name'])
        return allservers

    def server_stats(self, server):
        """
        Returns the names of the items for which statistics are available
        """
        r = requests.get("%s/status/%s/statistics" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def get_pools(self, server):
        """
        Returns a list of pools for a given VTM node
        """
        r = requests.get("%s/status/%s/statistics/pools" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def get_pool_stats(self, server, pool):
        """
        Returns statistics as a hash keyed by metric name for a given pool on a VTM node
        """
        r = requests.get("%s/status/%s/statistics/pools/%s" % (self.host, server, pool),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code == 200:
            return json.loads(r.text)['statistics']
        else:
            raise self.vtmException(r.status_code, r.text)

    def get_virtual_servers(self, server):
        """
        Returns a list of virtual servers for a given VTM node
        """
        r = requests.get("%s/status/%s/statistics/virtual_servers" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def get_virtual_server_stats(self, server, vserver):
        """
        Returns statistics as a hash keyed by metric name for a given virtual server on a VTM node
        """
        r = requests.get("%s/status/%s/statistics/virtual_servers/%s" %
                         (self.host, server, vserver),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code == 200:
            return json.loads(r.text)['statistics']
        else:
            raise self.vtmException(r.status_code, r.text)

    def get_perpool_nodes(self, server):
        """
        Returns a list of per pool nodes
        """
        r = requests.get("%s/status/%s/statistics/nodes/per_pool_node" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def get_nodes(self, server):
        """
        Returns a list of  nodes
        """
        r = requests.get("%s/status/%s/statistics/nodes/node" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def get_node_stats(self, server, node):
        """
        Returns statistics as a hash keyed by metric name for a given server node  on a VTM node
        """
        r = requests.get("%s/status/%s/statistics/nodes/node/%s" % (self.host, server, node),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code == 200:
            return json.loads(r.text)['statistics']
        else:
            raise self.vtmException(r.status_code, r.text)

    def get_glb_services(self, server):
        """
        Returns a list of glb services
        """
        r = requests.get("%s/status/%s/statistics/glb_services" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def get_glb_service_stats(self, server, glbservice):
        """
        Returns statistics as a hash keyed by metric name for a given glb service
        """
        r = requests.get("%s/status/%s/statistics/glb_services/%s" %
                         (self.host, server, glbservice),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code == 200:
            return json.loads(r.text)['statistics']
        else:
            raise self.vtmException(r.status_code, r.text)

    def get_net_interfaces(self, server):
        """
        Returns a list of network interfaces
        """
        r = requests.get("%s/status/%s/statistics/network_interface" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code != 200:
            raise self.vtmException(r.status_code, r.text)
        data = json.loads(r.text)
        allitems = []
        for item in data['children']:
            if 'name' in item:
                allitems.append(item['name'])
        return allitems

    def get_net_interface_stats(self, server, interface):
        """
        Returns statistics as a hash keyed by metric name for a given glb service
        """
        r = requests.get("%s/status/%s/statistics/network_interface/%s" %
                         (self.host, server, interface),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code == 200:
            return json.loads(r.text)['statistics']
        else:
            raise self.vtmException(r.status_code, r.text)

    def get_global_stats(self, server):
        """
        Return global statistics for a VTM node
        """
        r = requests.get("%s/status/%s/statistics/globals" % (self.host, server),
                         headers=self.headers, verify=self.sslverify)
        if r.status_code == 200:
            return json.loads(r.text)['statistics']
        else:
            raise self.vtmException(r.status_code, r.text)


if __name__ == "__main__":
    help(__name__)
