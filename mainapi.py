from fastapi import FastAPI,Request, status
from sqlalchemy.orm import Session,column_property
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Response,status,HTTPException,Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy import func
from sqlalchemy.sql import text
import sqlalchemy as bb
from mangum import Mangum

from datetime import datetime, timedelta
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme= OAuth2PasswordBearer(tokenUrl='login')
from sqlalchemy.orm import Session
# from passlib.context import CryptContext
# from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import psycopg2.extras 
from psycopg2.extras  import RealDictCursor
import time
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, DATE
from sqlalchemy.sql.expression import text
from sqlalchemy import func
from sqlalchemy.orm import column_property
from pydantic import BaseModel,EmailStr

from datetime import date,datetime
from typing import Optional

# from pydantic.types import conint
# from passlib.hash import pbkdf2_sha256





# #TO CHECK ALL THE ENVIRONMENT VARIABLES ARE THERE
# class Settings(BaseSettings):#checks local environment variablea (IN THE HOST)to see if the following variables are there
#    database_hostname:str
#    database_port:str
#    database_password:str
#    database_name:str
#    database_username:str
#    secret_key:str
#    algorithm:str
#    access_token_expire_minutes:int
  
#    class Config:
#        env_file=".env"


# settings= Settings()



# uvicorn mainapi:app --reload

while True :
    
   try:
      engine= create_engine('mysql+pymysql://arjangillmain:gill12391@p3nlmysql77plsk.secureserver.net:3306/ph16873094761_', pool_recycle=3600)

      sessionlocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

      base= declarative_base()
      
                 
      break
   except Exception as error:
         print("connection to database was failed")
         print("Error was",error)
         time.sleep(2)# waits 2 sec before trying again


connection = engine.connect()
# cursor_factory= RealDictCursor
connection = connection.execution_options(
isolation_level="READ COMMITTED")
def get_db(): # TO GET CONNECTION TO DATABASE
                  db= sessionlocal()
                  try:
                     yield db
                  finally:
                     db.close()

# if (engine.is_connected()):
#     print("Connected")
# else:
#     print("Not connected")

class data(base):
    __tablename__="product_2"
    
    id= Column(Integer,primary_key=True,nullable=False)
    company=Column(String(300),nullable=False,)
    model=Column(String(300),nullable=False)
    power_rating=Column(String(3000),nullable=False)
    description=Column(String(3000),nullable=False)
    specification=Column(String(3000),nullable=False)


class image(base):
    __tablename__="img_src"
    data_id=Column(Integer,ForeignKey("product_detail.id",ondelete="cascade"), primary_key=True)
    img_1=Column(String(30),nullable=False)
    img_2=Column(String(30),nullable=False)
    img_3=Column(String(30),nullable=False)


class get_id(BaseModel):
    
    id:int
    class Config:
        orm_mode=True
        
class post_html(BaseModel):
    
    company:str
    model:str
    power_rating:str
    description:str
    specification:str


 
#     class Config:
#         orm_mode=True


# class Token(BaseModel):
#     access_token:str
#     token_type:str

# class TokenData(BaseModel):
#     id:Optional[str] = None

# class UserCreate(BaseModel):
#     username:str
#     password:str

# class UserLogin(BaseModel):
#     username:str
#     password:str

# class UserResponce(BaseModel):
#     id:int
#     username:str
#     class Config:
#         orm_mode=True

# class dates(BaseModel):
#     date_from:date
#     date_to:date
#     @validator("date_from","date_to", pre=True)
#     def prase_formatted_datetime(cls, value):
#         return datetime.strptime(
            
#             value,
#              "%d-%m-%Y"
#         )

# class response(BaseModel):
#     id:int
#     formatted_datetime:str
#     type_val:int
#     detail:str
#     amount:int

   
#     class Config:
#         orm_mode=True














# SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 1440

# def create_access_token(data:dict):
#    to_encode= data.copy()
#    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#    to_encode.update({'exp':expire})

#    encoded_jwt= jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM) #(datalode, secret key, algorithm)
#    return encoded_jwt


# def verify_access_token(token:str,credentials_exceptions):
#     try:
#         payload=jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
#         id:str=payload.get("user_id")

#         if  id is None:
#            raise credentials_exceptions
#         token_data=TokenData(id=id)

#     except JWTError:  
#         raise credentials_exceptions
    
#     return token_data
    
# def get_current_user(token:str = Depends(oauth2_scheme), db:Session=Depends(get_db)):
#     credentials_exceptions=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials",headers={"WWW-Authrnticate":"Bearer"})   
    
#     token= verify_access_token(token,credentials_exceptions)
#     user=db.query(User).filter(User.id==token.id).first()

#     return user





# def hash(password:str):
    
#     return pbkdf2_sha256.hash(password)


# def verify(plain_pass,harsh_pass):#fun gives the value of true or false
#     print(plain_pass)
#     print(harsh_pass)
    
#     x =pbkdf2_sha256.verify(plain_pass, harsh_pass)
    
   
#     return x






base.metadata.create_all(bind=engine)
app=FastAPI()
handler=Mangum(app)
origions=["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],#domains which 
    allow_credentials=True,
     allow_methods=["*"],# allow specific mehods(get,update)
    allow_headers=["*"],#allwo which headers
 )

@app.get('/')
def home():
   return{
      "message":"we are in home baby"
   }


@app.post("/get")
def get_posts(ids:get_id, db: Session=Depends(get_db)):

    aa=db.query(data).filter(data.id==ids.id).first()
    ia=db.query(image).filter(image.data_id==ids.id).first()
    # sql=text("SELECT * FROM img_src WHERE id= {0} " .format(idd) )
   #  print(aa)
   #  im=db.query(image).filter(image.data_id==ids.id).first()
   #  print(im)
  
    return aa,ia

@app.post("/post")
def post_img(pp:post_html, db: Session=Depends(get_db)):
    trans = connection.begin()

    print(pp)
    mydict=pp.dict()
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
    sql = text("INSERT INTO %s ( %s ) VALUES ( %s );" % ('product_detail', columns, values))
    connection.execute(sql)
    trans.commit()
    return {"hi":"oops"}

# @app.post("/send_mail")
# async def send_mail(email: EmailSchema):

# 	template = """
# 		<html>
# 		<body>
		

# <p>Hi !!!
# 		<br>Thanks for using fastapi mail, keep using it..!!!</p>


# 		</body>
# 		</html>
# 		"""

# 	message = MessageSchema(
# 		subject="Fastapi-Mail module",
# 		recipients=email.dict().get("email"), # List of recipients, as many as you can pass
# 		body=template,
# 		subtype="html"
# 		)

# 	fm = FastMail(conf)
# 	await fm.send_message(message)
# 	print(message)

	

# 	return JSONResponse(status_code=200, content={"message": "email has been sent"})


# @app.get("/latest")
# def get_posts( db: Session=Depends(get_db),current_user:int =Depends(get_current_user)):
#     user = db.query(User).filter(User.id == current_user.id).first()
#     query = db.query(Income.amount).filter(Income.is_deleted==False,Income.user_id==current_user.id,Income.type_val==1).all()
#     query_exp=db.query(Income.amount).filter(Income.is_deleted==False,Income.user_id==current_user.id,Income.type_val==2).all()
#     query_pay=db.query(Income.amount).filter(Income.is_deleted==False,Income.user_id==current_user.id,Income.type_val==3).all()
#     a=0
#     b=0
#     c=0
#     for i in query:
#        a=a+i[0]
#     print(a)
#     for i in query_exp:
#        b=b+i[0]

#     for i in query_pay:
#        c=c+i[0]
#     profit=a-(b+c)  
    
#     return  {"profit":profit,"usernaem":user.username}


# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_post(db: Session=Depends(get_db)):
    
#     deytail=dd.dict()
#     new_post=data(**deytail)

#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return ("uploaded")



# @app.put("/delete/{id}")
# def delete_post(id:int,db: Session = Depends(get_db),current_user:int =Depends(get_current_user)): #id is integer
#     print(id)
#     id_user=current_user.id
#     post= db.query(Income).filter(Income.id==id,Income.user_id==id_user).first()
#     post.is_deleted=True
    
 
#     db.commit()
#     return ("Post deleted")


# @app.post("/user",status_code=status.HTTP_201_CREATED, response_model=UserResponce)
# def create_user(new_user:UserCreate,db: Session = Depends(get_db)):
#    #has the password- user.passowrd
#    hashed_password=hash(new_user.password)
#    print(hashed_password)
#    new_user.password= hashed_password
   
#    user=User(**new_user.dict())
#    print(user)
#    db.add(user)
#    db.commit()
#    db.refresh(user)
#    return user




# @app.post('/login')
# def login( user_credentials:UserLogin, db:Session = Depends(get_db)):
#  user = db.query(User).filter(User.username == user_credentials.username).first()
#  username = db.query(User.username).filter(User.username == user_credentials.username).first()
#  if not user:
#   raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credentials")
 
#  if not verify( user_credentials.password,user.password): #if it is true, returns token,,,,if not it raises an exception
#   raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")

#  access_token=create_access_token(data={"user_id": user.id})
#  print(access_token)
#  return{"access_token": access_token, "token_type":"bearer","user_name":user.username}

