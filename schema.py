from math import fabs
import graphene
import extraction
from graphene.types.scalars import String
from graphene.types.structures import List
import requests
from src.run_Recommend import Run, Product

def extract(url):
    html = requests.get(url).text
    extracted = extraction.Extractor().extract(html, source_url=url)
    print(extracted)
    return extracted

class Website(graphene.ObjectType):
    url = graphene.String(required=True)
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()
    feed = graphene.String()
 

class Recommendd(graphene.ObjectType):
    demand = graphene.String(required=True); 
    price = graphene.String(required=True);
    area = graphene.String();
    location = graphene.String(required=True);
    no_bedroom = graphene.String();
    no_wc = graphene.String();
    furniture = graphene.String();
    juridical = graphene.String()
    view = graphene.String()
    floor = graphene.String()
    hot = graphene.String()
    name_flat = graphene.String()
 
class Query(graphene.ObjectType):
    website = graphene.Field(Website, url=graphene.String())
    recommend = graphene.List(Recommendd, demand=graphene.String(),price=graphene.String(),area=graphene.String(),location = graphene.String(), no_bedroom = graphene.String(),no_wc = graphene.String(),furniture = graphene.String(),juridical = graphene.String(),view = graphene.String(),floor = graphene.String(),hot = graphene.String(),name_flat = graphene.String())
   

    def resolve_recommend(self,info,  demand='None', price='None', area='None', location='None', no_bedroom='None', no_WC='None', furniture='None', juridical='None', view='None', floor='None', hot='False'):  
        request_input = [demand, price, area, location, no_bedroom, no_WC, furniture, juridical, view, floor, hot]
        v = Run(request_input)
        h = Product(v)  
        Recommends =[]
        for item in h:
            Recommends.append(Recommendd(demand=item.price,price=item.price,area=item.area,location = item.location,no_bedroom = item.no_bedroom,no_wc = item.no_wc,furniture = item.furniture,juridical = item.juridical,view = item.view,floor = item.floor,hot = item.hot,name_flat = item.name_flat)) 
    
        return Recommends

    def resolve_website(self, info, url):
        extracted = extract(url)
        print(url)
        return Website(url=url,
                       title=extracted.title,
                       description=extracted.description,
                       image=extracted.image,
                       feed=extracted.feed
        )

schema = graphene.Schema(query=Query)