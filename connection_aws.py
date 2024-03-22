import boto3
from dotenv import find_dotenv,load_dotenv
load_dotenv(find_dotenv())
import os

class Connection_Aws:
    def __init__(self,aws_access_key_id : str,aws_secret_access_key : str,region_name : str):
        self.__aws_access_key_id = aws_access_key_id
        self.__aws_secret_access_key = aws_secret_access_key
        self.__region_name = region_name
        boto3.setup_default_session(self.__aws_access_key_id,self.__aws_secret_access_key,self.__region_name)


