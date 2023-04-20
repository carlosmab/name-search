# main.py
import os
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

port = int(os.environ.get('API_PORT', '5000'))
host = os.environ.get('API_HOST', '0.0.0.0')
    
if __name__ == "__main__":
    uvicorn.run("app.api:app", host=host, port=port, reload=True)