# brocade-vtm
Library for collecting metrics from the Brocade Traffic Manager (Load Balancer)


```python
server = "h1sta02.ovp.bskyb.com"
vtm = brocadevtm.VTM(host='https://' + server, user=conf['username'],
    password=conf['password'],
    version=conf['api_version'], port=conf['port'])
    
allglobalstats = vtm.get_global_stats(server)
```

### Documentation
[Documentation](brocadevtm.md)
Execute
```shell
python  brocadevtm.py
```
