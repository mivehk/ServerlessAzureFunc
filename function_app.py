import azure.functions as func
import logging
from datetime import datetime

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="HttpTrigger1")
def HttpTrigger1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    Zaman =datetime.now()
    ZamanFormated = Zaman.strftime("%m/%d/%Y %H:%M:%S") 
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}.<br> This Azure serverless function was Http triggered successfully at {ZamanFormated}, when you browsed the link", mimetype="text/html")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
