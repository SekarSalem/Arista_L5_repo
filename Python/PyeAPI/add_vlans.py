import yaml
import pyeapi


file = open('vlans.yml', 'r')

pyeapi.load_config('eapi.conf')
vlan_dict = yaml.safe_load(file)
print(vlan_dict)
for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    print(vlan_api)
    for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)

    # Retrieve VLAN information
    vlan_info = vlan_api.get(vlan_id)
    print(vlan_info)