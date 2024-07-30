import azure.functions as func
import logging
import random
from datetime import datetime
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="v1/mock/forexrates", methods=["GET"])
def mock_forex_rates(req: func.HttpRequest) -> func.HttpResponse:
	logging.info('Python HTTP trigger function processed a request for mock forex rates.')

	# Generate random exchange rates
	quotes = {
		"GBPAED": round(random.uniform(4.0, 6.0), 6),
		"GBPAFN": round(random.uniform(100.0, 110.0), 6),
		"GBPALL": round(random.uniform(130.0, 150.0), 6),
		"GBPAMD": round(random.uniform(700.0, 750.0), 6),
		"GBPANG": round(random.uniform(2.0, 3.0), 6),
		"GBPAOA": round(random.uniform(900.0, 950.0), 6),
		"GBPARS": round(random.uniform(120.0, 140.0), 6),
		"GBPAUD": round(random.uniform(1.5, 2.0), 6),
		"GBPAWG": round(random.uniform(2.0, 3.0), 6),
		"GBPAZN": round(random.uniform(2.0, 3.0), 6),
		"GBPBAM": round(random.uniform(2.0, 3.0), 6),
		"GBPBBD": round(random.uniform(2.0, 3.0), 6),
		"GBPBDT": round(random.uniform(110.0, 120.0), 6),
		"GBPBGN": round(random.uniform(2.0, 3.0), 6),
		"GBPBHD": round(random.uniform(0.5, 1.0), 6),
		"GBPBIF": round(random.uniform(2700.0, 2800.0), 6),
		"GBPBMD": round(random.uniform(1.0, 2.0), 6),
		"GBPBND": round(random.uniform(1.5, 2.0), 6),
		"GBPBOB": round(random.uniform(9.0, 10.0), 6),
		"GBPBRL": round(random.uniform(7.0, 8.0), 6),
	}

	response = {
		"success": True,
		"timestamp": datetime.now().strftime("%d-%m-%Y"),
		"source": "GBP",
		"quotes": quotes
	}

	return func.HttpResponse(
		body=json.dumps(response),
		status_code=200,
		mimetype="application/json"
	)