import logging

import azure.functions as func

import os
import mimetypes

def main(req: func.HttpRequest) -> func.HttpResponse:

    """ server1.startServer() """
    os.system("python server1.py index.html")
    
    logging.info('Python HTTP trigger function processed a request.')

    name = 'index.html'

    if name:
        #return func.HttpResponse(f"Hello {name}!")
        #path = 'static-file' # or other paths under `MyFunctionProj`
        filename = f"C:/Users/rferrugento/Desktop/Project folder/Send_Site/Send_Site/{name}"
        with open(filename, 'rb') as f:
            mimetype = mimetypes.guess_type(filename)
            return func.HttpResponse(f.read(), mimetype=mimetype[0])
    else:
        return func.HttpResponse(
                "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
                status_code=200
        )
