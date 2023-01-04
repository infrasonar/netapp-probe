# nieuwe typenaam
('CheckAggregates', 'cAggregates') -> 'aggregate'
('CheckCf', 'cF') -> 'cf'
('CheckCifs', 'cCifs') -> 'cifs'
('CheckClusterNode', 'cClusterNode') -> 'cluster_node'
('CheckFCP', 'cFcp') -> 'tcp'
('CheckLuns', 'cLun') -> 'lun'
('CheckPingCluster', 'cPing') -> 'ping'
('CheckQTree', 'CqTree') -> 'qtree'
('CheckSnapMirror', 'cSnapmirror') -> 'snapmirror'
('CheckSnapshot', 'cSnapshot') -> 'snapshot'
('CheckStorageDisk', 'cStoragedisk') -> 'disk'
('CheckSystemNodeInfo', 'cSystemNode') -> 'system_node'
('CheckVServer', 'cVserver') -> 'vserver'
('CheckVolumes', 'cVolumes') -> 'volume'
('CheckOntapApiVersion', 'ontapapi') -> 'apiversion'
('CheckInterfacePorts', 'netport') -> 'port'

# ontbrekende metrics
('CheckQTree', 'CqTree', 'qtree')  atlijd none?
('CheckSystemPerf', 'system', 'process_name')
('CheckSystemPerf', 'system', 'node_name')
('CheckSystemVersion', 'system', 'version-tuple')  niet meer, losse metrics
('CheckUptime', 'uptime', 'uptime_diff')  niet meer diffen in probe?
('CheckInterface', 'interface', 'data-protocols-data-protocol')  ?
('CheckVServer', 'cVserver', 'name-server-switch-nsswitch')  ?
('CheckVServer', 'cVserver', 'name-mapping-switch-nmswitch') ?
('CheckAggregates')  nested dingen
('CheckStorageDisk')  nested dingen