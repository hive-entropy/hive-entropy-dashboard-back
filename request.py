def get_nodes():
    param_node_list=[
        {
            "id": 0,
            "address": "192.168.1.56",
            "state": 0,
            "arch": "rasp-pi-4",
            "proxy": "192.168.1.99"
        },
        {
            "id": 1,
            "address": "192.168.1.42",
            "state": 0,
            "arch": "rasp-pi-4",
            "proxy": "192.168.1.102"
        },
        {
            "id": 2,
            "address": "192.168.1.49",
            "state": 0,
            "arch": "stm32",
            "proxy": "192.168.1.103"
        },
        {
            "id": 3,
            "address": "192.168.1.27",
            "state": 0,
            "arch": "stm32",
            "proxy": "192.168.1.104"
        },
    ]
    return param_node_list


def get_node_info(nodeid_int):
    info_node_dict = {
        "ID": nodeid_int,
        "processor": {
            "model": "ARM Cortex M3",
            "frequency": {
                "value": 3.55,
                "unit": "GB"
            },
            "occupation": 67.3,
            "cores": 4
        },
        "ram": {
            "capacity": {
                "value": 512,
                "unit": "MB"
            },
            "occupation": 55.2
        },
        "battery": 15.5
    }
    return info_node_dict



def deploy_node(nodeid_int):
    return True, None