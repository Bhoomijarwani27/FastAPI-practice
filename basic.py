from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body
app = FastAPI() # create fastapi appilcation it instant 
@app.get("/") # decorator  , use when someone send  get request  to , run the function below 
async def home(): # function that handle request effciently(non-blocking)
     return {"message": "hello world"}  # return dictionary fastapi automatically convert it to json 
 # another way  
   # return  "Hello world"  

# differnt endpoint  at end /about to get this after 8000/about 
@app.get("/about")
def about():
     return "about page"
# path paremeter 
@app.get('/blog/unpublished')
def unpublished():
     return {'data': 'all unpublished blogs'}
@app.get('/blog/check')

def check(limit:int,published:bool):
     # to get published or all 
     if published:
        return {'data':f'{limit} published blog list from db '}
     else:
          return {'data':f'{limit} blog list from db '}
# add data in url 
# like http://127.0.0.1:8000/blog/3   in this 3 is data we get data:3
@app.get('/blog/{id}')
def show(id:int): # default is string but to get for id need int 
     #fetch blog with id = id
     return {'data': id}
@app.get('/blog/{id}/comments')
def comments(id):
     #fetch comments of blog with id = id
     return {'data':{'1','2','3'}}
# quriey parermeter 
@app.get('/blog?limit=10published=true')
def index():
     # only get 10 published blogs 
     return {'data':'blog list'}
@app.get('/blog')
# add parameter to make flexiable like id 
def index(limit):
     return {'data':f'{limit} blog list from db '}

# post method 
@app.post('/requestbody') # it not view from url it can be on docs and redocs
def request_body():
     return {'data': 'blog created'}
class rule(BaseModel):
     title:str
     body:str
     published:Optional[bool] 
@app.post('/rule')
def rule(request:rule):
      return {'data': "blog created with title as{request.title}"}
@app.post("/createpost")
def create_post(payload:dict = Body(...)):
     print(payload)
     return {"new post":f"title: {payload['title']}  content : {payload['content']}"}
    # return "successfully created posts"
class post_pydantic(BaseModel):
     title : str
     content: str
@app.post("/py_post")
def create_post(new_post: post_pydantic):
     print(new_post)
     return {"new_post":f"title: {new_post.title}  content : {new_post.content}"}
