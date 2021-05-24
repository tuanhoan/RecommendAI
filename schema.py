import graphene
import extraction
from graphene.types.scalars import String
import requests
from src.run_Recommend import Run 

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

class Recommend(graphene.ObjectType): 
    result = graphene.List(String)
# class ListRecommend(graphene.ObjectType):
#     results = [Recommend]
    
class Query(graphene.ObjectType):
    website = graphene.Field(Website, url=graphene.String())
    recommend = graphene.Field(Recommend, need=graphene.String(),price=graphene.String())

    def resolve_recommend(self,info, need, price):
        a = "Tuấn Hoàn"
        x = Run(need, price)  
        a = []
        for i in x:
            a.append(str(i).encode("utf-8"))
            print(str(i)) 
        return Recommend(result = a)

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