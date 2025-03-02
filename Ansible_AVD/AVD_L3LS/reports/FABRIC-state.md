
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 321 | 254 | 67 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| leaf1 |  57 | 51 | 6 | LLDP Topology, IP Reachability, BGP, Routing Table, Loopback0 Reachability |
| leaf2 |  57 | 49 | 8 | LLDP Topology, IP Reachability, BGP, Routing Table, Loopback0 Reachability |
| leaf3 |  57 | 47 | 10 | LLDP Topology, IP Reachability, BGP, Routing Table, Loopback0 Reachability |
| leaf4 |  58 | 46 | 12 | LLDP Topology, IP Reachability, BGP, Routing Table, Loopback0 Reachability |
| spine1 |  23 | 17 | 6 | IP Reachability, BGP |
| spine2 |  23 | 17 | 6 | IP Reachability, BGP |
| spine3 |  23 | 17 | 6 | IP Reachability, BGP |
| spine4 |  23 | 10 | 13 | Interface State, IP Reachability, BGP |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  8 | 8 | 0 |
| Interface State |  89 | 88 | 1 |
| LLDP Topology |  40 | 36 | 4 |
| MLAG |  4 | 4 | 0 |
| IP Reachability |  32 | 9 | 23 |
| BGP |  76 | 45 | 31 |
| Routing Table |  40 | 36 | 4 |
| Loopback0 Reachability |  32 | 28 | 4 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 97 | spine4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | FAIL | Interface status: Not configured - line protocol status: Not configured |
| 103 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet3 | FAIL | spine4.arista.lab - Ethernet3 |
| 109 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet4 | FAIL | spine4.arista.lab - Ethernet4 |
| 115 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet5 | FAIL | spine4.arista.lab - Ethernet5 |
| 121 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet6 | FAIL | spine4.arista.lab - Ethernet6 |
| 145 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet6 - Destination: spine4_Ethernet3 | FAIL | 100% packet loss |
| 148 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet5 - Destination: spine3_Ethernet4 | FAIL | 100% packet loss |
| 149 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet6 - Destination: spine4_Ethernet4 | FAIL | 100% packet loss |
| 151 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet4 - Destination: spine2_Ethernet5 | FAIL | 100% packet loss |
| 152 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet5 - Destination: spine3_Ethernet5 | FAIL | 100% packet loss |
| 153 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet6 - Destination: spine4_Ethernet5 | FAIL | 100% packet loss |
| 154 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet3 - Destination: spine1_Ethernet6 | FAIL | 100% packet loss |
| 155 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet4 - Destination: spine2_Ethernet6 | FAIL | 100% packet loss |
| 156 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet5 - Destination: spine3_Ethernet6 | FAIL | 100% packet loss |
| 157 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet6 - Destination: spine4_Ethernet6 | FAIL | 100% packet loss |
| 159 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet4 - Destination: leaf2_Ethernet3 | FAIL | 100% packet loss |
| 160 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet5 - Destination: leaf3_Ethernet3 | FAIL | 100% packet loss |
| 161 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet6 - Destination: leaf4_Ethernet3 | FAIL | 100% packet loss |
| 163 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet4 - Destination: leaf2_Ethernet4 | FAIL | 100% packet loss |
| 164 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet5 - Destination: leaf3_Ethernet4 | FAIL | 100% packet loss |
| 165 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet6 - Destination: leaf4_Ethernet4 | FAIL | 100% packet loss |
| 167 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet4 - Destination: leaf2_Ethernet5 | FAIL | 100% packet loss |
| 168 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet5 - Destination: leaf3_Ethernet5 | FAIL | 100% packet loss |
| 169 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet6 - Destination: leaf4_Ethernet5 | FAIL | 100% packet loss |
| 170 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet3 - Destination: leaf1_Ethernet6 | FAIL | 100% packet loss |
| 171 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet4 - Destination: leaf2_Ethernet6 | FAIL | 100% packet loss |
| 172 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet5 - Destination: leaf3_Ethernet6 | FAIL | 100% packet loss |
| 173 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet6 - Destination: leaf4_Ethernet6 | FAIL | 100% packet loss |
| 186 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.6 | FAIL | Session state Not configured |
| 190 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.12 | FAIL | Session state Not configured |
| 191 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.14 | FAIL | Session state Not configured |
| 194 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.18 | FAIL | Session state Not configured |
| 195 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.20 | FAIL | Session state Not configured |
| 196 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.22 | FAIL | Session state Not configured |
| 198 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.24 | FAIL | Session state Not configured |
| 199 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.26 | FAIL | Session state Not configured |
| 200 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.28 | FAIL | Session state Not configured |
| 201 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.30 | FAIL | Session state Not configured |
| 203 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.9 | FAIL | Session state Not configured |
| 204 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.17 | FAIL | Session state Not configured |
| 205 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.25 | FAIL | Session state Not configured |
| 207 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.11 | FAIL | Session state Not configured |
| 208 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.19 | FAIL | Session state Not configured |
| 209 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.27 | FAIL | Session state Not configured |
| 211 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.13 | FAIL | Session state Not configured |
| 212 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.21 | FAIL | Session state Not configured |
| 213 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.29 | FAIL | Session state Not configured |
| 214 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.7 | FAIL | Session state Not configured |
| 215 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.15 | FAIL | Session state Not configured |
| 216 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.23 | FAIL | Session state Not configured |
| 217 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.31 | FAIL | Session state Not configured |
| 221 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 225 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 229 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 233 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 246 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | FAIL | Session state: Not configured |
| 247 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | FAIL | Session state: Not configured |
| 248 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | FAIL | Session state: Not configured |
| 249 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | FAIL | Session state: Not configured |
| 265 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 273 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 281 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 289 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 297 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.14 | FAIL | 100% packet loss |
| 305 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.14 | FAIL | 100% packet loss |
| 313 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.14 | FAIL | 100% packet loss |
| 321 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.14 | FAIL | 100% packet loss |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 2 | leaf2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 3 | leaf3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 4 | leaf4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 5 | spine1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 6 | spine2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 7 | spine3 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 8 | spine4 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 9 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf2_Ethernet1 | PASS | - |
| 10 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf2_Ethernet2 | PASS | - |
| 11 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet3 | PASS | - |
| 12 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet3 | PASS | - |
| 13 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet3 | PASS | - |
| 14 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet3 | PASS | - |
| 15 | leaf1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1_Ethernet1 | PASS | - |
| 16 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf1_Ethernet1 | PASS | - |
| 17 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf1_Ethernet2 | PASS | - |
| 18 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet4 | PASS | - |
| 19 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet4 | PASS | - |
| 20 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet4 | PASS | - |
| 21 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet4 | PASS | - |
| 22 | leaf2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1_Ethernet2 | PASS | - |
| 23 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf4_Ethernet1 | PASS | - |
| 24 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf4_Ethernet2 | PASS | - |
| 25 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet5 | PASS | - |
| 26 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet5 | PASS | - |
| 27 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet5 | PASS | - |
| 28 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet5 | PASS | - |
| 29 | leaf3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host2_Ethernet1 | PASS | - |
| 30 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf3_Ethernet1 | PASS | - |
| 31 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf3_Ethernet2 | PASS | - |
| 32 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1_Ethernet6 | PASS | - |
| 33 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2_Ethernet6 | PASS | - |
| 34 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3_Ethernet6 | PASS | - |
| 35 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_SPINE4_Ethernet6 | PASS | - |
| 36 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet9 -  | PASS | - |
| 37 | leaf4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host2_Ethernet2 | PASS | - |
| 38 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet3 | PASS | - |
| 39 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet3 | PASS | - |
| 40 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet3 | PASS | - |
| 41 | spine1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet3 | PASS | - |
| 42 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet4 | PASS | - |
| 43 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet4 | PASS | - |
| 44 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet4 | PASS | - |
| 45 | spine2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet4 | PASS | - |
| 46 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet5 | PASS | - |
| 47 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet5 | PASS | - |
| 48 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet5 | PASS | - |
| 49 | spine3 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet5 | PASS | - |
| 50 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF1_Ethernet6 | PASS | - |
| 51 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF2_Ethernet6 | PASS | - |
| 52 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF3_Ethernet6 | PASS | - |
| 53 | spine4 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_LEAF4_Ethernet6 | PASS | - |
| 54 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf2_Po1 | PASS | - |
| 55 | leaf1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1_PortChannel host1 | PASS | - |
| 56 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf1_Po1 | PASS | - |
| 57 | leaf2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host1_PortChannel host1 | PASS | - |
| 58 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf4_Po1 | PASS | - |
| 59 | leaf3 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host2_PortChannel host2 | PASS | - |
| 60 | leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf3_Po1 | PASS | - |
| 61 | leaf4 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel7 - host2_PortChannel host2 | PASS | - |
| 62 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 63 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 64 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 65 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 66 | leaf1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 67 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 68 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 69 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 70 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 71 | leaf2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 72 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 73 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 74 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 75 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 76 | leaf3 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 77 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 78 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 79 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 80 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 81 | leaf4 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 82 | leaf1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 83 | leaf2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 84 | leaf3 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 85 | leaf4 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 86 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 87 | leaf1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 88 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 89 | leaf2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 90 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 91 | leaf3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 92 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 93 | leaf4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 94 | spine1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 95 | spine2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 96 | spine3 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 97 | spine4 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | FAIL | Interface status: Not configured - line protocol status: Not configured |
| 98 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf2_Ethernet1 | PASS | - |
| 99 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf2_Ethernet2 | PASS | - |
| 100 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet3 | PASS | - |
| 101 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet3 | PASS | - |
| 102 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet3 | PASS | - |
| 103 | leaf1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet3 | FAIL | spine4.arista.lab - Ethernet3 |
| 104 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf1_Ethernet1 | PASS | - |
| 105 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1_Ethernet2 | PASS | - |
| 106 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet4 | PASS | - |
| 107 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet4 | PASS | - |
| 108 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet4 | PASS | - |
| 109 | leaf2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet4 | FAIL | spine4.arista.lab - Ethernet4 |
| 110 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf4_Ethernet1 | PASS | - |
| 111 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf4_Ethernet2 | PASS | - |
| 112 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet5 | PASS | - |
| 113 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet5 | PASS | - |
| 114 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet5 | PASS | - |
| 115 | leaf3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet5 | FAIL | spine4.arista.lab - Ethernet5 |
| 116 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf3_Ethernet1 | PASS | - |
| 117 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf3_Ethernet2 | PASS | - |
| 118 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1_Ethernet6 | PASS | - |
| 119 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2_Ethernet6 | PASS | - |
| 120 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3_Ethernet6 | PASS | - |
| 121 | leaf4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: spine4_Ethernet6 | FAIL | spine4.arista.lab - Ethernet6 |
| 122 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet3 | PASS | - |
| 123 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet3 | PASS | - |
| 124 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet3 | PASS | - |
| 125 | spine1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet3 | PASS | - |
| 126 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet4 | PASS | - |
| 127 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet4 | PASS | - |
| 128 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet4 | PASS | - |
| 129 | spine2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet4 | PASS | - |
| 130 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet5 | PASS | - |
| 131 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet5 | PASS | - |
| 132 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet5 | PASS | - |
| 133 | spine3 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet5 | PASS | - |
| 134 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf1_Ethernet6 | PASS | - |
| 135 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf2_Ethernet6 | PASS | - |
| 136 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf3_Ethernet6 | PASS | - |
| 137 | spine4 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf4_Ethernet6 | PASS | - |
| 138 | leaf1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 139 | leaf2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 140 | leaf3 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 141 | leaf4 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 142 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet3 - Destination: spine1_Ethernet3 | PASS | - |
| 143 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet4 - Destination: spine2_Ethernet3 | PASS | - |
| 144 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet5 - Destination: spine3_Ethernet3 | PASS | - |
| 145 | leaf1 | IP Reachability | ip reachability test p2p links | Source: leaf1_Ethernet6 - Destination: spine4_Ethernet3 | FAIL | 100% packet loss |
| 146 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet3 - Destination: spine1_Ethernet4 | PASS | - |
| 147 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet4 - Destination: spine2_Ethernet4 | PASS | - |
| 148 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet5 - Destination: spine3_Ethernet4 | FAIL | 100% packet loss |
| 149 | leaf2 | IP Reachability | ip reachability test p2p links | Source: leaf2_Ethernet6 - Destination: spine4_Ethernet4 | FAIL | 100% packet loss |
| 150 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet3 - Destination: spine1_Ethernet5 | PASS | - |
| 151 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet4 - Destination: spine2_Ethernet5 | FAIL | 100% packet loss |
| 152 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet5 - Destination: spine3_Ethernet5 | FAIL | 100% packet loss |
| 153 | leaf3 | IP Reachability | ip reachability test p2p links | Source: leaf3_Ethernet6 - Destination: spine4_Ethernet5 | FAIL | 100% packet loss |
| 154 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet3 - Destination: spine1_Ethernet6 | FAIL | 100% packet loss |
| 155 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet4 - Destination: spine2_Ethernet6 | FAIL | 100% packet loss |
| 156 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet5 - Destination: spine3_Ethernet6 | FAIL | 100% packet loss |
| 157 | leaf4 | IP Reachability | ip reachability test p2p links | Source: leaf4_Ethernet6 - Destination: spine4_Ethernet6 | FAIL | 100% packet loss |
| 158 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet3 - Destination: leaf1_Ethernet3 | PASS | - |
| 159 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet4 - Destination: leaf2_Ethernet3 | FAIL | 100% packet loss |
| 160 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet5 - Destination: leaf3_Ethernet3 | FAIL | 100% packet loss |
| 161 | spine1 | IP Reachability | ip reachability test p2p links | Source: spine1_Ethernet6 - Destination: leaf4_Ethernet3 | FAIL | 100% packet loss |
| 162 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet3 - Destination: leaf1_Ethernet4 | PASS | - |
| 163 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet4 - Destination: leaf2_Ethernet4 | FAIL | 100% packet loss |
| 164 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet5 - Destination: leaf3_Ethernet4 | FAIL | 100% packet loss |
| 165 | spine2 | IP Reachability | ip reachability test p2p links | Source: spine2_Ethernet6 - Destination: leaf4_Ethernet4 | FAIL | 100% packet loss |
| 166 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet3 - Destination: leaf1_Ethernet5 | PASS | - |
| 167 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet4 - Destination: leaf2_Ethernet5 | FAIL | 100% packet loss |
| 168 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet5 - Destination: leaf3_Ethernet5 | FAIL | 100% packet loss |
| 169 | spine3 | IP Reachability | ip reachability test p2p links | Source: spine3_Ethernet6 - Destination: leaf4_Ethernet5 | FAIL | 100% packet loss |
| 170 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet3 - Destination: leaf1_Ethernet6 | FAIL | 100% packet loss |
| 171 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet4 - Destination: leaf2_Ethernet6 | FAIL | 100% packet loss |
| 172 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet5 - Destination: leaf3_Ethernet6 | FAIL | 100% packet loss |
| 173 | spine4 | IP Reachability | ip reachability test p2p links | Source: spine4_Ethernet6 - Destination: leaf4_Ethernet6 | FAIL | 100% packet loss |
| 174 | leaf1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 175 | leaf2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 176 | leaf3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 177 | leaf4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 178 | spine1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 179 | spine2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 180 | spine3 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 181 | spine4 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 182 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.1 | PASS | - |
| 183 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.0 | PASS | - |
| 184 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.2 | PASS | - |
| 185 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.4 | PASS | - |
| 186 | leaf1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.6 | FAIL | Session state Not configured |
| 187 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.0 | PASS | - |
| 188 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.8 | PASS | - |
| 189 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.10 | PASS | - |
| 190 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.12 | FAIL | Session state Not configured |
| 191 | leaf2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.14 | FAIL | Session state Not configured |
| 192 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.5 | PASS | - |
| 193 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.16 | PASS | - |
| 194 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.18 | FAIL | Session state Not configured |
| 195 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.20 | FAIL | Session state Not configured |
| 196 | leaf3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.22 | FAIL | Session state Not configured |
| 197 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.4 | PASS | - |
| 198 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.24 | FAIL | Session state Not configured |
| 199 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.26 | FAIL | Session state Not configured |
| 200 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.28 | FAIL | Session state Not configured |
| 201 | leaf4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.30 | FAIL | Session state Not configured |
| 202 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.1 | PASS | - |
| 203 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.9 | FAIL | Session state Not configured |
| 204 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.17 | FAIL | Session state Not configured |
| 205 | spine1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.25 | FAIL | Session state Not configured |
| 206 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.3 | PASS | - |
| 207 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.11 | FAIL | Session state Not configured |
| 208 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.19 | FAIL | Session state Not configured |
| 209 | spine2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.27 | FAIL | Session state Not configured |
| 210 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.5 | PASS | - |
| 211 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.13 | FAIL | Session state Not configured |
| 212 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.21 | FAIL | Session state Not configured |
| 213 | spine3 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.29 | FAIL | Session state Not configured |
| 214 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.7 | FAIL | Session state Not configured |
| 215 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.15 | FAIL | Session state Not configured |
| 216 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.23 | FAIL | Session state Not configured |
| 217 | spine4 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 192.168.103.31 | FAIL | Session state Not configured |
| 218 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 219 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 220 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 221 | leaf1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 222 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 223 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 224 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 225 | leaf2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 226 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 227 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 228 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 229 | leaf3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 230 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 231 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 232 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 233 | leaf4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.14 | FAIL | Session state: Not configured |
| 234 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 235 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 236 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 237 | spine1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 238 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 239 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 240 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 241 | spine2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 242 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 243 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 244 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 245 | spine3 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 246 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | FAIL | Session state: Not configured |
| 247 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | FAIL | Session state: Not configured |
| 248 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | FAIL | Session state: Not configured |
| 249 | spine4 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | FAIL | Session state: Not configured |
| 250 | leaf1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 251 | leaf1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 252 | leaf2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 253 | leaf2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 254 | leaf3 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 255 | leaf3 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 256 | leaf4 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 257 | leaf4 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 258 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 259 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 260 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 261 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 262 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 263 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 264 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 265 | leaf1 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 266 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 267 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 268 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 269 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 270 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 271 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 272 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 273 | leaf2 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 274 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 275 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 276 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 277 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 278 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 279 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 280 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 281 | leaf3 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 282 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 283 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 284 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 285 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 286 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 287 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 288 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 289 | leaf4 | Routing Table | Remote Lo0 address | 192.168.101.14 | FAIL | Lo0 192.168.101.14 is not in the routing table |
| 290 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.1 | PASS | - |
| 291 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.2 | PASS | - |
| 292 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.3 | PASS | - |
| 293 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.4 | PASS | - |
| 294 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.11 | PASS | - |
| 295 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.12 | PASS | - |
| 296 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.13 | PASS | - |
| 297 | leaf1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1 - 192.168.101.1 Destination: 192.168.101.14 | FAIL | 100% packet loss |
| 298 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.1 | PASS | - |
| 299 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.2 | PASS | - |
| 300 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.3 | PASS | - |
| 301 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.4 | PASS | - |
| 302 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.11 | PASS | - |
| 303 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.12 | PASS | - |
| 304 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.13 | PASS | - |
| 305 | leaf2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2 - 192.168.101.2 Destination: 192.168.101.14 | FAIL | 100% packet loss |
| 306 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.1 | PASS | - |
| 307 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.2 | PASS | - |
| 308 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.3 | PASS | - |
| 309 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.4 | PASS | - |
| 310 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.11 | PASS | - |
| 311 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.12 | PASS | - |
| 312 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.13 | PASS | - |
| 313 | leaf3 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3 - 192.168.101.3 Destination: 192.168.101.14 | FAIL | 100% packet loss |
| 314 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.1 | PASS | - |
| 315 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.2 | PASS | - |
| 316 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.3 | PASS | - |
| 317 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.4 | PASS | - |
| 318 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.11 | PASS | - |
| 319 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.12 | PASS | - |
| 320 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.13 | PASS | - |
| 321 | leaf4 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4 - 192.168.101.4 Destination: 192.168.101.14 | FAIL | 100% packet loss |
