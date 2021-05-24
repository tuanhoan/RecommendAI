# import __init__

from src.source import Get_request, run_source, Load_dataset

map_path = './dataset/map.json'
dataset_Apartment = './dataset/Apartment.csv'
dataset_Service_floor = './dataset/Service_floor.csv'
cfg_path = './libs/config/basic.json'

# print("Apartmen{0} or Service floor{1}: ")
# service = int(input())

service = 0

# request_input = Get_request()
request_input = ["Bán","2100000000","56.7","Quận 9","3","2","Có","Sổ hồng","Tây Nam","12","False"]
print(request_input, '\n\n')
# if service == 0:
#     run_source(request_input, map_path, dataset_Apartment, cfg_path)
# else:
#     run_source(request_input, map_path, dataset_Service_floor, cfg_path)

def Run():
    if service == 0:
        x = run_source(request_input, map_path, dataset_Apartment, cfg_path)
        return x
    else:
        return run_source(request_input, map_path, dataset_Service_floor, cfg_path)
def Run(need, price):
    request_input[0] = need
    request_input[1] = price
    if service == 0:
        x = run_source(request_input, map_path, dataset_Apartment, cfg_path)
        return x
    else:
        return run_source(request_input, map_path, dataset_Service_floor, cfg_path)




