from fastapi import FastAPI
from command_pros import command_retriever
from model import CommandRetriever
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
import time
import configparser

app = FastAPI(title="Command Retrieval System", description="Simplify the process of recalling and executing commands for individual applications/OS.", version="0.0.1")

config = configparser.ConfigParser()
config.read('config.ini')

#configuration retrieval 
app_host = config['app']['host']
app_port = config['app']['port']

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = round(time.time() - start_time, 4)
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.post('/command-retriever',response_class = JSONResponse)
async def fetch_commands(request: CommandRetriever):
    user_input = request.input_text
    product = request.product
    result_json = command_retriever(user_input, product)
    return result_json

@app.get("/")
async def root():
    return {"message": "Hello World"}