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
def Run():  
    if service == 0:
        x = run_source(request_input, map_path, dataset_Apartment, cfg_path)
    else:
        x =run_source(request_input, map_path, dataset_Service_floor, cfg_path) 
    return x 

def Run(_request):  
    if service == 0:
        x = run_source(_request, map_path, dataset_Apartment, cfg_path)
    else:
        x =run_source(_request, map_path, dataset_Service_floor, cfg_path) 
    return x 
class Recommender:
    need = ""
    price = 0
    area = 0
    location = 0
    no_bedroom = 0
    no_wc = 0
    furniture = ""
    juridical = ""
    view = ""
    floor =""
    hot = False
    name_flat = ""

 
def Product(x): 
    a = []
    for index in range(len(x)):
        k = Recommender() 
        k.need = x[index]["demand"]
        k.price = x[index]["price"]
        k.view = x[index]["view"]
        k.area = x[index]["area"]
        k.location = x[index]["location"]
        k.no_bedroom = x[index]["no_bedroom"]
        k.no_wc = x[index]["no_WC"]
        k.furniture = x[index]["furniture"]
        k.juridical = x[index]["juridical"]
        k.view = x[index]["view"]
        k.floor = x[index]["floor"]
        k.hot = x[index]["hot"]
        k.name_flat = x[index]["name flat"]
        a.append(k)
    return a
if __name__ == '__main__':
    h = Run(request_input)
    k = Product(h)
    print(k[3].price, k[2].price)
 


