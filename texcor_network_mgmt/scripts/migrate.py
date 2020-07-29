import xmlrpc.client as xmlrpclib

mods = {
    'tower_type': 'x_tower_type',
    'qos': 'x_qos',
    'equipment_table': 'x_equipment_table',
    'equipment': 'x_equipment',
    'tower': 'x_towers',
    'pop': 'x_pop',
    'circuit': 'x_circuit_ids',
    'pop_id': 'pop',
    'qos_id': 'qos',
    'ap_name_id': 'equipment',
    'tower_id': 'tower',
    'equipment_id': 'equipment',
    'ip_management_id': 'ip_management'
}

circuit = {
    'id': 'oldid',
    'x_name': 'name',
    'x_studio_circuit_type': 'circuit_type',
    'x_studio_field_6DKAX': 'pop_id',
    'x_studio_customer': 'customer_id',
    'x_studio_service_location': 'location_id',
    'x_studio_customer_id': 'customerId',
    'x_studio_field_HMu1i': 'service_order_id',
    'x_studio_field_NPD3S': 'status',
    'x_studio_field_eqo8o': 'qos_id',
    'x_studio_vlanid': 'vlanid',
    'x_studio_ap_name': 'ap_name_id',
    'x_studio_field_nlcQR': 'pe_switch_id',
    'x_studio_pe_switch_port': 'pe_switch_port',
    'x_studio_field_FgYFj': 'tech_name_id',
    'x_studio_dmarc_location': 'dmarc_location',
    'x_studio_documents': 'documents',
    'x_studio_notes': 'notes',
    'x_studio_sales_person': 'sales_person',
}

equipment = {
    'id': 'oldid',
    'x_name': 'name',
    'x_studio_serial_number': 'serial_number',
    'x_studio_mac_address': 'mac_address',
    'x_studio_firmware_version': 'firmware_version',
    'x_studio_in_service': 'in_service',
    'x_studio_cpe_device': 'cpe_device',
    'x_studio_field_tQkqb': 'number_of_ports',
    'x_studio_model': 'model',
    'x_studio_device_type': 'device_type',
    'x_studio_field_a2987': 'manufacturer',
    'x_studio_field_6CAey': 'ip_management_id',
    'x_studio_field_vitwV': 'pop_id',
    'x_studio_tower': 'tower_id',
    'x_studio_wireless_ssid': 'wireless_ssid',
    'x_studio_wireless_mac': 'wireless_mac',
    'x_studio_access_point_mode': 'module_mode',
}

equipment_table = {
    'id': 'oldid',
    'x_studio_manufacturer_2': 'manufacturer',
    'x_studio_model_1': 'model',
    'x_studio_l3_capable': 'l3_capable',
    'x_studio_type': 'type_name',
    'x_studio_l2_capable': 'l2_capable',
    'x_studio_class_1': 'class_name',
    'x_name': 'name',
}

ip_management = {
    'id': 'oldid',
    'x_name': 'name',

    'x_studio_net_mask': 'net_mask',
    'x_studio_provider_ip': 'provider_ip',
    'x_studio_network_address_1': 'network_address',

    'x_studio_cidr_1': 'cidr',
    'x_studio_availability': 'availability',

    'x_studio_management_ip': 'management_ip',
    'x_studio_parent_network': 'parent_network',
    'x_studio_internal_use': 'internal_use',

    'x_studio_field_nynEv': 'equipment_id',
    'x_studio_field_Ni3e1': 'circuit_id',
    'x_studio_field_Z9kFS': 'location_id',

    'x_studio_description_1': 'description',
}

pop = {
    'id': 'oldid',
    'x_name': 'name',
    'x_studio_hut_number': 'hut_number',
    'x_studio_geo_cooridinates': 'geo_cooridinates',
    'x_studio_pop_type': 'pop_type',
}

qos = {
    'id': 'oldid',
    'x_name': 'name'
}

tower_type = {
    'id': 'oldid',
    'x_name': 'name'
}

tower = {
    'id': 'oldid',
    'x_name': 'name',

    'x_studio_field_tjLbn': 'tower_type_id',
    'x_studio_field_kWVR2': 'pop_id',
    'x_studio_geo_location': 'geo_location',
    'x_studio_tower_height_in_ft': 'tower_height',

    'x_studio_field_mkCNY': 'array_type',
    'x_studio_wireless_frequency': 'wireless_frequency',
    'x_studio_array_height_in_ft': 'array_height',

    'x_studio_ap_name': 'ap_name_id',
    'x_studio_field_nje8n': 'circuit_ids',

    'x_studio_sector_1': 'sector_1',
    'x_studio_h_azimuth': 'h_azimuth_1',
    'x_studio_v_azimuth': 'v_azimuth_1',

    'x_studio_sector_2': 'sector_2',
    'x_studio_h_azimuth_1': 'h_azimuth_2',
    'x_studio_v_azimuth_1': 'v_azimuth_2',


    'x_studio_sector_3': 'sector_3',
    'x_studio_h_azimuth_2': 'h_azimuth_3',
    'x_studio_v_azimuth_2': 'v_azimuth_3',


    'x_studio_sector_4': 'sector_4',
    'x_studio_h_azimuth_3': 'h_azimuth_4',
    'x_studio_v_azimuth_3': 'v_azimuth_4',
}

url = 'http://localhost:8069'
db = 'texcor'
username = 'admin'
password = 'admin'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
print('User authentication success!')

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

# table = models.execute_kw(db, uid, password, 'x_equipment', 'search_read', [[]])
# to_map = equipment

# to_create = []
# for t in table:
#     obj = {}
#     for k in to_map:
#         if '_id' in k:
#             continue
#         key = to_map[k]
#         obj[key] = t[k]
#     to_create.append(obj)

# equipments = models.execute_kw(db, uid, password, 'equipment', 'create', [to_create])

table = models.execute_kw(db, uid, password, 'x_equipment_table', 'search_read', [[]])
to_map = equipment_table

to_create = []
for t in table:
    obj = {}
    for k in to_map:
        if '_id' in k:
            continue
        key = to_map[k]
        obj[key] = t[k]
    to_create.append(obj)

equipment_tables = models.execute_kw(db, uid, password, 'equipment_table', 'create', [to_create])

table = models.execute_kw(db, uid, password, 'x_pop', 'search_read', [[]])
to_map = pop

to_create = []
for t in table:
    obj = {}
    for k in to_map:
        if '_id' in k:
            continue
        key = to_map[k]
        obj[key] = t[k]
    to_create.append(obj)

pops = models.execute_kw(db, uid, password, 'pop', 'create', [to_create])

table = models.execute_kw(db, uid, password, 'x_tower_type', 'search_read', [[]])
to_map = tower_type

to_create = []
for t in table:
    obj = {}
    for k in to_map:
        if '_id' in k:
            continue
        key = to_map[k]
        obj[key] = t[k]
    to_create.append(obj)

tower_types = models.execute_kw(db, uid, password, 'tower_type', 'create', [to_create])

table = models.execute_kw(db, uid, password, 'x_towers', 'search_read', [[]])
to_map = tower

to_create = []
for t in table:
    obj = {}
    for k in to_map:
        if '_id' in k:
            continue
        key = to_map[k]
        obj[key] = t[k]
    to_create.append(obj)

towers = models.execute_kw(db, uid, password, 'tower', 'create', [to_create])

table = models.execute_kw(db, uid, password, 'x_circuit_ids', 'search_read', [[]])
to_map = circuit

to_create = []
for t in table:
    obj = {}
    for k in to_map:
        if '_id' in k:
            continue
        key = to_map[k]
        obj[key] = t[k]
    to_create.append(obj)

circuits = models.execute_kw(db, uid, password, 'circuit', 'create', [to_create])

table = models.execute_kw(db, uid, password, 'x_ip_management', 'search_read', [[]])
to_map = ip_management

to_create = []
for t in table:
    obj = {}
    for k in to_map:
        if '_id' in k:
            continue
        key = to_map[k]
        obj[key] = t[k]
    to_create.append(obj)

ip_managements = models.execute_kw(db, uid, password, 'ip_management', 'create', [to_create])

table = models.execute_kw(db, uid, password, 'x_qos', 'search_read', [[]])
to_map = qos

to_create = []
for t in table:
    obj = {}
    for k in to_map:
        if '_id' in k:
            continue
        key = to_map[k]
        obj[key] = t[k]
    to_create.append(obj)

qoss = models.execute_kw(db, uid, password, 'qos', 'create', [to_create])
